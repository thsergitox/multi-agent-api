class LatexService:
    def __init__(self, latex_template: str):
        self.latex_template = latex_template

    def render(self, context: dict) -> str:
        return self.latex_template.format(**context)