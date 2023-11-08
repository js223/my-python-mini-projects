import json
from difflib import get_close_matches

with open('data.json', 'r') as file:
    data = json.load(file)

def closeMatches(word):
    word= word.lower()
    matches = get_close_matches(word, data.keys())
    if word in data:
        for i in range(len(data[word])):
            print(data[word][i])
    elif word.upper() in data:
        word = word.upper()
        for i in range(len(data[word])):
            print(data[word][i])
    elif word.title() in data:
        word = word.title()
        for i in range(len(data[word])):
            print(data[word][i])
    elif matches:
        suggestion = matches[0]
        print(f"did you mean '{suggestion}' instead? (y/n)")
        second_match = input()
        if second_match == 'y':
            for i in range(len(data[suggestion])):
                print(data[suggestion][i])
        else :
            print("pugger your paw steps on working keys ")
    else:
        print("You have entered wrong keys. Try again")


decision_char = 'y'

while decision_char == 'y':
    print("Enter the word you want to search: ")
    word = input()
    closeMatches(word)
    print()
    print("Do you wanna keep search? (y/n)")
    decision_char = input()
    print()