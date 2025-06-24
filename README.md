# 🧠 Persona-Powered Debate Agent

A web-based debate simulation tool that uses LLM agents to generate persuasive, persona-driven arguments across structured debate rounds.

---

## 📌 Overview

This project allows users to simulate formal debates between two personas—either **AI vs AI** or **User vs AI**—on a selected topic. Built using **Streamlit** and powered by **LLMs (Large Language Models)**, it provides structured argumentation phases: **Constructive**, **Rebuttal**, and **Closing Statements**.

Speech bubbles simulate live dialogue and emphasize clarity, contrast, and professionalism in visual design. At the end, an **AI Judge** evaluates both sides and provides a verdict.

---

## 🎯 Features

- ✍️ **User vs AI** or 🤖 **AI vs AI** modes  
- 💬 Realistic debate structure with 3 rounds and 6 turns  
- 🧠 Customizable personas  
- 💡 Rebuttals with new arguments, not just repetition  
- ✅ Fixed-position Next/Submit button for intuitive navigation  
- 🎨 Professional UI with contrasting speech bubbles  
- 👨‍⚖️ Final summary and AI-generated verdict  

---

## 🛠️ How It Works

### 🔁 Debate Flow

| Phase        | Persona 1       | Persona 2       |
|--------------|-----------------|-----------------|
| Constructive | Argues for      | Argues against  |
| Rebuttal     | Rebuts and adds | Rebuts and adds |
| Closing      | Summarizes case | Summarizes case |

Each turn generates speech using a language model conditioned on:
- The **debate topic**
- The **persona’s perspective**
- The **history of prior turns**

### ⚙️ LLM-Powered Agents

The app uses an LLM (e.g. `meta-llama/Llama-3-8b-chat-hf`) via the [Together.ai API](https://www.together.ai/) to simulate debate agents. Each agent is prompt-engineered with:
- A role/persona
- The debate phase (e.g. constructive, rebuttal)
- Optional access to opponent's prior speech

### 👨‍⚖️ Judging the Debate

After all 6 turns, the transcript is passed to the judge agent, which:
- Evaluates argument strength, clarity, and persuasiveness
- Determines the winner
- Gives constructive feedback

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/debate-agent.git
cd debate-agent
```

### 2. Set Up Environment Variables

Create a `.env` file in the root directory:

```bash
TOGETHER_API_KEY=your-api-key-here
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
