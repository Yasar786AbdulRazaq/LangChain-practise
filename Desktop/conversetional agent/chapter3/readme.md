
# Chapter 3: Dynamic Joke Generator using Gemini and LangChain

In this chapter, you'll learn how to use **dynamic variables** in prompts to generate customized jokes using the **Gemini 1.5 Flash** model via LangChain.

## 🧠 Features

- Uses `gemini-1.5-flash` model
- Dynamically inserts variables (`topic`, `language`) into prompts
- Uses `ChatPromptTemplate` for formatting
- Outputs jokes based on user-defined topics and languages

## 🚀 Requirements

- Python 3.8+
- Google Gemini API Key
- `.env` file with API key

## 📦 Install Dependencies

```bash
pip install python-decouple langchain-google-genai langchain-core
```

## 🔐 .env Setup

Create a `.env` file in the `chapter-3/` directory:

```
GENAI_API_KEY=your_gemini_api_key_here
```

## ▶️ Run the Code

```bash
python main.py
```

## 📄 Code Overview

```python
from decouple import config
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

SECRET_KEY = config('GENAI_API_KEY')

llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash", api_key=SECRET_KEY)

topic = "monky"
language = "Urdu"

prompt_template = ChatPromptTemplate.from_template("Tell me a joke about {topic} in {language}.")

messages = prompt_template.format_messages(topic=topic, language=language)

res = llm.invoke(messages)

print(res.content)
```

## 📌 How It Works

- A prompt template is created with placeholders for `topic` and `language`.
- These variables are filled dynamically to personalize the response.
- Gemini returns a joke based on the given topic and language.
