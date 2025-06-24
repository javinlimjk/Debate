import streamlit as st
from agents import generate_response, get_judge_verdict

# Setup
st.set_page_config(page_title="Persona Debate Agent", page_icon="🧠", layout="wide")
st.title("🧠 Persona-Powered Debate Agent")

# Debate schedule
TURNS = [
    ("persona_1", "constructive"),
    ("persona_2", "constructive"),
    ("persona_1", "rebuttal"),
    ("persona_2", "rebuttal"),
    ("persona_1", "closing"),
    ("persona_2", "closing")
]

# State Init
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.transcript = []
    st.session_state.topic = ""
    st.session_state.persona_1 = ""
    st.session_state.persona_2 = ""
    st.session_state.bubbles = []
    st.session_state.mode = ""
    st.session_state.partial_turn = ""

# Form
if st.session_state.topic == "":
    with st.form("setup"):
        topic = st.text_input("Debate Topic")
        persona_1 = st.text_input("Persona 1 (e.g. You)")
        persona_2 = st.text_input("Persona 2 (e.g. AI Opponent)")
        mode = st.selectbox("Debate Mode", ["AI vs AI", "User vs AI"])
        submitted = st.form_submit_button("Start Debate")
    if submitted and topic and persona_1 and persona_2:
        st.session_state.topic = topic
        st.session_state.persona_1 = persona_1
        st.session_state.persona_2 = persona_2
        st.session_state.mode = mode
        st.rerun()

# End of Debate
elif st.session_state.step >= len(TURNS):
    st.markdown("### 🧾 Final Transcript")
    for i, (p1, p2) in enumerate(st.session_state.transcript):
        st.markdown(f"**Round {i+1}:**")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"<div class='bubble-left'><b>{st.session_state.persona_1}</b><br>{p1}</div>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<div class='bubble-right'><b>{st.session_state.persona_2}</b><br>{p2}</div>", unsafe_allow_html=True)

    with st.spinner("Evaluating debate..."):
        judge_feedback = get_judge_verdict(st.session_state.topic, st.session_state.transcript)
    st.success("🧑‍⚖️ Judge's Verdict")
    st.markdown(judge_feedback)

    if st.button("🔁 Restart"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# Main Debate Flow
else:
    speaker_key, phase_mode = TURNS[st.session_state.step]
    speaker_name = st.session_state.persona_1 if speaker_key == "persona_1" else st.session_state.persona_2
    opponent_key = "persona_2" if speaker_key == "persona_1" else "persona_1"
    opponent_name = st.session_state.persona_2 if speaker_key == "persona_1" else st.session_state.persona_1

    st.subheader(f"🧭 Phase: {phase_mode.title()} — {speaker_name}'s Turn")
    st.markdown(f"**Debate Topic:** *{st.session_state.topic}*")

    # Display bubbles
    st.markdown("---")
    for bubble in st.session_state.bubbles:
        align = "bubble-left" if bubble["side"] == "left" else "bubble-right"
        st.markdown(f"<div class='{align}'><b>{bubble['persona']}</b><br>{bubble['text']}</div>", unsafe_allow_html=True)

    # User vs AI
    if st.session_state.mode == "User vs AI" and speaker_key == "persona_1":
        user_input = st.text_area("✍️ Your Turn:", key=f"user_input_{st.session_state.step}", height=150)
        st.markdown("<div class='bottom-button'>", unsafe_allow_html=True)
        if st.button("➡️ Submit", key="user_submit"):
            st.session_state.bubbles.append({
                "persona": speaker_name,
                "text": user_input,
                "side": "left"
            })
            st.session_state.partial_turn = user_input
            st.session_state.step += 1
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # AI speaking
    else:
        st.markdown("<div class='bottom-button'>", unsafe_allow_html=True)
        if st.button("➡️ Next", key="ai_next"):
            with st.spinner("Generating response..."):
                opponent_text = ""
                if st.session_state.transcript:
                    last_turn = st.session_state.transcript[-1]
                    opponent_text = last_turn[1] if speaker_key == "persona_1" else last_turn[0]

                response = generate_response(
                    st.session_state.topic,
                    speaker_name,
                    opponent_text,
                    st.session_state.transcript,
                    phase_mode
                )

                st.session_state.bubbles.append({
                    "persona": speaker_name,
                    "text": response,
                    "side": "left" if speaker_key == "persona_1" else "right"
                })

                if speaker_key == "persona_1":
                    st.session_state.partial_turn = response
                else:
                    st.session_state.transcript.append((st.session_state.partial_turn, response))

                st.session_state.step += 1
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# CSS: Professional, contrasting + fixed bottom button
st.markdown("""
<style>
/* Speech bubbles */
.bubble-left, .bubble-right {
    padding: 1.4em;
    margin: 1em 0;
    border-radius: 16px;
    font-size: 1.05em;
    line-height: 1.6;
    width: 95%;
}
.bubble-left {
    background-color: #e3f2fd;
    color: #0d47a1;
    border: 2px solid #64b5f6;
}
.bubble-right {
    background-color: #fce4ec;
    color: #880e4f;
    border: 2px solid #f06292;
    margin-left: auto;
}

/* Fixed bottom button */
.bottom-button {
    position: fixed;
    bottom: 1.5em;
    left: 1.5em;
    z-index: 9999;
    background-color: white;
    padding: 0.5em 1em;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)
