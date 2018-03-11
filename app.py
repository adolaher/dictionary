import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def search(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        return "Did you mean %s?" % get_close_matches(word, data.keys())[0]
    elif word.title() in data:
        return data[word.title()]
    else:
        return "Word not in database, please make sure it's a real word."


word = input("Enter word: ")

print(search(word))
