import json

config_file = "./config.json"

with open(config_file, 'r') as f:
    config = json.loads(f.read())

