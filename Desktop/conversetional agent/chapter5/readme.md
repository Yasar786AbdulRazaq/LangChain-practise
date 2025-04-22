
# Chapter 5: Few-Shot Prompting with LangChain and Gemini

This chapter demonstrates how to use **Few-Shot Prompting** to provide multiple examples to the model for more accurate and context-aware answers using **Gemini 1.5 Flash**.

## 🧠 Features

- Uses `gemini-1.5-flash` model
- Implements Few-Shot Prompting with LangChain
- Provides example Q&A pairs to improve response accuracy
- Custom math and general knowledge Q&A logic

## 🚀 Requirements

- Python 3.8+
- Google Gemini API Key
- `.env` file with API key

## 📦 Install Dependencies

```bash
pip install python-decouple langchain-google-genai langchain-core
```

## 🔐 .env Setup

Create a `.env` file in the `chapter-5/` directory:

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
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

SECRET_KEY = config('GENAI_API_KEY')

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=SECRET_KEY)

example_prompt = PromptTemplate.from_template("Question:{question}\n){answer}\n")

examples = [
    {"question": "What is the capital of France?", "answer": "Paris."},
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

prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question:{input}",
    input_variables=["input"],
)

my_prompt = prompt.format_prompt(input="40+40")
res = llm.invoke(my_prompt)

print(res.content)
```

## 📌 How It Works

- A list of example Q&A pairs is passed to the model.
- The model learns from these examples and answers similar queries.
- `FewShotPromptTemplate` structures the format for consistency.
- You provide a new question, and the model answers based on the learned pattern.
