from decouple import config
from langchain_google_genai import ChatGoogleGenerativeAI

SECRET_KEY = config('GENAI_API_KEY')


llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=SECRET_KEY)
res = llm.invoke("what are you doing.")
print(res.content)