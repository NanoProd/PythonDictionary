
import json
from difflib import get_close_matches

data = json.load(open("dictionary/data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()] #check for words that start with a capital
    elif word.upper() in data:
        return data[word.upper()] #check for words in all caps, like accronyms
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "we didn't understand your entry."
    else:
        return "The word does not exist. Please double check it."

word = input("Please enter a word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)



