import openai
import json
import numpy as np
from helpers import calculate_cosine_similarity
import inflect

# Set up OpenAI API credentials
openai.api_key = 'API-KEY-PLACEHOLDER'

embeddings = {}

p = inflect.engine()

def generate_embedding(user):
    # Extract user information for embedding
    age = user['age']
    state = user['state']
    interests = user['interests']
    activities = user['activities']

    # Convert numerical age to words
    age_word = p.number_to_words(age)

    # Concatenate user information into a single string
    user_data = f"Age: {age_word}, \n State: {state}, \n Interests: {', '.join(interests)} Activities: {', '.join(activities)}"

    # Send formated user data to OpenAI's API to generate embeddings
    return openai.Embedding.create(input=[user_data], model='text-embedding-ada-002')['data'][0]['embedding']
  
# Generate embeddings for candidate IDs
def generate_embeddings(users, candidate_ids):
    for user in users:
        user_id = user['id']
        if user_id in candidate_ids and user_id not in embeddings:
            embedding = generate_embedding(user)
            embeddings[user_id] = embedding

# Get the embedding for a specific user ID from the embeddings dictionary
def get_embedding(user_id):
    return embeddings.get(user_id)