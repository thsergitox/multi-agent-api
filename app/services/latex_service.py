import os
import string
import secrets
import subprocess
from typing import List
from app.schemas.ai import Paper
from app.services.interfaces.latex_service_interface import LaTeXServiceInterface
from fastapi import HTTPException


class LaTeXService(LaTeXServiceInterface):
    def __init__(self):
        self.template = r"""
\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[english]{babel}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage[left=2cm,right=2cm,top=2cm,bottom=2cm]{geometry}
\usepackage{hyperref}
\usepackage{natbib}

\title{%s}
\author{Paper Review}
\date{\today}

\begin{document}

\maketitle

\section{Introduction}
This document presents a review of recent papers in the field. The papers reviewed cover various aspects and developments in the area.

\section{Papers Reviewed}
%s

\section{Conclusion}
This review has covered several important papers in the field, highlighting key developments and findings.

\end{document}
"""

    def _generate_random_string(self, length=8):
        """Generate a random string for temporary file names"""
        characters = string.ascii_letters + string.digits
        return "".join(secrets.choice(characters) for _ in range(length))

    def _format_paper_section(self, paper: Paper) -> str:
        """Format a single paper into a LaTeX subsection"""
        authors = " and ".join(paper.authors)
        return f"""
\\subsection{{{paper.title}}}
\\textbf{{Authors:}} {authors}\\\\
\\textbf{{Published:}} {paper.published}\\\\
\\textbf{{Categories:}} {paper.categories}\\\\
\\textbf{{Paper URL:}} \\url{{{paper.pdf_url}}}

\\subsubsection{{Abstract}}
{paper.abstract}

"""

    async def generate_paper_review(self, papers: List[Paper], paper_name: str) -> str:
        """Generate a LaTeX paper review file from a list of papers and paper name"""
        # Format each paper into a LaTeX section
        papers_content = "\n".join(
            self._format_paper_section(paper) for paper in papers
        )

        # Generate the complete LaTeX document
        latex_content = self.template % (paper_name, papers_content)

        return latex_content

    async def render_latex(self, latex_content: str) -> bytes:
        """Render LaTeX content to PDF"""
        try:
            # Create unique tag for this render
            tag = self._generate_random_string()

            # Setup directories
            root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            render_dir = "backend"
            full_render_dir = f"{root_dir}/{render_dir}"

            # Clean and create render directory
            os.system(f"rm -f {full_render_dir}/*")
            os.makedirs(full_render_dir, exist_ok=True)

            # Write LaTeX content to file
            file_path = os.path.join(full_render_dir, f"{tag}.tex")
            with open(file_path, "w") as file_object:
                file_object.write(latex_content.replace("\\\\", "\\"))

            # Compile LaTeX to PDF
            compile_command = [
                "docker",
                "run",
                "--rm",
                "-v",
                f"{full_render_dir}:/workdir",
                "texlive/texlive",
                "pdflatex",
                f"{tag}.tex",
            ]

            result = subprocess.run(
                compile_command, cwd=full_render_dir, capture_output=True, text=True
            )

            if result.returncode != 0:
                raise HTTPException(status_code=501, detail=result.stderr)

            # Read the generated PDF
            pdf_path = os.path.join(full_render_dir, f"{tag}.pdf")
            with open(pdf_path, "rb") as pdf_file:
                pdf_content = pdf_file.read()

            return pdf_content

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
