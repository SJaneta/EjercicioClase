import openai
from pydantic import BaseModel

openai.organization = 'org-J0y1yI2sOfB5bhErJ2Ul9UrT'
openai.api_key = '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'


class Document(BaseModel):
    item: str = 'pizza'


def process_inference(user_prompt) -> str:
    print('[PROCESANDO]'.center(40, '-'))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Eres un chef que lista los ingredientes de los platillos que se te proporcionan.
        E.G
        pan
        Ingredientes:
        arina
        huevos
        agua
        azucar
        ...
        """},
            {"role": "user", "content": user_prompt}
        ]
    )
    response = completion.choices[0].message.content
    return response
