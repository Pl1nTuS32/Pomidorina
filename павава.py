import json
from pprint import pprint

with open('pubg_players.json', 'r', encoding='utf-8') as f:
    player_stats = json.load(f)

pprint(player_stats[:10])