import pandas as pd
import requests
import json
from threading import Thread

BASE_URL = 'https://api.rawg.io/api/games'

important_cols = ['id', 'slug', 'name', 'released', 'rating', 'ratings_count', 'metacritic', 'playtime']
genres = []
num_pages = 1000

thicc_results = [[] for i in range(num_pages)]

def get_genres():
    genres = requests.get('https://api.rawg.io/api/genres')
    data = json.loads(genres.text)['results']
    shorter = [(x['id'], x['name']) for x in data]
    shorter.sort(key=lambda x:x[0])
    return shorter


def getGames(page, arr):
    if page != 0:
        games = requests.get(BASE_URL + "?page=" + str(page))
    else:
        games = requests.get(BASE_URL)
    game_data = json.loads(games.text)
    results = game_data['results']
    arr[page] = results
    print(page)
    return results

def convertRow(row):
    newRow =[row[x] for x in important_cols]
    genreNums = [x['id'] for x in row['genres']]
    genreRow = [int(x[0]) in genreNums for x in genres]
    newRow += genreRow
    return newRow

def startGameThreads():
    threads = [Thread(target=getGames, args=(i,thicc_results)) for i in range(num_pages)]
    print("threads made")
    for thread in threads:
        thread.start()

    print("threads started")
    for thread in threads:
        thread.join()

    print("threads done")
    print(thicc_results)

    flat_list = [item for sublist in thicc_results for item in sublist]


    converted_list = [convertRow(y) for y in flat_list]

    col_names = important_cols + [x[1] for x in genres]

    df = pd.DataFrame(converted_list, columns=col_names)

    return df

genres = get_genres()
df = startGameThreads()

df.to_csv("data/butt.csv")

print("real done")