# Flask Chatbot with LangChain and FAISS

This project is a Flask-based chatbot that retrieves relevant technical courses from Brainlox using LangChain for document loading, Hugging Face embeddings for text representation, and FAISS for vector search.

## Features
- Scrapes technical course data from Brainlox.
- Uses `HuggingFaceEmbeddings` for embedding generation.
- Stores and searches vectorized documents using FAISS.
- Provides relevant course recommendations based on user queries.

## Installation
### Prerequisites
Ensure you have Python installed along with the required dependencies.

### Clone the Repository
```sh
git clone https://github.com/your-repo/flask-chatbot-faiss.git
cd flask-chatbot-faiss
```

### Install Dependencies
```sh
pip install flask langchain langchain_community faiss-cpu sentence-transformers
```

## Usage
### Run the Flask Application
```sh
python app.py
```

The API will start at `http://127.0.0.1:5000/`.

### API Endpoint
#### `/chat` (POST)
- **Description**: Accepts user input and returns relevant course recommendations.
- **Request Format**:
  ```json
  {
      "message": "Python programming"
  }
  ```
- **Response Format**:
  ```json
  {
      "response": [
          {
              "course": "Python for Beginners",
              "description": "Learn Python from scratch."
          },
          {
              "course": "Advanced Python",
              "description": "Deep dive into Python concepts."
          }
      ]
  }
  ```

## How It Works
1. The `WebBaseLoader` scrapes course data from Brainlox.
2. `HuggingFaceEmbeddings` converts text data into embeddings.
3. FAISS stores these embeddings and enables similarity search.
4. The chatbot searches for the most relevant courses based on user input.
5. Results are formatted and returned as a JSON response.

## Customization
- Modify the `WebBaseLoader` URL to fetch data from a different website.
- Adjust the embedding model in `HuggingFaceEmbeddings`.
- Change `k=3` in `similarity_search` to adjust the number of recommendations.

## License
This project is licensed under the MIT License.

