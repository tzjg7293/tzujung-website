## Load training data (the intent json file) - NOTE: RERUN TRAINING FILE WHENEVER intents.json IS MODIFIED!
import json
import numpy as np
import random

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from nltk_utils import tokenize, stem, bag_of_words # import the functions that we created in nltk_utils.py
from model import NeuralNetwork # Import our NeuralNetwork model from model.py

with open('chatbot/intents.json', 'r') as f:
    intents = json.load(f)

# lists to store the tokens and stems etc
all_words = []
tags = []
xy = []

# Tokenization
for intent in intents['intents']: # for intent in the list of intents in the json file with the key 'intents' - since json file is now displays as a python dictionary (aka python obj)
    tag = intent['tag']
    tags.append(tag) # add to tag list
    for pattern in intent['patterns']:
        # tokenize each word in the sentence
        w = tokenize(pattern)
        # add to our words list
        all_words.extend(w) # Using extend isntead of append b/c 'w' is already an array, so we don't want all_words to be an array of arrays
        # add to xy pair
        xy.append((w, tag))
        
# Create the list of words that we want to ignore
ignore_words = ['?', '!', '.', ',']

# Stemming
all_words = [stem(w) for w in all_words if w not in ignore_words] # Stem all the words that's not in the ignore words list
all_words = sorted(set(all_words)) # remove duplicates and sort - set() removes duplicate elements, we only want to keep the unique words; sorted() returns sorted list
tags = sorted(set(tags))

## Creating and training the data
# creating the bag of words
X_train = []
y_train = []

for(pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag) # append this to the x training data
    label = tags.index(tag) # y is the labels - so the list of tags will be indexed according to their order
    y_train.append(label) # Using CrossEntropyLoss later here so we odn't need to worry about 1 hot vector encoding

# convert to numpy array
X_train = np.array(X_train) # Capitalized X_train represents 2-D vector, while lower case represents 1-D vectors
y_train = np.array(y_train)

## Create a pytorch dataset from the X_train and y_train dataset
class ChatDataset(Dataset): # Create a new class called chatDataset that inherits Dataset

    # Constructor
    def __init__(self):
        self.n_samples = len(X_train) # Number of samples = length of x training data
        self.x_data = X_train  
        self.y_data = y_train

    # Define the get item function so we can later on access dataset[idx]
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index] # Return as a tuple of x and y data
    
    # Length method
    def __len__(self):
        return self.n_samples
    
# Hyper-parameters (can be changed)
batch_size = 8
input_size = len(X_train[0]) # Length of each bag_of_words we created. In this case it has the same length as the all_words array, or we can use the first set of X_train data since they all have the same length
hidden_size = 8
output_size = len(tags) # Number of different classes aka tags that we have
learning_rate = 0.001
num_epochs = 1000 # Num of training iterations
print(input_size, output_size)

#  Check before running
dataset = ChatDataset()
# training loader
train_loader = DataLoader(dataset = dataset, batch_size = batch_size, shuffle = True, num_workers = 0) # Depending on num_workers, the more the faster it loads but takes more cpu

# If we have GPU available we can specify it here
device = torch.device("cuda" if torch.cuda.is_available() else "cpu") # If if we have cuda, push our model to it to use it, otherwise use cpu
# Integrate model
model = NeuralNetwork(input_size, hidden_size, output_size).to(device) # Push our model to either cuda or cpu depending on availability

# Specify the loss and optimizer
criterion = nn.CrossEntropyLoss() # CrossEntropyLoss ayutomatically applied softmax
optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate) # We are optimizing the model.parameters(); lr = learning rate

# Define the training epoch (loops)
for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        word = words.to(device) # we want to push it to the device
        labels = labels.to(dtype=torch.long).to(device)

        # call the forward pass
        outputs = model(words) # words as the input
        loss = criterion(outputs, labels) # calculate the loss; outputs = predicted output; labels = actual labels

        # backward pass and optimizer step
        optimizer.zero_grad() # empty the gradient first
        loss.backward() # to calculate back propagation
        optimizer.step()

    # Print this every 100 epoch (iterations)
    if (epoch + 1) % 100 == 0:
        print(f"epoch [{epoch + 1} / {num_epochs}], loss = {loss.item():.4f}") # print as a f string the current epoch: (epoch + 1), and the total number of epochs (num_epochs); print loss item up to 4 decimal points

print(f"final loss, loss = {loss.item():.4f}") # print the final loss - the lost at the end

## SAVING THE TRAINED DATA
# Create a dictionary to store different things about the model
data = {
    "model_state": model.state_dict(),
    "input_size": input_size,
    "output_size": output_size,
    "hidden_size": hidden_size,
    "all_words": all_words, # Store all the words we collected at the beginning
    "tags": tags
}

FILE = "chatbot/data/BaconChatbotData.pth" # Define a file name
torch.save(data, FILE) # will save it as a pickle file at the FILE location. THIS IS THE TRAINED MODEL

print(f"Training complete. File saved to {FILE}")