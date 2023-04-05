# test from https://www.kaggle.com/code/niraliivaghani/chatbot-training-model/notebook

## Load training data (the intent json file) - NOTE: RERUN TRAINING FILE WHENEVER intents.json IS MODIFIED!
import json
import pickle
import numpy as np
import random

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

from nltk_utils import tokenize, lemma, bag_of_words # import the functions that we created in nltk_utils.py
# from model import NeuralNetwork # Import our NeuralNetwork model from model.py


with open('/home/ubuntu/my_website/chatbot/intents.json', 'r') as f:
    intents = json.load(f)

# lists to store the tokens and stems etc
all_words = []
tags = []
xy = [] # xy = combination pair between patterns and intents
# Create the list of words that we want to ignore
ignore_words = ['?', '!', '.', ',']

# Tokenization
for intent in intents['intents']: # for intent in the list of intents in the json file with the key 'intents' - since json file is now displays as a python dictionary (aka python obj)
    tag = intent['tag']
    if intent['tag'] not in tags:
        tags.append(tag) # add to tag list
    for pattern in intent['patterns']:
        # tokenize each word in the sentence
        w = tokenize(pattern)
        # add to our words list
        all_words.extend(w) # Using extend isntead of append b/c 'w' is already an array, so we don't want all_words to be an array of arrays
        # add to xy pair
        xy.append((w, tag))

# lemmatize, lower each word and remove duplicates
all_words = [lemma(w) for w in all_words if w not in ignore_words] # Stem all the words that's not in the ignore words list
all_words = sorted(list(set(all_words))) # remove duplicates and sort - set() removes duplicate elements, we only want to keep the unique words; sorted() returns sorted list
tags = sorted(list(set(tags))) # Sort the tags

# see current data
print (len(xy), "patterns\n", xy, "\n")
# classes = intents[tag]
print (len(tags), "classes\n", tags, "\n")
# words = all words, vocabulary
print (len(all_words), "unique lemmatized words\n", all_words, "\n")
pickle.dump(all_words,open('/home/ubuntu/my_website/chatbot/data/words.pkl','wb'))
pickle.dump(tags,open('/home/ubuntu/my_website/chatbot/data/classes.pkl','wb'))

## Creating and training the data
# create our training data
training = []
# create an empty array for our output
output_empty = [0] * len(tags)

for doc in xy:
    # initialize our bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # lemmatize each word - create base word, in attempt to represent related words
    pattern_words = [lemma(word) for word in pattern_words]
    # create our bag of words array with 1, if word match found in current pattern
    for w in all_words:
        bag.append(1) if w in pattern_words else bag.append(0)
    # output is a '0' for each tag and '1' for current tag (for each pattern)
    output_row = list(output_empty)
    output_row[tags.index(doc[1])] = 1
    training.append([bag, output_row])

# shuffle our features and turn into np.array
random.shuffle(training)
training = np.array(training)
# create train and test lists. X - patterns, Y - intents
train_x = list(training[:,0])
train_y = list(training[:,1])
print("Training data created")
    
# Create model - 3 layers. First layer 128 neurons, second layer 64 neurons and 3rd output layer contains number of neurons
# equal to number of intents to predict output intent with softmax
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compile model. Stochastic gradient descent with Nesterov accelerated gradient gives good results for this model
sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

#fitting and saving the model 
hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
FILE = "/home/ubuntu/my_website/chatbot/data/BaconChatbotData.h5" # Define a file name
model.save(FILE, hist)

print("Model saved to " + FILE)