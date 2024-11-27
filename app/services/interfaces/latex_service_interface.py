from abc import ABC, abstractmethod
from typing import List
from app.schemas.ai import Paper


class LaTeXServiceInterface(ABC):
    @abstractmethod
    async def generate_paper_review(self, papers: List[Paper], paper_name: str) -> str:
        """Generate a LaTeX paper review file from a list of papers and paper name

        Args:
            papers: List of papers to review
            paper_name: Name of the paper review

        Returns:
            str: Generated LaTeX content
        """
        pass

    @abstractmethod
    async def render_latex(self, latex_content: str) -> bytes:
        """Render LaTeX content to PDF

        Args:
            latex_content: LaTeX content to render

        Returns:
            bytes: PDF content
        """
        pass
