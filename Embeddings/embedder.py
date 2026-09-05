from sentence_transformers import SentenceTransformer
import numpy as np

class embeddingModel:
    def __init__(self,model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_chunks(self,text:list[str]):
        return self.model.encode(text)

    def embed_question(self,text:str):
        return self.model.encode(text)
