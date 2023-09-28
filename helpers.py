import numpy as np

# Calculate cosine similarity of two embeddings
def calculate_cosine_similarity(embedding1, embedding2):
    dot_product = np.dot(embedding1, embedding2)
    norm1 = np.linalg.norm(embedding1)
    norm2 = np.linalg.norm(embedding2)
    similarity = dot_product / (norm1 * norm2)
    return similarity

# Calculate similarity score between a user and the target user based on their embeddings
def calculate_similarity_score(user, target_user_embedding, users_embeddings):
    user_embedding = users_embeddings.get(user['id'])
    similarity_score = calculate_cosine_similarity(user_embedding, target_user_embedding)
    return similarity_score

# Finding the most similar users to a target user
def filter_users_by_similarity(users, target_user_embedding, num_users, users_embeddings):
    similarity_scores = []
    
    # Calculate the similarity score between each user and the target user
    for user in users:
        similarity_score = calculate_similarity_score(user, target_user_embedding, users_embeddings)
        similarity_scores.append((user, similarity_score))

    # Sort the users based on their similarity scores in descending order
    similarity_scores.sort(key=lambda x: x[1], reverse=True)

    # Return the top `num_users` users with the highest similarity scores
    filtered_users = [user for user, _ in similarity_scores[:num_users]]
    return filtered_users
