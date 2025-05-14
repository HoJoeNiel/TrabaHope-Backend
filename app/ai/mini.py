from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

sentences = ["I am learning to use the MiniLM transformer for natural language processing tasks.", "I am studying how to apply the MiniLM transformer for NLP tasks."]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(sentences)
a = np.array(embeddings[0])
b = np.array(embeddings[1])

a = a.reshape(1, -1)
b = b.reshape(1, -1)

similarity = cosine_similarity(a, b)
print(similarity)