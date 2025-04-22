from decouple import config
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate ,FewShotPromptTemplate

SECRET_KEY = config('GENAI_API_KEY')


llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=SECRET_KEY)
example_prompt = PromptTemplate.from_template("Question:{question}\n){answer}\n")
examples =  [
    {
        "question": "What is the capital of France?", "answer": "Paris."
        },
    {"question": "What is the capital of Germany?", "answer": "Berlin."},
    {"question": "What is the capital of Italy?", "answer": "Rome."},
    {"question": "What is the capital of Spain?", "answer": "Madrid."},
    {"question": "What is the capital of Japan?", "answer": "Tokyo."},
    {"question": "What is the capital of China?", "answer": "Beijing."},
    {"question": "What is the capital of India?", "answer": "New Delhi."},
    {"question": "What is the capital of Brazil?", "answer": "Brasilia."},
    {"question": "What is the capital of Canada?", "answer": "Ottawa."},
    {"question": "What is the capital of Australia?", "answer": "Canberra."},
    {"question": "one plus one", "answer": "two"},
    {"question": "two plus two", "answer": "four"}
]

prompt= FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question:{input}",
    input_variables=["input"],
)

my_prompt=prompt.format_prompt(input="40+40")
res = llm.invoke(my_prompt)
print(res.content)