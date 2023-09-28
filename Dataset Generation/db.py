import json
import random
from tqdm import tqdm

# Load interests and activities from interests.json
def load_interests_activities():
    with open('interests.json') as file:
        interests_data = json.load(file)

    interests = []
    activities = []

    for category in interests_data:
        if category['category'] == 'Interests':
            interests += category['items']
        elif category['category'] == 'Activities':
            activities += category['items']

    return interests, activities

# Load demographics from demographics.json
def load_demographics():
    with open('demographics.json') as file:
        demographics_data = json.load(file)

    ages = demographics_data['ages']
    states = demographics_data['states']

    age_weights = demographics_data['weights']['ages']
    state_weights = demographics_data['weights']['states']

    return ages, states, age_weights, state_weights

# Generate users
def generate_users(num_users, interests, activities, ages, states, age_weights, state_weights):
    users = []

    with tqdm(total=num_users, desc='Generating Users') as pbar:
        for i in range(1, num_users + 1):
            # Calculate age based on the new age group structure in demographics.json
            age_group = random.choices(ages, weights=age_weights)[0]
            age_min = age_group['min']
            age_max = age_group['max']
            age = random.randint(age_min, age_max) if age_max else age_min

            # Random number of interests between 0 and 8
            num_interests = random.randint(0, 10)
            user_interests = random.sample(interests, min(num_interests, len(interests)))

            # Random number of activities between 0 and 3
            num_activities = random.randint(0, 5)
            user_activities = random.sample(activities, min(num_activities, len(activities)))

            # Select a random state based on weights
            user_state = random.choices(states, weights=state_weights)[0]

            user = {
                'id': i,
                'age': age,
                'state': user_state,
                'interests': user_interests,
                'activities': user_activities,
                'friends': []  # Initialize friends as an empty list
            }
            users.append(user)
            pbar.update(1)

    return users


def generate_friends(users):
    with tqdm(total=len(users), desc='Generating Friends', leave=True) as pbar:
        # First, assign 10-15 random friends to each user
        for user in users:
            num_friends = random.randint(1, 350)
            friend_ids = set()

            while len(friend_ids) < num_friends:
                friend_id = random.randint(1, len(users))
                if friend_id != user['id']:
                    friend_ids.add(friend_id)

            friend_ids = list(friend_ids)
            user['friends'] = friend_ids

            pbar.update(1)

        # Then, create reciprocal friendships for users
        for user in users:
            for friend_id in user['friends']:
                friend = next((u for u in users if u['id'] == friend_id), None)
                if friend and user['id'] not in friend['friends']:
                    friend['friends'].append(user['id'])

        pbar.update(1)

# Save users to usersdb.json
def save_users(users):
    # Prepare users data for saving
    users_data = {
        'users': []
    }

    for user in users:
        # Convert the list of friend IDs to a comma-separated string
        friends_str = ', '.join(str(friend_id) for friend_id in user['friends'])
        user_data = {
            'id': user['id'],
            'age': user['age'],
            'state': user['state'],
            'interests': user['interests'],
            'activities': user['activities'],
            'friends': friends_str
        }
        users_data['users'].append(user_data)

    with open('usersdb.json', 'w') as file:
        json.dump(users_data, file, indent=4)

def main():
    interests, activities = load_interests_activities()
    ages, states, age_weights, state_weights = load_demographics()

    users = generate_users(20000, interests, activities, ages, states, age_weights, state_weights)
    generate_friends(users)
    save_users(users)

if __name__ == '__main__':
    main()