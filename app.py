import json

data = json.load(open("data.json"))

def search(word):
    return data[word]

word = input("Enter word: ")

print(search(word))
