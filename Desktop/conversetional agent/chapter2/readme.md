
# Chapter 2: Language Translator with LangChain and Gemini Pro

This chapter showcases how to create a simple language translator using the **Gemini 1.5 Pro** model via LangChain, along with safe and customizable prompt engineering.

## 🧠 Features

- Uses `gemini-1.5-pro` model
- Custom prompt template for translation
- Language translation from English to Arabic
- Safety settings configuration
- Deterministic output with temperature control

## 🚀 Requirements

- Python 3.8+
- Google Gemini API Key
- `.env` file with API key

## 📦 Install Dependencies

```bash
pip install python-decouple langchain-google-genai langchain-core
```

## 🔐 .env Setup

Create a `.env` file in the `chapter-2/` directory with the following:

```
GENAI_API_KEY=your_gemini_api_key_here
```

## ▶️ Run the Code

```bash
python main.py
```

## 📄 main.py Overview

```python
from decouple import config
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    HarmBlockThreshold,
    HarmCategory,
)
from langchain_core.prompts import ChatPromptTemplate

SECRET_KEY = config('GENAI_API_KEY')

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    api_key=SECRET_KEY,
    safety_settings={
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    },
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that translates {input_language} to {output_language}."),
    ("human", "{input}"),
])

chain = prompt | llm

res = chain.invoke({
    "input_language": "English",
    "output_language": "arabic",
    "input": "I love programming.",
})

print(res.content)
```

This script creates a translation assistant that takes dynamic input/output languages and prints the translated result using Gemini Pro.

```