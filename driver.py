import json
from cna import CommonNeighborsRecommendations
import embeddings
import helpers

users_file_path = 'users.json'

# Create instance of CommonNeighborsRecommendations classe
cna = CommonNeighborsRecommendations(users_file_path)

# Set the target user's ID, the number of candidate recommendations, and the number of final recommendations
target_user_id = 1
num_candidates = 50
num_recommendations = 15

# Get Common Neighbors recommendations
cna_recommendations = cna.find_common_neighbors_recommendations(target_user_id, num_candidates,10)

# Open and load the users data file
with open(users_file_path, 'r') as users_file:
    users_data = json.load(users_file)
    users = users_data['users']

# Create a list of candidate IDs for embedding generation
candidate_ids = [candidate['id'] for candidate in cna_recommendations]
candidate_ids.append(target_user_id)

# Generate embeddings for the candidates and target user
embeddings.generate_embeddings(users, candidate_ids)
target_user_embedding = embeddings.get_embedding(target_user_id)

# Filter candidates based on similarity
filtered_candidates = helpers.filter_users_by_similarity(cna_recommendations, target_user_embedding, num_recommendations, embeddings.embeddings)

# Print the final recommendations
print("\nProposed Model Recommendations:")
for index, candidate in enumerate(filtered_candidates, start=1):
    similarity_score = helpers.calculate_similarity_score(candidate, target_user_embedding, embeddings.embeddings)
    similarity_score_rounded = round(similarity_score, 3)
    print(f"{index}. User ID: {candidate['id']} (Similarity Score: {similarity_score_rounded}), {candidate['age']},  {candidate['state']}")