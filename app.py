import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# ----------------------------
# Gemini API
# ----------------------------
API_KEY = "AQ.Ab8RN6K0fQpnJZ1CiZR9qIIk6ccAJ37E2JXfRIu2c-hYHrX1xw"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# ----------------------------
# Streamlit
# ----------------------------
st.set_page_config(
    page_title="Citizen AI Assistant",
    page_icon="🏛",
    layout="wide"
)

st.title("🏛 Citizen AI Assistant")

# ----------------------------
# Language Selection
# ----------------------------

language = st.selectbox(
    "🌐 Select Language",
    [
        "English",
        "తెలుగు",
        "हिन्दी",
        "தமிழ்",
        "ಕನ್ನಡ",
        "മലയാളം",
        "বাংলা",
        "मराठी"
    ]
)

st.write(f"Current Language: **{language}**")

# ----------------------------
# Session State
# ----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""

# ----------------------------
# Sidebar
# ----------------------------

with st.sidebar:

    st.header("📄 Upload PDF")

    pdf = st.file_uploader("Choose PDF", type="pdf")

    if pdf:

        reader = PdfReader(pdf)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

        st.session_state.pdf_text = text

        st.success("PDF Uploaded Successfully!")

# ----------------------------
# Display Chat
# ----------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------
# Chat Input
# ----------------------------

prompt = st.chat_input("Ask anything...")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Prompt Construction
    if st.session_state.pdf_text:

        final_prompt = f"""
Reply ONLY in {language}.

The user uploaded this document.

Document:

{st.session_state.pdf_text[:12000]}

Question:

{prompt}

If the answer exists in the document,
answer using the document.

Otherwise answer normally using your own knowledge.
"""

    else:

        final_prompt = f"""
Reply ONLY in {language}.

User Question:

{prompt}
"""

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = model.generate_content(final_prompt)

            answer = response.text

            st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )