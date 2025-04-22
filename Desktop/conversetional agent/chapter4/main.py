from decouple import config
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
SECRET_KEY = config('GENAI_API_KEY')


llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=SECRET_KEY)
prompt=ChatPromptTemplate.from_messages([
    ("system",
      "You are a translator {language_input} to {language_output}."),
    ("human", "{input}"),
]
)
chain=prompt|llm
res=chain.invoke(
   {"language_input":"English", "language_output": "hindi", "urdu": "i love you"}
)
print(res.content)