from flask import Flask, request, jsonify
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

app = Flask(__name__)

# Initialize embeddings
embeddings = HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2'
)

# Load and process documents
loader = WebBaseLoader("https://brainlox.com/courses/category/technical")
documents = loader.load()

# Create and save FAISS vector store
vector_store_path = "vector_store"
vectorstore = FAISS.from_documents(documents, embeddings)
vectorstore.save_local(vector_store_path)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    
    # Get similar documents
    results = vectorstore.similarity_search(user_input, k=3)
    
    # Format response with course title and description
    response = {
        "response": [{
            "course": result.page_content.split("\n")[0].strip(),
            "description": result.page_content.split("\n")[1].strip()
        } for result in results]
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
