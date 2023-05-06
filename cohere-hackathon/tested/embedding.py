import cohere
import numpy as np
from config import cohere_key
co = cohere.Client(cohere_key)  # This is your trial API key

response = co.embed(
    model='large',
    texts=[" \"I like Football\"", "I like computer science and AI ", "I studied political science "])
# print('Embeddings: {}'.format(response.embeddings))
np_embedding = np.array(response.embeddings)
print(np_embedding.shape)
# np.save("co_embedding",np_embedding)
