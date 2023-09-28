import json

class CommonNeighborsRecommendations:
 
    # Initialize the class with the path to the users data file    
    def __init__(self, users_file_path):
        self.users_file_path = users_file_path


    def find_common_neighbors_recommendations(self, target_user_id, num_recommendations, threshold=1):
        
        # Open and read the JSON file containing user data
        with open(self.users_file_path, 'r') as users_file:
            users_data = json.load(users_file)
            users = users_data['users']
        
        # Find the target user's data
        target_user_data = next((user for user in users if user['id'] == target_user_id), None)

        if not target_user_data:
            return []

        # Find all friends of the target user and store their ids
        target_user_friends = set([int(fid.strip()) for fid in target_user_data['friends'].split(',')])
        recommendations_found = 0
        common_neighbors_recommendations = []

        # Find common neighbors
        for user in users:
            user_id = user['id']
            if user_id == target_user_id:
                continue
            
            # Store the current user's friend ids as a set
            user_friends = set([int(fid.strip()) for fid in user['friends'].split(',')])
            
            # Find the common friendsbetween the target user and the current user
            common_neighbors = target_user_friends.intersection(user_friends)

            # Add current user to recommendation list if they meet the threshold
            if len(common_neighbors) >= threshold:
                common_neighbors_recommendations.append(user)
                recommendations_found += 1

            if recommendations_found >= num_recommendations:
                break

        return common_neighbors_recommendations