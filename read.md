# VectorMind

VectorMind is a local Retrieval-Augmented Generation (RAG) system that allows users to ask questions about documents.

Instead of sending the entire document to the LLM, VectorMind retrieves the most relevant chunks and provides them as context to the LLM.

## Architecture

Document
   ↓
Loader
   ↓
Chunking
   ↓
Embeddings
   ↓
Vector Store
   ↓
Retriever + Top-K Search
   ↓
Context Builder
   ↓
Prompt Builder
   ↓
Ollama
   ↓
Answer

## Features

- Supports document loading and validation
- Splits documents into smaller chunks
- Generates embeddings using Sentence Transformers
- Stores document chunks and embeddings
- Uses Cosine Similarity for semantic search
- Retrieves Top-K relevant chunks
- Builds context for the LLM
- Uses Ollama for local LLM inference

## Technologies

- Python
- NumPy
- Sentence Transformers
- Ollama
- Requests

## Main Concepts

- RAG
- Text Chunking
- Embeddings
- Cosine Similarity
- Vector Search
- Top-K Retrieval
- Prompt Engineering
- Object-Oriented Programming
- Modular Architecture
- Dependency Injection

## How It Works

1. The user provides a document.
2. The document is loaded and divided into chunks.
3. Each chunk is converted into an embedding.
4. The embeddings are stored in the Vector Store.
5. The user's question is converted into an embedding.
6. Cosine Similarity is used to compare the question with document chunks.
7. The Top-K most relevant chunks are retrieved.
8. The retrieved chunks are added to the prompt.
9. Ollama generates the final answer using the retrieved context.