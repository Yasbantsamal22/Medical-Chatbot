from flask import Flask, render_template, jsonify, request
from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)


load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

embeddings = download_hugging_face_embeddings()

index_name = "medibot"

docsearch = PineconeVectorStore.from_existing_index(
    index_name = index_name,
    embedding=embeddings
)

# This line of code give me three relevant answer

retriver = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})
# Initialize the LLM
llm = GoogleGenerativeAI(model="gemini-pro", temperature=0.4, max_output_tokens=500)
# Define the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

# Step 4: Create the Question-Answering Chain
question_answer_chain = create_stuff_documents_chain(llm, prompt)
# Step 5: Create the Retrieval-Augmented Generation (RAG) Chain
rag_chain = create_retrieval_chain(retriver, question_answer_chain)

# First route is the default route
# User will get interface of my application
@app.route("/")
def index():
    return render_template('chat.html')

# 2nd route is my chat operation
@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form['msg']
    input = msg
    print(input)
    response = rag_chain.invoke({"input":msg})
    print("Response : ", response["answer"])
    return str(response["answer"])



if __name__=='__main__':
    app.run()
    
