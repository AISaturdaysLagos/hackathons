import cohere
from config import cohere_key
co = cohere.Client(cohere_key) # This is your trial API key

# Temperature is a configuration hyperparameter that controls the randomness of language
# model output. A high temperature produces more unpredictable and creative results, 
# while a low temperature produces more common and conservative output. 
# https://txt.cohere.com/llm-parameters-best-outputs-language-ai/

response = co.generate(
  model='command-xlarge-nightly',
  prompt='Write a body paragraph about \"My promotion to the head of HR in my company\" in a blog post titled \"My 2023 promotion\"',
  max_tokens=300,
  temperature=0.9,
  k=0,
  stop_sequences=[],
  return_likelihoods='NONE')
print('Prediction: {}'.format(response.generations[0].text))

# response = co.generate(
#   model='command-xlarge-nightly',
#   prompt='Write a body paragraph about \"My promotion to the head of Machine Learning in Cohere\" in a blog post titled \"My 2024 promotion\"',
#   max_tokens=300,
#   temperature=0.9,
#   k=0,
#   stop_sequences=[],
#   return_likelihoods='NONE')

print('Prediction: {}'.format(response.generations[0].text))