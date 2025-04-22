from decouple import config
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    HarmBlockThreshold,
    HarmCategory,
)
from langchain_core.prompts import ChatPromptTemplate

SECRET_KEY = config('GENAI_API_KEY')


llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro",api_key=SECRET_KEY, 
safety_settings={
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    },
                             temperature=0, 
                             max_tokens=None,
                             timeout=None,
                             max_retries=2,)
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ]
)
 
chain = prompt | llm
res= chain.invoke(
    {
        "input_language": "English",
        "output_language": "arabic",
        "input": "I love programming.",
    }
)

print(res.content)