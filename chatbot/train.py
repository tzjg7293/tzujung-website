## Load training data (the intent json file) 
import json
# import the functions that we created in nltk_utils.py
from nltk_utils import tokenize, stem, bag_of_words
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

with open('chatbot/intents.json', 'r') as f:
    intents = json.load(f)

# lists to store the tokens and stems etc
all_words = []
tags = []
xy = []

# Tokenization
for intent in intents['intents']: # for intent in the list of intents in the json file with the key 'intents' - since json file is now displays as a python dictionary (aka python obj)
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w) # Using extend isntead of append b/c 'w' is already an array, so we don't want all_words to be an array of arrays
        xy.append((w, tag))
        
print(xy)
# Create the list of words that we want to ignore
ignore_words = ['?', '!', '.', ',']

# Stemming
all_words = [stem(w) for w in all_words if w not in ignore_words] # Stem all the words that's not in the ignore words list
all_words = sorted(set(all_words)) # set() removes duplicate elements - we only want to keep the unique words; sorted() returns sorted list
tags = sorted(set(tags))

## Training the data - creating the bag of words
x_train = []
y_train = []

for(w, tag) in xy:
    bag = bag_of_words(w, all_words)
    x_train.append(bag) # append this to the x training data
    label = tags.index(tag) # y is the labels - so the list of tags will be indexed according to their order
    y_train.append(label) # Using CrossEntropyLoss later here so we odn't need to worry about 1 hot vector encoding

# convert to numpy array
x_train = np.array(x_train)
y_train = np.array(y_train)

## Create a pytorch dataset from the x_train and y_train dataset
class ChatDataset(Dataset): # Create a new class called chatDataset that inherits Dataset

    # Constructor
    def __init__(self):
        self.n_samples = len(x_train) # Number of samples = length of x training data
        self.x_data = x_train  
        self.y_data = y_train

    # Define the get item function so we can later on access dataset[idx]
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index] # Return as a tuple of x and y data
    
    # Length method
    def __len__(self):
        return self.n_samples
    
    # Hyperparameters
    batch_size = 8

    #  Check before running
    dataset = ChatDataset()
    train_loader = DataLoader(dataset = dataset, batch_size = batch_size, shuffle = True, num_workers = 2) # Depending on num_workers, the more the faster it loads but takes more cpu
