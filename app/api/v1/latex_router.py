from fastapi import APIRouter, Depends
from fastapi.responses import Response
from typing import List
from app.schemas.ai import Paper
from app.schemas.user import LatexDocSchema
from app.services.latex_service import LaTeXService

router = APIRouter()


def get_latex_service():
    return LaTeXService()


@router.post("/paper-review")
async def generate_paper_review(
    papers: List[Paper],
    paper_name: str,
    latex_service: LaTeXService = Depends(get_latex_service),
):
    """Generate a LaTeX paper review from a list of papers"""
    return await latex_service.generate_paper_review(papers, paper_name)


@router.post("/render")
async def render_latex(
    request: LatexDocSchema,
    latex_service: LaTeXService = Depends(get_latex_service),
):
    """Render LaTeX content to PDF"""
    pdf_content = await latex_service.render_latex(request.latex)
    return Response(
        content=pdf_content,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=rendered.pdf"},
    )
