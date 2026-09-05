from Embeddings.embedder import embeddingModel
from Storage.vector_store import VectorStore

class Retreiver : 
    def __init__(self, embedder, vector_store):
        self.embedder = embedder
        self.vector_store = vector_store


    def retreive(self,query):
        query_embed = self.embedder.embed_question(query)
        results = self.vector_store.search(query_embed,top_k=3)
        return results
    


        
        
        
    
