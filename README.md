## Lectures Overview

### Lecture 1: **Basic Setup with Google Generative AI**

In this lecture, we initialize the Google Generative AI model using LangChain. We use the `ChatGoogleGenerativeAI` class to connect to the model and invoke it to get a simple response. The example given is a basic interaction where the model responds to the prompt "What are you doing?"

---

### Lecture 2: **Basic Translation with LangChain**

This lecture demonstrates how to build a basic translation agent using LangChain. We define the `ChatPromptTemplate` to format user input and output for translation. The model is then invoked to translate the sentence "I love programming" from English to Arabic.

---

### Lecture 3: **Using Variables in Prompts**

In this lecture, we make the translation agent more dynamic by passing variables into the prompt. The code demonstrates how to tell a joke about a specific topic (e.g., "monkey") in a specified language (e.g., Urdu) using LangChain and the Google Generative AI model.

---

### Lecture 4: **Language Translation with Input/Output Customization**

This lecture focuses on customizing input and output languages using LangChain and Google Generative AI. In this example, the model translates an English sentence ("I love you") to Hindi, demonstrating how to dynamically change both the input and output languages using variables.

---

### Lecture 5: **Using Few-Shot Prompting for Dynamic Responses**

In this final lecture, we introduce few-shot prompting where we provide the model with examples to improve its responses. The code demonstrates how the model answers dynamic questions, like mathematical equations (e.g., "40+40"), based on the provided examples of capital cities.

---

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Yasar786AbdulRazaq/lanGchain-practise.git
   cd lanGchain-practise
   ```

2. **Install the required packages**:

   Make sure you have `python-dotenv`, `langchain`, and other dependencies installed. You can use `pip` or `poetry` to install the necessary libraries.

   ```bash
   pip install -r requirements.txt
   ```

3. **Setup the environment**:

   Create a `.env` file and add your `GENAI_API_KEY`:

   ```bash
   GENAI_API_KEY=your-api-key-here
   ```

4. **Run the code**:

   To run any of the lectures' code, just execute the corresponding `main.py` file.

   ```bash
   python chapter1/main.py
   ```
