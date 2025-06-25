# 🧠 Persona-Powered Debate Agent

A web-based debate simulation tool that uses LLM agents to generate persuasive, persona-driven arguments across structured debate rounds — including autonomous judging and user interaction modes.

🌐 **Live App:** [debate-agents.streamlit.app](https://debate-agents.streamlit.app)

---

## 📌 Overview

This project enables users to simulate formal debates between two personas—either 🤖 AI vs AI or 🧑 User vs AI—on a selected topic. The system uses **LLM-powered agents** to generate structured arguments and rebuttals across three formal debate rounds: **Constructive, Rebuttal, and Closing**.

At the end of the debate, a third **Judge Agent** evaluates the full transcript and provides:
- A verdict on the winner
- Constructive feedback for both debaters

---

## 🧑‍💻 Developer Highlights

- Designed and implemented a **3-agent system**: two debating personas and one autonomous LLM judge
- Built **two interaction modes**: AI vs AI and User vs AI
- Applied **prompt engineering techniques** to guide LLM behavior across structured debate phases
- Enabled context-aware rebuttals with evolving argument flow and reduced repetition
- Deployed using **Streamlit** for accessible UI and interactive simulation

---

## 🧰 Tech Stack

- Python  
- Streamlit  
- Together AI API  
- LLaMA 3 (meta-llama/Llama-3-8b-chat-hf)  
- Prompt Engineering  
- dotenv

---

## 🎯 Features

- ✍️ User vs AI or 🤖 AI vs AI modes  
- 💬 Realistic 3-round debate structure (Constructive → Rebuttal → Closing)  
- 🧠 Customizable personas with guided roles  
- 🔁 Rebuttals include new arguments, not just reworded points  
- 👨‍⚖️ AI Judge provides verdict and feedback based on transcript  

---

## 🔁 Debate Flow

| Phase        | Persona 1               | Persona 2               |
|--------------|-------------------------|-------------------------|
| Constructive | Presents opening case   | Presents counter-case   |
| Rebuttal     | Rebuts and adds point   | Rebuts and adds point   |
| Closing      | Summarizes key arguments| Summarizes key arguments|

Each turn is generated using context-aware LLM prompts based on:
- The debate topic  
- The speaker's persona description  
- Debate phase (e.g., Constructive, Rebuttal, Closing)  
- Full transcript up to that point

---

## 🧠 Prompt Engineering Strategy

Prompt engineering is used to ensure the debate follows structured, logical, and persuasive patterns. Each round type has its own prompt logic.

### 🔧 Sample Prompt Logic:
```python
if mode == "constructive":
    prompt = (
        f"You are {persona}. Present a constructive argument for the topic '{topic}'.\n"
        "Focus on presenting main points clearly with evidence and reasoning. Do not address the opponent yet.\n\n"
        f"Debate so far:\n{history_text if history else 'None'}"
    )
elif mode == "rebuttal":
    prompt = (
        f"You are {persona}. Rebut your opponent's last point and add a new argument on the topic '{topic}'.\n"
        "Be persuasive, avoid repeating points from earlier.\n\n"
        f"Debate so far:\n{history_text if history else 'None'}"
    )
elif mode == "closing":
    prompt = (
        f"You are {persona}. Deliver a compelling closing statement for the debate on '{topic}'.\n"
        "Summarize your strongest points without introducing new arguments.\n\n"
        f"Debate transcript:\n{history_text if history else 'None'}"
    )
```

This prompt logic ensures:
- Persona-specific tone and behavior  
- Clear role separation across rounds  
- Logical progression of arguments  
- Rebuttals are fresh and non-repetitive  

---

## ⚖️ Judging Agent

After the final round, a third LLM agent (the **Judge**) is prompted to:
- Review the full transcript  
- Identify the stronger side based on clarity, logic, and persuasiveness  
- Provide feedback to each persona on how to improve

This reinforces the educational or coaching potential of the tool.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/persona-debate-agent.git
cd persona-debate-agent
```

### 2. Set Up Environment Variables
Create a `.env` file in the root directory:
```
TOGETHER_API_KEY=your_api_key_here
```

> ⚠️ `.env` is listed in `.gitignore` – do not commit your key.

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch the App
```bash
streamlit run app.py
```

---

## ⚠️ Limitations

- 🧠 Free-tier LLM (Together API) – slower generation and rate limits may apply  
- 🗂️ No long-term memory or state across sessions  
- 🗣️ Currently text-only (no audio or real-time speech features)  
- 🎯 Debate depth is limited by model size compared to GPT-4-tier models

---

## 🧾 License

This project is licensed under the **MIT License**.

---

## 🙏 Acknowledgements

- [Together AI](https://www.together.ai/) – free API access to open-source LLMs  
- [Meta AI](https://ai.meta.com/) – for LLaMA model development  
- [Streamlit](https://streamlit.io/) – for rapid web app deployment  
- Open-source contributors in the LLM ecosystem

---
