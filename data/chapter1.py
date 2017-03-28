from json import json

data = None

with open("chap1_network.json", 'r') as read_json:
    data = json.load(read_json.read())
