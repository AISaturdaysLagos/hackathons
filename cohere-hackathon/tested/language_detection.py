# https://docs.cohere.com/docs/language-detection
import cohere
from config import cohere_key
co = cohere.Client(cohere_key)  # This is your trial API key

# English, Spanish, Japanese, Afrikaans <-> (Dutch ?)
response = co.detect_language(
    texts=["Good morning", "Buen día", "おはよう", "Goeie more", "Goedemorgen"])

# print(dir(response))
print(response.results)

