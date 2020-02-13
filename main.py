import pandas as pd
import requests

games = requests.get('https://api.rawg.io/api/games')

game_data = pd.json_normalize(games.json())

print(game_data.columns)
