import streamlit as st
import time
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
import pickle
with open('company_data.pickle', 'rb') as f:
    company_data = pickle.load(f)
api_key = "AIzaSyAe9h1Xl8aFGZcEAjF-g6diBi0-1zxpBU4"
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=api_key, temperature=0, max_output_tokens=1000)

chain = load_qa_chain(llm, chain_type="stuff")
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
def get_similar_company(company):
    match = db.similarity_search(company, k=20)
    answers_doc = []
    answers = []
    for i in match:
        if i.page_content not in answers:
            doc=Document(page_content=i.page_content,metadata={"source": "local"})
            answers_doc.append(doc)
            answers.append(i.page_content)
    response = chain.run(input_documents = answers_doc, question = f"Retrieve all names sounding similar or written similarly or is same to {company} from the documents.")
    return response

# Page title and background setup
st.set_page_config(page_title="Legal Trademark Infringement App", page_icon=":robot:", 
                   layout="wide", initial_sidebar_state="collapsed")

# Dark navy blue background
st.markdown(
    """
    <style>
    body {
        background-color: #000000;
        color: white;
        font-family: Arial, sans-serif;
    }
    .orange-box {
        background-color: #FFA500;
        color: black;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        width: 60%;
        word-wrap: break-word;
    }
    .user-message {
        text-align: right;
        margin-bottom: 15px;
    }
    .streamlit-message {
        text-align: left;
        margin-bottom: 15px;
    }
    .message-container {
        display: flex;
        justify-content: flex-end;
    }
    .message-bubble {
        max-width: 80%;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 5px;
    }
    .user-bubble {
        background-color: #000435;
        color: white;
        align-self: flex-end;
    }
    .streamlit-bubble {
        background-color: #FFA500;
        color: white;
        align-self: flex-start;
    }
    .message-time {
        font-size: 0.8em;
        text-align: right;
        color: #707B7C;
    }
    @keyframes glow {
        0% { text-shadow: 0 0 5px #fff; }
        50% { text-shadow: 0 0 20px #FFA500; }
        100% { text-shadow: 0 0 5px #fff; }
    }
    .glow {
        animation: glow 1s infinite;
        color: #FFA500;
    }
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: left;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header and sidebar
st.title("Legal Trademark Infringement App")
st.sidebar.title("Settings")

# Input text box
input_text = st.text_input("Enter the company name:")

# Function to display user message
def display_user_message(text):
    st.markdown(
        f"""
        <div class="message-container">
            <div class="message-bubble user-bubble">
                {text}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Function to display Streamlit message
def display_streamlit_message(text):
    companies = get_similar_company(text)
    try:
        for i in companies.split(", "):
            answer = [data for data in company_data if i.lower() in data.lower()]
            texts = f"Company: {i}\n{answer[0]}"
            texts = texts.replace('\n', '<br>')
            html_content = f"""
                <div class="message-container">
                    <div class="message-bubble streamlit-bubble">
                        {texts}
                    </div>
                </div>"""
            st.markdown(html_content, unsafe_allow_html=True)
        
    except:
        html_content = f"""
                <div class="message-container">
                    <div class="message-bubble streamlit-bubble">
                        No other companies found
                    </div>
                </div>"""
        st.markdown(html_content, unsafe_allow_html=True)


# Function to simulate processing with spinner
def simulate_processing(text):
    with st.spinner("Processing..."):
        time.sleep(2)  # Simulate a delay
        display_streamlit_message(text)

# Button to submit text
if st.button("Search"):
    display_user_message(input_text)
    simulate_processing(input_text)

# History section
st.sidebar.subheader("Chat History")

# Save history using a list (can be improved with a database for persistence)
if 'history' not in st.session_state:
    st.session_state.history = []

if input_text:
    st.session_state.history.append({'input': input_text, 'timestamp': time.time()})

# Display chat history
for entry in st.session_state.history:
    if 'input' in entry:
        st.sidebar.markdown(
            f"""
            <div class="message-container">
                <div class="message-bubble user-bubble">
                    {entry['input']}
                </div>
                <div class="message-time">{time.ctime(entry['timestamp'])}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    if 'output' in entry:
        st.sidebar.markdown(
            f"""
            <div class="message-container">
                <div class="message-bubble streamlit-bubble">
                    {entry['output']}
                </div>
                <div class="message-time">{time.ctime(entry['timestamp'])}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# Animated text
st.markdown('<div class="glow footer">Welcome to Legal Trademark Infringement App!</div>', unsafe_allow_html=True)
