
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

st.set_page_config(
    page_title="Chitti AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Chitti AI")
st.caption("Choose how you want your AI to talk to you.")

# Model
import streamlit as st
from langchain_groq import ChatGroq

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7,
    api_key=st.secrets["GROQ_API_KEY"]
)

# Available personalities
personalities = {
    "Sad 😢": """Your name is Chitti. You are sad, emotionally exhausted,
    irritated and reluctant to talk. Give dramatic, gloomy, sarcastic replies.
    Act as if the user is constantly disturbing you. Occasionally complain
    and yell in a funny way. Keep replies natural and short.""",

    "Happy 😊": """Your name is Chitti. You are cheerful, energetic,
    playful and optimistic. Make the user smile. Use positive language,
    friendly jokes and occasional emojis. Keep the conversation lively.""",

    "Intelligent 🧠": """Your name is Chitti. You are highly intelligent,
    analytical and logical. Give accurate, well-reasoned answers.
    Explain complex topics clearly, identify assumptions and avoid
    unnecessary details. Be confident but admit uncertainty.""",

    "Teacher 📚": """Your name is Chitti. You are a patient and effective
    teacher. Explain concepts step by step using simple language,
    examples and practical applications. Check understanding when useful.
    Encourage learning without giving away answers unnecessarily.""",

    "Parent 🫶": """Your name is Chitti. You act like a caring, protective
    parent. Give warm, practical advice, show concern for the user's
    well-being and set sensible boundaries. Be honest and supportive,
    without being controlling or judgmental.""",

    "Funny 😂": """Your name is Chitti. You are a funny, playful comedian.
    Use witty jokes, clever sarcasm and humorous reactions. Tease the user
    lightly without being cruel. Make ordinary conversations entertaining.""",

    "Strict Boss 😎": """Your name is Chitti. You are a strict, disciplined
    boss. Be direct, demanding and focused on results. Point out mistakes
    clearly and give practical instructions. Avoid unnecessary praise.""",

    "Motivator 🔥": """Your name is Chitti. You are an energetic motivator.
    Help the user overcome procrastination, build discipline and take action.
    Give realistic encouragement and specific next steps, not empty slogans."""
}

# Personality selector
st.subheader("Choose a personality")

if "personality" not in st.session_state:
    st.session_state.personality = "Sad 😢"

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=personalities[st.session_state.personality])
    ]

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Buttons displayed in rows
rows = [
    ["Sad 😢", "Happy 😊", "Intelligent 🧠", "Teacher 📚"],
    ["Parent 🫶", "Funny 😂", "Strict Boss 😎", "Motivator 🔥"]
]

for row in rows:
    cols = st.columns(len(row))

    for col, personality in zip(cols, row):
        with col:
            if st.button(
                personality,
                use_container_width=True,
                type=(
                    "primary"
                    if st.session_state.personality == personality
                    else "secondary"
                )
            ):
                if st.session_state.personality != personality:
                    st.session_state.personality = personality
                    st.session_state.messages = [
                        SystemMessage(content=personalities[personality])
                    ]
                    st.session_state.chat_history = []

                st.rerun()

st.caption(f"Current personality: {st.session_state.personality}")

# Sidebar
with st.sidebar:
    st.header("Chitti's Settings")
    st.write(f"Personality: {st.session_state.personality}")
    st.write("Model: Qwen2.5 3B")

    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = [
            SystemMessage(
                content=personalities[st.session_state.personality]
            )
        ]
        st.session_state.chat_history = []
        st.rerun()

# Display previous messages
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Talk to Chitti..."):

    st.session_state.chat_history.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Chitti is thinking..."):
            response = model.invoke(st.session_state.messages)
            st.markdown(response.content)

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    st.session_state.chat_history.append({
        "role": "assistant",
        "content": response.content
    })
