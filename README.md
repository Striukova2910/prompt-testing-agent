# prompt-testing-agent
# 🤖 Multi-Agent Prompt Testing App

This app lets you **test and evaluate prompts** for AI chatbots using **three interacting agents**:

1. **User Agent** — acts like a user asking questions and follow-ups.
2. **Business Agent** — answers based on a given system prompt (for example, a tech support bot).
3. **Analyzer Agent** — reviews the whole dialogue and scores the Business Agent using a checklist.

The goal is to check if your prompts make the AI behave correctly and stay within the topic.

---

## 🚀 Features

* Interactive interface built with **Streamlit**
* Upload or edit your own prompts, test cases, and evaluation checklist
* Choose different **OpenAI models** (`gpt-4o`, `gpt-3.5-turbo`)
* Adjustable **temperature** for creativity control
* Automatic dialogue generation and analysis
* Random “trap” questions to test robustness

---

## 🧩 Project Structure

```
mainVisual.py       → Launches the Streamlit app
choice1.py          → (Same logic variant) defines the showWindow() function
business_agent.py   → Defines the business agent (uses LangChain + ChatOpenAI)
user_agent.py       → Generates user questions and follow-ups
analyzer_agent.py   → Evaluates the dialogue using a checklist
```

---

## 🛠️ Requirements

* Python 3.10+
* Streamlit
* LangChain
* OpenAI
* python-dotenv

Install dependencies:

```bash
pip install streamlit langchain-openai python-dotenv
```

---

## ⚙️ How to Run

1. Add your OpenAI API key in a `.env` file:

   ```
   OPENAI_API_KEY=your_api_key_here
   ```
2. Run the app:

   ```bash
   streamlit run mainVisual.py
   ```
3. The Streamlit window will open in your browser.

---

## 💡 How It Works

1. The **User Agent** generates a main question and several follow-ups.
2. The **Business Agent** replies to each one according to its system prompt.
3. The **Analyzer Agent** reads the full dialogue and rates the Business Agent based on your checklist.

You can change prompts, test cases, or trap questions in the sidebar to test different behaviors.

---

## 📈 Example Use

* Test support bot responses within a specific domain (e.g., Machine Learning).
* Check if the bot avoids forbidden or political topics.
* Compare results between GPT models and temperatures.

---

## 🧠 Credits

Created for **prompt engineering and AI behavior testing** using Streamlit and LangChain.
