from openai import AsyncOpenAI
from app.config import settings

client = AsyncOpenAI(base_url=settings.client_provider, api_key=settings.client_api)

SYSTEM_PROMPT = """you are a helpful assistant that answers questions
ONLY using the document provided below. If the answer is not in the document, say
"I can't find that in the document"  
DOCUMENT:
"""

async def get_ai_reply(document_text: str, history: list[dict], user_message: str) -> str:

    messages = [
        {'role': 'system', 'content': SYSTEM_PROMPT + document_text},
        *history,
        {'role': 'user', 'content': user_message}
    ]

    response = await client.chat.completions.create(
        model=settings.client_model,
        messages=messages,
    )

    return response.choices[0].message.content
