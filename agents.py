import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {TOGETHER_API_KEY}",
    "Content-Type": "application/json"
}

MODEL = "meta-llama/Llama-3-8b-chat-hf"
API_URL = "https://api.together.xyz/v1/chat/completions"

def generate_response(topic, persona, opponent_text, history, mode):
    history_text = "\n\n".join(
        [f"Round {i+1}:\n{h[0]}\n---\n{h[1]}" for i, h in enumerate(history)]
    )

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
    else:
        raise ValueError("Invalid mode.")

    messages = [{"role": "system", "content": prompt}]
    if opponent_text:
        messages.append({"role": "user", "content": f"Opponent said:\n{opponent_text}\nRespond accordingly."})

    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 512
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content'].strip()


def get_judge_verdict(topic, transcript, judge_persona="A fair and objective debate judge"):
    debate_summary = "\n\n".join(
        [f"Round {i+1}:\nPersona 1: {p1}\n---\nPersona 2: {p2}" for i, (p1, p2) in enumerate(transcript)]
    )
    prompt = (
        f"You are {judge_persona}. The debate topic is: '{topic}'.\n"
        "Based on the transcript below, decide who made the more convincing arguments overall.\n"
        "Explain your verdict and provide brief feedback.\n\n"
        f"{debate_summary}"
    )

    messages = [{"role": "system", "content": prompt}]
    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.5,
        "max_tokens": 512
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()
