from decouple import config
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Load API key
SECRET_KEY = config('GENAI_API_KEY')

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash", api_key=SECRET_KEY)

# Define your variables
topic = "monky"
language = "Urdu"

# Use variables in the prompt template
prompt_template = ChatPromptTemplate.from_template("Tell me a joke about {topic} in {language}.")

# Format the prompt with your variables
messages = prompt_template.format_messages(topic=topic, language=language)

# Get response
res = llm.invoke(messages)

# Print the result
print(res.content)
