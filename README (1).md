# SFR-AIE Friend Recommendation Framework
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/mohits-code/SFR-AIE-Friend-Recommendation-Framework/tree/main)

This repository contains a friend recommendation framework for online social networks, developed as part of a research project under the National Science Foundation REU program.

The framework employs a two-stage process to suggest new friends:
1.  **Candidate Generation**: It first identifies a broad set of potential friend candidates for a target user. The primary method implemented is the **Common Neighbors Algorithm (CNA)**, which finds users who share a significant number of mutual friends with the target user.
2.  **AI-Powered Ranking**: The generated candidates are then ranked using AI-generated embeddings. User profiles, including age, state, interests, and activities, are converted into vector embeddings using OpenAI's `text-embedding-ada-002` model. The framework calculates the cosine similarity between the target user's embedding and each candidate's embedding to find the most compatible matches.

## Project Structure

```
.
├── Dataset Generation/     # Scripts and data for creating a synthetic user dataset
│   ├── db.py               # Main script to generate users and friendships
│   ├── demographics.json   # Defines age/state distributions for users
│   ├── interests.json      # A list of possible interests and activities
│   └── stats.py            # Utility to analyze the generated dataset
├── cna.py                  # Implements the Common Neighbors Algorithm
├── driver.py               # The main executable script to run the framework
├── embeddings.py           # Handles embedding generation via the OpenAI API
├── fof.py                  # Implements a Friend-of-a-Friend recommendation algorithm
├── helpers.py              # Utility functions for similarity calculations
├── LICENSE                 # MIT License
└── mask.py                 # Contains a function for hashing user data (not used in main driver)
```

## Getting Started

Follow these steps to generate a synthetic dataset and run the recommendation framework.

### Prerequisites

You need Python 3 and the following Python libraries installed. You can install them using pip:

```bash
pip install openai numpy inflect tqdm matplotlib
```

### 1. Set up OpenAI API Key

You must have an API key from OpenAI to generate the user embeddings.

Open the `embeddings.py` file and replace the placeholder text with your actual API key:

```python
# In embeddings.py
openai.api_key = 'YOUR-OPENAI-API-KEY-HERE' # previously 'API-KEY-PLACEHOLDER'
```

### 2. Generate the Dataset

The framework requires a user dataset to function. A script is provided to generate a synthetic one.

1.  Navigate to the dataset generation directory:
    ```bash
    cd "Dataset Generation"
    ```

2.  Run the database generation script. This will create a file named `usersdb.json` containing 20,000 synthetic users.
    ```bash
    python db.py
    ```
    *Note: You can run `python stats.py` to see a distribution of friends per user in the generated dataset.*

3.  The main driver script expects the data file to be named `users.json` in the root directory. Move and rename the generated file:
    ```bash
    # From the "Dataset Generation" directory
    mv usersdb.json ../users.json
    ```

### 3. Run the Recommendation Framework

Once the dataset and API key are in place, you can run the main driver script from the root directory of the project.

```bash
# Ensure you are in the root directory of the project
python driver.py
```

The script will output a ranked list of the top 15 friend recommendations for `user_id = 1`, along with their similarity score, age, and state.

```
Proposed Model Recommendations:
1. User ID: 1423 (Similarity Score: 0.845), 32,  NY
2. User ID: 876 (Similarity Score: 0.841), 29,  NY
3. User ID: 5432 (Similarity Score: 0.839), 34,  NJ
...
```

### Customization

You can easily customize the recommendation process by modifying `driver.py`:

*   `target_user_id`: Change the user for whom you want to generate recommendations.
*   `num_candidates`: Adjust the number of initial candidates to generate using the Common Neighbors Algorithm.
*   `num_recommendations`: Set the number of final recommendations to display.

## Author

*   **Mohit Singh**
*   LinkedIn: https://www.linkedin.com/in/mochi-momo/
*   GitHub: https://github.com/mochi-momo
*   Email: emailtomohitsingh@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.