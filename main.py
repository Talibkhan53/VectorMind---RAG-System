from pathlib import Path

from Loaders.main_loader import MainLoader
from Chunking.chunking import Chunking
from Embeddings.embedder import embeddingModel
from Storage.vector_store import VectorStore
from Retreiver.retreiver import Retreiver
from ContextBuilder.context_builder import ContextBuilder
from Prompt.prompt import PromptBuilder
from LLm.llm import OllamaClient


# 1. Get document path

file_directory = input("\nEnter directory path: ").strip()
file_name = input("Enter file name: ").strip()

file_path = Path(file_directory) / file_name

# 2. Validate and load document

if not file_path.is_file():
    print("Error: File not found in that directory. Try again.")
    exit()


str_loader = MainLoader.choose_loader(file_path)

if not str_loader.validate_file(file_path):
    print("Error: Invalid or unsupported file.")
    exit()


str_content = str_loader.read_file(file_path)



# 3. Chunk document
chunker = Chunking()

chunks = chunker.sliding_chunk(str_content)

print(f"\nDocument loaded.")
print(f"Chunks created: {len(chunks)}")


# 4. Create embeddings

embedder = embeddingModel()

embeddings = embedder.embed_chunks(chunks)

print("Embeddings created.")

# 5. Store chunks + embeddings
vector_store = VectorStore()

for chunk, embedding in zip(chunks, embeddings):
    vector_store.add(chunk, embedding)

print("Vector store ready.")



# 6. Create Retriever
retriever = Retreiver(
    embedder,
    vector_store
)

# 7. Ask question
query = input("\nEnter Your Question: ").strip()



# 8. Retrieve relevant chunks
results = retriever.retreive(query)

# 9. Build context
context_builder = ContextBuilder()
context = context_builder.build(results)


# 10. Build prompt
prompt_builder = PromptBuilder()

prompt = prompt_builder.build(
    query,
    context
)


# 11. Send to Ollama

ollama = OllamaClient()
answer = ollama.generate(prompt)



# 12. Display answer
print("\n-----------------------------")
print("Answer:")
print(answer)
print("-----------------------------")