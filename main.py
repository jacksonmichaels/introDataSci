import pandas as pd
import requests
import json
from threading import Thread

# URL to retrieve data from
BASE_URL = 'https://api.rawg.io/api/games'
GENRE_URL = 'https://api.rawg.io/api/genres'

# Columns we want to get data from
important_cols = ['id', 'slug', 'name', 'released', 'rating', 'ratings_count', 'metacritic', 'playtime']
# Initialize genres list
genres = []
# Number of pages we want to search through
num_pages = 1000

# Initialize results list
thicc_results = [[] for i in range(num_pages)]


# Retrieve genres from the API
def get_genres():
    genres = requests.get(GENRE_URL)
    data = json.loads(genres.text)['results']
    shorter = [(x['id'], x['name']) for x in data]
    shorter.sort(key=lambda x: x[0])
    return shorter


# Retrieve all games from the URL
def get_games(page, arr):
    if page != 0:
        games = requests.get(BASE_URL + "?page=" + str(page))
    else:
        games = requests.get(BASE_URL)
    game_data = json.loads(games.text)
    results = game_data['results']
    arr[page] = results
    print(page)
    return results


# Convert rows
def convert_row(row):
    new_row = [row[x] for x in important_cols]
    genre_nums = [x['id'] for x in row['genres']]
    genre_row = [int(x[0]) in genre_nums for x in genres]
    new_row += genre_row
    return new_row


# Multi-thread retrieving game data
def start_game_threads():
    # Initialize threads with functions
    threads = [Thread(target=get_games, args=(i, thicc_results)) for i in range(num_pages)]
    print("threads made")

    # Spin up threads
    for thread in threads:
        thread.start()
    print("threads started")

    # Re-join threads (no race conditions here!)
    for thread in threads:
        thread.join()
    print("threads done")

    # Output results list
    print(thicc_results)

    # Flatten list into sub-lists
    flat_list = [item for sublist in thicc_results for item in sublist]

    # Convert rows for easier viewing
    converted_list = [convert_row(y) for y in flat_list]

    # Get relevant column names
    col_names = important_cols + [x[1] for x in genres]

    # Create a pandas DataFrame from the organized list
    df = pd.DataFrame(converted_list, columns=col_names)

    # Return the DataFrame
    return df


# Retrieve genres from API for use
game_genres = get_genres()
# Retrieve game data from API
game_frame = start_game_threads()

# Output data to CSV for visualization
game_frame.to_csv("data/output.csv")

# Output program has finished
print("Data Retrieved")
