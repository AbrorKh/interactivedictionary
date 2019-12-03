import json #To get the data from .json file
from difflib import get_close_matches #To find close matches to the incorrectly typed word. 

data = json.load(open("C:/Users/Abror Khaytbaev/Desktop/Python_apps/Application 1 - Dictionary/data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word, data.keys())) > 0 :
        a = input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(word, data.keys())[0])
        if a == 'y' or a == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif a == 'n' or a == 'N':
            return "Sorry we could not find any definitions for the word you requested."
        else:
            return "I couldn't understand your answer."       
    else:
        return "The word doesn't exist. Please double check it."
 
word = input("Enter a word here: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

e = input("If the result is satisfactory press close to exit.")
print(e)
    
    
