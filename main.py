import pandas as pd
import requests
import json
from threading import Thread

BASE_URL = 'https://api.rawg.io/api/games'

important_cols = ['id', 'slug', 'name', 'released', 'rating', 'ratings_count', 'metacritic', 'playtime']
genres = []
parent_platforms = []
num_threads = 120
num_pages_per_thread = 150

num_games = 380270
games_per_page = 20
pages_per_file = 50

thicc_results = [[] for i in range(num_threads * num_pages_per_thread)]


def get_genres():
    genres = requests.get('https://api.rawg.io/api/genres')
    data = json.loads(genres.text)['results']
    shorter = [(x['id'], x['name']) for x in data]
    shorter.sort(key=lambda x: x[0])
    return shorter


def get_parent_consoles():
    genres = requests.get('https://api.rawg.io/api/platforms/lists/parents')
    data = json.loads(genres.text)['results']
    shorter = [(x['id'], x['name']) for x in data]
    shorter.sort(key=lambda x: x[0])
    return shorter


# end code (jackson)
# start code (connor)
def getGames(pages):
    arr = []
    for page in pages:
        if page % 10 == 0:
            print("Running {}".format(page))
        if page != 0:
            games = requests.get(BASE_URL + "?page=" + str(page))
        else:
            games = requests.get(BASE_URL)
        game_data = json.loads(games.text)
        results = game_data['results']
        arr.append(results)
    return arr


# end code (connor)
# start code (jackson)

def convertRow(row):
    newRow = [row[x] for x in important_cols]
    genreNums = [x['id'] for x in row['genres']]
    parentNums = [x['platform']['id'] for x in row['parent_platforms']]
    genreRow = [int(x[0]) in genreNums for x in genres]
    platformRow = [int(x[0]) in parentNums for x in parent_platforms]
    newRow += genreRow
    newRow += platformRow
    return newRow


def startGameThreads():
    # threads = [Thread(target=getGames,
    #                   args=([j + i * num_pages_per_thread for j in range(num_pages_per_thread)], thicc_results)) for i
    #            in range(num_threads)]
    # print("threads made")
    # for thread in threads:
    #     thread.start()
    #
    # print("threads started")
    # for thread in threads:
    #     thread.join()
    #
    # print("threads done")

    current_page = 0

    while current_page < num_games / games_per_page:
        pages = [i + current_page for i in range(pages_per_file)]
        games = getGames(pages)

        flat_list = [item for sublist in games for item in sublist]

        converted_list = [convertRow(y) for y in flat_list]

        col_names = important_cols + [x[1] for x in genres] + [x[1] for x in parent_platforms]

        df = pd.DataFrame(converted_list, columns=col_names)

        df.to_csv("data/{}-{}.csv".format(current_page, current_page+pages_per_file))

        current_page += pages_per_file

        print("saving data/{}-{}.csv".format(current_page, current_page+pages_per_file))

    return 0


genres = get_genres()
parent_platforms = get_parent_consoles()
startGameThreads()