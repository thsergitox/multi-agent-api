from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import LatexDocSchema
import os
import string
import secrets
from fastapi.responses import FileResponse
import subprocess



router = APIRouter()

def generate_random_string(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))


@router.post("/render-latex")
async def render_latex(request: LatexDocSchema):
    latex = request.latex
    unsanitized_latex_content = latex.replace('\\\\', '\\')

    tag = generate_random_string()
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    render_dir = f"backend"
    os.system(f"rm -f {render_dir}/*")

    os.makedirs(f"{root_dir}/{render_dir}", exist_ok=True)
    file_path = os.path.join(f"{root_dir}/{render_dir}", f"{tag}.tex")
    with open(file_path, "w") as file_object:
        file_object.write(unsanitized_latex_content)
    try:
        compile_command = [
            "docker", "run", "--rm",
            "-v", f"{root_dir}/{render_dir}:/workdir",
            "texlive/texlive", "pdflatex", f"{tag}.tex"
        ]
        result = subprocess.run(compile_command, cwd=f"{root_dir}/{render_dir}/", capture_output=True, text=True)
        print(result)
        if result.returncode != 0:
            raise HTTPException(status_code=501, detail=result.stderr)

    except Exception as e:
        print("something", e)
        raise HTTPException(status_code=500, detail=str(e))
    response = FileResponse(f"{root_dir}/{render_dir}/{tag}.pdf")
    
    return response
