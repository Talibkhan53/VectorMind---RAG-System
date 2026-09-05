import numpy as np
from Search.similarity import CosineSimilarity

class VectorStore:
    def __init__(self):
        self.chunks = []
        self.embeddings = []

    def add(self,chunk,embedding):
        self.chunks.append(chunk)
        self.embeddings.append(embedding)


    def matrix(self):
        embedding_matrix = np.array(self.embeddings) 
        return embedding_matrix

    def search(self, query_embed, top_k=3):
        relevant = {}
        c = CosineSimilarity()

        # Calculate similarity for every embedding
        for i, embedding in enumerate(self.embeddings):
            score = c.cosine_similarity(query_embed, embedding)
            relevant[i] = score

        # Sort by similarity score, highest first
        sorted_results = sorted(
            relevant.items(),
            key=lambda x: x[1],
            reverse=True)

        # Take only the top K results
        top_results = sorted_results[:top_k]

        results = []

        for index , score in top_results:
            results.append((self.chunks[index], score))
        # print(results)
        return results
