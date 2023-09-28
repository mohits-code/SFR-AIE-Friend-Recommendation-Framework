import json

class FriendRecommendations:
    
    # Initialize the class with the path to the users data file
    def __init__(self, users_file_path):
        self.users_file_path = users_file_path


    def find_friend_of_friend_recommendations(self, target_user_id, num_recommendations):
        
        # Open and read the JSON file containing user data
        with open(self.users_file_path, 'r') as users_file:
            users_data = json.load(users_file)
            users = users_data['users']
        
        # Find the target user's data
        target_user_data = next((user for user in users if user['id'] == target_user_id), None)
        
        # Find all friends of the target user and store their ids
        friend_ids = [int(fid.strip()) for fid in target_user_data['friends'].split(',')]
        recommendations_found=0
        friend_recommendations = []

        for friend_id in friend_ids:
            # Find the friend's data
            friend = next((user for user in users if user['id'] == friend_id), None)

            if not friend:
                continue
            
            # Store friend-of-friend ids
            friend_of_friend_ids = [int(fid.strip()) for fid in friend['friends'].split(',')]

            for friend_of_friend_id in friend_of_friend_ids:
                if recommendations_found >= num_recommendations:
                    break
                
                # Store the friend-of-friend's data
                friend_of_friend = next((user for user in users if user['id'] == friend_of_friend_id), None)

                # Check if the friend-of-friend is valid for recommendation
                if friend_of_friend and friend_of_friend['id'] != target_user_data['id'] and friend_of_friend['id'] not in friend_ids:
                    friend_recommendations.append(friend_of_friend)
                    recommendations_found += 1

        return friend_recommendations
