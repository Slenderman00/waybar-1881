#!/usr/bin/env python3

import requests
import argparse
import json

def gen_name(name):
    return name.replace(" ", "_")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name")

    args = parser.parse_args()

    if not args.name:
        exit()

    name = gen_name(args.name)
    url = f"https://service.1881.no//autocompleteservice/autocomplete/getsuggestions?mode=search&callback=callback&q={name}"
    
    response = requests.get(url).text
    response = response.replace("callback(", "")
    response = response.replace(");", "")
    data = json.loads(response)
    if len(data) != 0:
        print(json.dumps({'text': "🔴"}))
    else:
        print(json.dumps({'text': "🟢"}))

if __name__ == "__main__":
    main()