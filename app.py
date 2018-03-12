import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def search(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        response = input("Did you mean %s? Enter yes or no. " % get_close_matches(word, data.keys())[0])
        if response.lower() == "yes":
            return data[get_close_matches(word, data.keys())[0]]
        elif response.lower() == "no":
            return "Word not in database."
        else:
            return "Invalid entry, please try again. "
    elif word.title() in data:
        return data[word.title()]
    else:
        return "Word not in database, please make sure it's a real word."

word = input("Enter word: ")
definition = search(word)
if type(definition) == list:
    for item in definition:
        print(item)
else:
    print(search(word))
