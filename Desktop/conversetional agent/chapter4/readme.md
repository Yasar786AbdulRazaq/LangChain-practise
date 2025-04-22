
# Chapter 4: Language Translator with Dynamic Inputs in LangChain

This chapter enhances the translation example by allowing more flexible and dynamic language input and output using **Gemini 1.5 Flash** and LangChain’s message templates.

## 🧠 Features

- Uses `gemini-1.5-flash` model
- Translates text from one language to another
- Dynamic language input and output
- Simple and customizable prompt chaining

## 🚀 Requirements

- Python 3.8+
- Google Gemini API Key
- `.env` file with API key

## 📦 Install Dependencies

```bash
pip install python-decouple langchain-google-genai langchain-core
```

## 🔐 .env Setup

Create a `.env` file in the `chapter-4/` directory:

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

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=SECRET_KEY)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a translator {language_input} to {language_output}."),
    ("human", "{input}"),
])

chain = prompt | llm

res = chain.invoke({
    "language_input": "English",
    "language_output": "hindi",
    "urdu": "i love you"
})

print(res.content)
```

## ⚠️ Note

There is a minor issue in the `res = chain.invoke(...)` block: the `input` key is expected in the prompt, but `urdu` is used instead. It should be:

```python
res = chain.invoke({
    "language_input": "English",
    "language_output": "hindi",
    "input": "i love you"
})
