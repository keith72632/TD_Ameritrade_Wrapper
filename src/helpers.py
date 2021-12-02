import json

def print_json(response):
    print(json.dumps(response, sort_keys=True, indent=4))
