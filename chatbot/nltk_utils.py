## Preprocessing techniques: ##

import nltk
# nltk.download('punkt')  # Only need to download for first time
from nltk.stem.porter import PorterStemmer  # Can try different imports of stemmers instead of PorterStemmer

# Create a stemmer
stemmer = PorterStemmer()

# function to tokenize the sentences - split sentence into individual words
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

# Extract the roots of each word - eg. {organize, organizing, organizer} => {organ, organ, organ}
def stem(word):
    return stemmer.stem(word.lower())  # We want to lower case all the words too so use word.lower()

# Convert the individial tokens (words) into number - binary
def bag_of_words(tokenized_sentence, all_words):
    pass

# For testing the preprocessing techniques
test_string = "This is a test?"
words = ["Organize, organizes, Organizing"]
print(test_string)
print(words)

test_string = tokenize(test_string)
print(test_string)

stemmed_string = [stem(w) for w in words]
print(stemmed_string)