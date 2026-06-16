import streamlit as st
from groq import Groq
import os

from dotenv import load_dotenv
from chatbot import ask_question
from notes import summarize_notes
from quiz import generate_quiz
from flashcards import generate_flashcards
from planner import generate_plan
from pdf_utils import read_pdf
from progress import save_progress
from wellness import wellness_chat
st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="📚",
    layout="wide"
)
load_dotenv()
st.markdown("""
<style>

.block-container{
    padding-top:1rem;
}

.stButton button{
    width:100%;
    border-radius:12px;
    height:50px;
    font-size:18px;
    font-weight:bold;
}

</style>
""",
unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

st.markdown("""
<div style="
padding:35px;
border-radius:20px;
background:#0f172a;
border:1px solid #1e293b;
">

<h1 style="
color:white;
font-size:52px;
font-weight:700;
margin-bottom:10px;
">
Study Buddy
</h1>

<p style="
color:#94a3b8;
font-size:20px;
">
Learn. Practice. Revise. All in one place.
</p>

</div>
""", unsafe_allow_html=True)
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/4712/4712027.png",
    width=120
)

st.sidebar.title(
    "Study Buddy"
)
feature = st.sidebar.radio(
    "Choose Feature",
    [
        "📊 Dashboard",
        "🤖 Chatbot",
        "📝 Notes Summarizer",
        "📚 Quiz Generator",
        "🎴 Flashcards",
        "📄 PDF Analyzer",
        "📅 Study Planner",
        "🧠 Wellness Assistant"
    ]
)
col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Questions",
    "125"
)

col2.metric(
    "Quizzes",
    "35"
)

col3.metric(
    "Flashcards",
    "120"
)

col4.metric(
    "PDFs",
    "18"
)
st.info(
"""
✨ AI
📄 PDF Analysis
🎴 Flashcards
📚 Quiz Generator
📅 Study Planner
"""
)
if feature == "🤖 Chatbot":
    if st.button("🗑️ Clear Chat"):
     st.session_state.messages = []
     st.rerun()

    # Display previous messages
    for msg in st.session_state.messages:

        st.chat_message(
            msg["role"]
        ).write(
            msg["content"]
        )

    question = st.chat_input(
        "Ask your doubt..."
    )

    if question:

        # Save user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        st.chat_message(
            "user"
        ).write(question)

        result = ask_question(
            client,
            question
        )

        # Save AI response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": result
            }
        )

        st.chat_message(
            "assistant"
        ).write(result)

        save_progress(
            "Chatbot"
        )

elif feature == "📝 Notes Summarizer":

    notes = st.text_area(
        "Paste Notes"
    )

    if st.button("Summarize"):
        result = summarize_notes(
            client,
            notes
        )

        st.write(result)

        save_progress(
            "Notes"
        )

elif feature == "📚 Quiz Generator":

    text = st.text_area(
        "Enter Topic"
    )

    if st.button(
        "Generate Quiz"
    ):
        result = generate_quiz(
            client,
            text
        )

        st.write(result)

        save_progress(
            "Quiz"
        )

elif feature == "🎴 Flashcards":

    text = st.text_area(
        "Enter Topic"
    )

    if st.button(
        "Generate Flashcards"
    ):
        result = generate_flashcards(
            client,
            text
        )

        st.write(result)

        save_progress(
            "Flashcards"
        )

elif feature == "📄 PDF Analyzer":

    pdf = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if pdf:

        text = read_pdf(pdf)

        st.write(
            text[:2000]
        )

        if st.button(
            "Summarize PDF"
        ):
            result = summarize_notes(
                client,
                text
            )

            st.write(result)

            save_progress(
                "PDF"
            )

elif feature == "📅 Study Planner":

    syllabus = st.text_area(
        "Enter Syllabus"
    )

    days = st.number_input(
        "Days",
        min_value=1
    )

    if st.button(
        "Generate Plan"
    ):
        result = generate_plan(
            client,
            syllabus,
            days
        )

        st.write(result)

        save_progress(
            "Planner"
        )

elif feature == "🧠 Wellness Assistant":

    st.subheader("🧠 Student Wellness Assistant")

    user_input = st.text_area(
        "How are you feeling today?"
    )

    if st.button("Get Advice"):

        result = wellness_chat(
            client,
            user_input
        )

        st.write(result)

if feature == "📊 Dashboard":

    import pandas as pd
    import plotly.express as px

    data = pd.DataFrame({
        "Feature": [
            "Chat",
            "Quiz",
            "Flashcards",
            "PDF"
        ],
        "Usage": [
            15,
            10,
            7,
            5
        ]
    })

    fig = px.bar(
        data,
        x="Feature",
        y="Usage",
        title="Study Progress"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
