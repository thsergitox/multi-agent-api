from openai import OpenAI
from app.config import settings
from app.schemas.ai import UserAIRequest
from app.services.interfaces.ai_service_interface import AIChatbotServiceInterface


class AIChatbotService(AIChatbotServiceInterface):
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.initial_prompt = """
        Eres un asistente experto en redacción académica e investigación. Tu objetivo es ayudar a mejorar la calidad de un artículo científico proporcionando sugerencias bien fundamentadas basadas en los abstracts y títulos de otros trabajos de investigación. Tienes acceso a los siguientes abstracts con sus respectivos títulos, que representan el estado del arte en el campo:

        {array}

        El usuario proporcionará una sección específica de su artículo científico en latex (por ejemplo, Introducción, Metodología, Resultados, Discusión, o Conclusiones) junto con una solicitud detallada. Tu tarea es:

        1. Leer y entender el contenido proporcionado por el usuario.
        2. Analizar cómo puede mejorar esa sección, ya sea en términos de claridad, profundidad, estructura o relevancia.
        3. Utilizar los abstracts y títulos proporcionados para sugerir referencias, ideas adicionales o argumentos que enriquezcan el contenido.
        4. Proponer un texto reescrito o modificado, siguiendo las indicaciones del usuario y respetando el tono y estilo académico.

        Todas las sugerencias y mejoras deben ser claras, bien justificadas y alineadas con las prácticas de escritura académica. Si detectas algún problema en la coherencia, gramática o formato del texto proporcionado, también indícalo y sugiere correcciones incluyendo solo los cambios del latex y la explicación.

        ¿Entendido? Comencemos.
        """

    def _format_papers(self, papers):
        """Format papers into the expected dictionary format"""
        return [
            {
                "title": paper.title,
                "authors": paper.authors,
                "abstract": paper.abstract,
                "published": paper.published,
                "updated": paper.updated,
                "pdf_url": paper.pdf_url,
                "entry_id": paper.entry_id,
                "categories": paper.categories,
            }
            for paper in papers
        ]

    def _format_messages(self, messages):
        """Format chat messages into the expected format"""
        return [{"role": msg.role, "content": msg.content} for msg in messages]

    async def process_chatbot_request(self, request: UserAIRequest):
        """Process an AI chatbot request and return the response"""
        try:
            # Format the input data
            formatted_messages = self._format_messages(request.messages)
            formatted_papers = self._format_papers(request.papers)

            # Prepare the messages for the API call
            messages = [{"role": "system", "content": self.initial_prompt}]
            messages.extend(formatted_messages)

            # Make the API call
            response = self.client.chat.completions.create(
                model="gpt-4o-mini", messages=messages
            )

            return response.choices[0].message
        except Exception as e:
            return str(e)
