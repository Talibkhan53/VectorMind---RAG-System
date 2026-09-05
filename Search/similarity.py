import numpy as np 

class CosineSimilarity:
    def cosine_similarity(self,chunk,query):
        product = np.dot(chunk,query)
        distance_from_origin_a = np.linalg.norm(chunk)
        distance_from_origin_b = np.linalg.norm(query)
        distance_from_origin = distance_from_origin_a * distance_from_origin_b
        angle = product / distance_from_origin
        return angle
        

c = CosineSimilarity()
c.cosine_similarity(50,-50)