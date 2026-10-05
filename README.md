# VectorMind

VectorMind is a simple local semantic search and question-answering system built with Python.

It allows you to provide a `.txt` or `.csv` document, convert its content into vector embeddings, find the most relevant parts of the document for a question, and generate an answer using a local LLM through Ollama.

The project is built to understand the basic workflow behind semantic search and Retrieval-Augmented Generation (RAG).

## Features

- Supports `.txt` and `.csv` files
- Validates files before processing
- Detects empty files
- Splits documents into overlapping chunks
- Generates embeddings using Sentence Transformers
- Stores chunks and their embeddings in an in-memory vector store
- Uses cosine similarity to find relevant chunks
- Retrieves the top 3 relevant chunks
- Builds context from retrieved chunks
- Uses a prompt builder to control the LLM response
- Uses Ollama for local LLM generation
- Runs completely locally

## How It Works

VectorMind follows this basic pipeline:

```text
Document
   ↓
File Loader
   ↓
Text Extraction
   ↓
Chunking
   ↓
Embeddings
   ↓
Vector Store
   ↓
User Question
   ↓
Question Embedding
   ↓
Cosine Similarity
   ↓
Top Relevant Chunks
   ↓
Context Builder
   ↓
Prompt Builder
   ↓
Ollama
   ↓
Answer
```

## Project Structure

```text
VectorMind/
│
├── Chunking/
│   └── chunking.py
│
├── ContextBuilder/
│   └── context_builder.py
│
├── Embeddings/
│   └── embedder.py
│
├── LLm/
│   └── llm.py
│
├── Loaders/
│   ├── base_loader.py
│   ├── document_loaders.py
│   └── main_loader.py
│
├── Prompt/
│   └── prompt.py
│
├── Retreiver/
│   └── retreiver.py
│
├── Search/
│   └── similarity.py
│
├── Storage/
│   └── vector_store.py
│
├── exceptions.py
└── main.py
```

## Technologies Used

- Python
- NumPy
- Sentence Transformers
- Ollama
- Requests
- CSV module

## Embedding Model

VectorMind currently uses:

```text
all-MiniLM-L6-v2
```

This model converts document chunks and user questions into numerical vectors.

These vectors allow VectorMind to compare the meaning of the question with the meaning of document chunks rather than simply matching keywords.

## Similarity Search

VectorMind uses cosine similarity to compare the question embedding with document embeddings.

A higher cosine similarity score means that the document chunk is more semantically related to the question.

The system currently retrieves the top 3 most relevant chunks.

## Supported Files

Currently supported:

```text
.txt
.csv
```

Other file types will raise an `UnsupportedFileTypeError`.

Empty files are rejected using `EmptyFileError`.

## Requirements

Install the required Python packages:

```bash
pip install numpy sentence-transformers requests
```

You also need to install and run Ollama.

VectorMind currently uses:

```text
phi3:mini
```

You can download the model with:

```bash
ollama pull phi3:mini
```

Make sure Ollama is running before asking questions.

## Running the Project

Clone the repository:

```bash
git clone <your-repository-url>
```

Go into the project directory:

```bash
cd VectorMind
```

Run:

```bash
python main.py
```

The program will ask for:

```text
Enter directory path:
Enter file name:
```

After loading the document, it will create embeddings and ask:

```text
Enter Your Question:
```

VectorMind will then retrieve the most relevant parts of the document and send them to Ollama to generate the answer.

## Example

Suppose the document contains:

```text
Python is a programming language.
It is widely used in data science and artificial intelligence.
```

You can ask:

```text
What is Python used for?
```

VectorMind will:

1. Load the document
2. Split it into chunks
3. Create embeddings
4. Create an embedding for the question
5. Compare the question with document chunks
6. Select the most relevant chunks
7. Build the context
8. Send the context and question to Ollama
9. Generate the final answer

## Current Limitations

VectorMind is currently a learning-focused project and has some limitations:

- Embeddings are stored only in memory
- Documents are processed again when the program starts
- Only TXT and CSV files are supported
- Only the top 3 chunks are retrieved
- No persistent vector database is currently used
- Ollama is required for local answer generation
- Chunking is currently based on word count
- There is no graphical interface

## Future Improvements

Possible improvements include:

- Persistent vector storage
- Better document change detection
- Improved chunking strategies
- Configurable `top_k` retrieval
- Similarity score filtering
- Support for more file formats
- Better error handling
- Command-line options
- Search result display with similarity scores
- Improved prompt configuration
- More efficient embedding generation

## Purpose of the Project

The main purpose of VectorMind is to understand how semantic search and RAG systems work internally instead of relying completely on high-level frameworks.

The project separates the major components of the pipeline so that each stage can be understood and improved independently.

## Learning Outcomes

Through this project, the following concepts are practiced:

- Object-Oriented Programming
- File handling
- Abstract classes
- Factory pattern
- Text processing
- Chunking
- Vector embeddings
- NumPy arrays
- Cosine similarity
- Semantic search
- Information retrieval
- Context building
- Prompt construction
- Local LLM integration
- Basic RAG architecture

## Author

**Talib**

This project is continuously being improved to better understand practical AI and semantic-search systems.
