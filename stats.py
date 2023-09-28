import json
import matplotlib.pyplot as plt
import numpy as np

def load_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def analyze_friends(data):
    friends_counts = []

    for user in data["users"]:
        friends_str = user["friends"]
        friends_list = [int(friend_id) for friend_id in friends_str.split(", ")]
        friends_counts.append(len(friends_list))

    num_users = len(friends_counts)
    min_friends = min(friends_counts)
    max_friends = max(friends_counts)
    avg_friends = sum(friends_counts) / num_users
    median_friends = np.median(friends_counts)
    quartiles = np.percentile(friends_counts, [25, 50, 75])

    plt.hist(friends_counts, bins=20, edgecolor='black')
    plt.title("Friends Count Distribution")
    plt.xlabel("Number of Friends")
    plt.ylabel("Frequency")
    plt.axvline(x=min_friends, color='red', linestyle='--', label=f'Min: {min_friends}')
    plt.axvline(x=max_friends, color='green', linestyle='--', label=f'Max: {max_friends}')
    plt.axvline(x=quartiles[0], color='orange', linestyle='--', label=f'Q1: {quartiles[0]}')
    plt.axvline(x=quartiles[1], color='purple', linestyle='--', label=f'Median: {median_friends}')
    plt.axvline(x=quartiles[2], color='blue', linestyle='--', label=f'Q3: {quartiles[2]}')
    plt.axvline(x=avg_friends, color='cyan', linestyle='--', label=f'Average: {avg_friends}')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    filename = "usersdb.json"
    user_data = load_data(filename)
    analyze_friends(user_data)
