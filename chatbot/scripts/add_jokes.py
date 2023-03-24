import json

with open('chatbot/data/intents.json', 'r+') as f:
    intents = json.load(f)
    for intent in intents['intents']:
        if(intent['tag'] == 'funny'):
            # print(intent['responses'])
            intent['responses'].append({"IT WORKED!"})
    json.dump(data, file, indent=indent) 

with open('chatbot/data/jokes.txt', 'r') as joke_f:
    jokes = joke_f.read().splitlines()

# print(intents)
# print(jokes)
# for intent in intents['intents']:
#     if(intent['tag'] == 'funny'):
#         print(intent['responses'])
#         intent['responses'] = "testing"
    

# for joke in jokes:
    
