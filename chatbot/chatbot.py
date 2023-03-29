# Rule based chatbot
import random # So we can select random choice(s) from the possible responses
import json

import torch

from model import NeuralNetwork # import our model
from nltk_utils import bag_of_words, tokenize # Import our functions for data curation

# Check if we have GPU available to use
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Open the intents data file
with open('chatbot/intents.json', 'r') as f:
    intents = json.load(f)

# Load the training data file
FILE = "chatbot/data/BaconChatbotData.pth"
data = torch.load(FILE)

# Assign parameters - the info we need to create/run the model again
input_size = data["input_size"] # Assign the value at the key "input_size" in the data file to the local variable "input_size"
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNetwork(input_size, hidden_size, output_size).to(device)

# Load the learnt parameters from above into the model
model.load_state_dict(model_state)
# set it to evaluation mode
model.eval()

## Creating the actual chat
bot_name = "Sydney_bot"

def get_response(msg):
    # Tokenize the sentence and calculate the bag_of_word
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words) # create the bag of words by inputing the tokenized sentence and all the words (all_words) laoded from the data file above
    X = X.reshape(1, X.shape[0]) # reshape X - give it only 1 row b/c we only have 1 sample at a time; second parameter is columns, which is X.shape[0] since model expects it in these dimensions
    X = torch.from_numpy(X).to(device) # convert it to a torch tensor; using from_numpy b/c the bag_of_words function returns a numpy array

    output = model(X) # EXECUTE THE MODEL - This will give us a the prediction
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()] # Get the actual tags by saying tag = tags of the index of the predicted item; predicted.item() is the class label so it's the class's (index) number; tag is the actual tag stored in the intents.json file eg. "greeting"

    # Apply softmax to get the actual probabilities - Check if the probability for the tag is high enough
    probability = torch.softmax(output, dim = 1)  # Looking at softmax of the raw output (output)
    tag_probability = probability[0][predicted.item()] # Actual probability of the tag - both parameters are indexes
    # If the probability is large enough then choose the appropriate response, otherwise print error ("i don't understand...")
    if(tag_probability.item() > 0.75): # items() are used in dictionary.items() to display all the set of items (key and value) in the dictionary
        # Compare the predicted label to the actual labels in the intents.json data file
        for intent in intents['intents']:
            if tag == intent["tag"]: # Find the tag that matches the tag in one of the intents in the intents.json file
                return random.choice(intent['responses']) # Randomly choose a repsonse from the response array in that tag
    
    return "Sorry but I don't understand..."


if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        # sentence = "do you use credit cards?"
        # Get the input
        sentence = input("You: ")
        if sentence == "quit":
            break  # Stop the chat if user says 'quit'

        resp = get_response(sentence)
        print(bot_name + ": " + resp)