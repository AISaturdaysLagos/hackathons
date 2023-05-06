import cohere
from cohere.responses.classify import Example
from config import cohere_key
co = cohere.Client(cohere_key) # This is your trial API key

"""
Sentiment analysis is a type of classification task that analyzes the tone of a piece of text. 
It is used in a variety of different ways, or example, on social media comments and customer reviews. 
It is commonly used to see how people feel about their products or company, but it can also be used to 
help businesses understand how different trends in the economy may impact their business.
Here we look at an example of analyzing the sentiments of customer feedback about a product into Positive, Negative, or Neutral.
"""

examples=[
  Example("The order came 5 days early", "positive"), 
  Example("The item exceeded my expectations", "positive"), 
  Example("I ordered more for my friends", "positive"), 
  Example("I would buy this again", "positive"), 
  Example("I would recommend this to others", "positive"), 
  Example("The package was damaged", "negative"), 
  Example("The order is 5 days late", "negative"), 
  Example("The order was incorrect", "negative"), 
  Example("I want to return my item", "negative"), 
  Example("The item\'s material feels low quality", "negative"), 
  Example("The product was okay", "neutral"), 
  Example("I received five items in total", "neutral"), 
  Example("I bought it from the website", "neutral"), 
  Example("I used the product this morning", "neutral"), 
  Example("The product arrived yesterday", "neutral"),
]

inputs=[
  "This item was broken when it arrived",
  "The product is amazing",
  "The product was not too bad",
]

# Default model size is large, you can switch to small. 
response = co.classify(
  inputs=inputs,
  examples=examples,
)
print(response)