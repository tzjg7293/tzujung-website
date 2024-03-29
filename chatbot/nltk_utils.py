## Preprocessing techniques: ##
import numpy as np
import nltk
nltk.download('punkt') # Only need to download for first time
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer  # Can try different imports of stemmers instead of PorterStemmer
# Using lemmatizer instead of stemmer b/c more accurate even though it has more recall time

# Create a lemmatizer
lemmatizer = WordNetLemmatizer()

# function to tokenize the sentences - split sentence into individual words
def tokenize(sentence):
    """
    split sentence into array of words/tokens
    a token can be a word or punctuation character, or number
    """
    return nltk.word_tokenize(sentence)

# Extract the roots of each word - eg. {organize, organizing, organizer} => {organ, organ, organ}
def lemma(word):
    """
    stemming = find the root form of the word
    examples:
    words = ["organize", "organizes", "organizing"]
    words = [stem(w) for w in words]
    -> ["organ", "organ", "organ"]
    """
    return lemmatizer.lemmatize(word.lower())  # We want to lower case all the words too so use word.lower()

# Convert the individial tokens (words) into number - binary
def bag_of_words(tokenized_sentence, all_words):
    """
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    tokenized_sentence = [lemma(word) for word in tokenized_sentence]

    bag = np.zeros(len(all_words), dtype = np.float32) # Create an array filled with zeroes that is the length of all the words in the list
    for idx, w in enumerate(all_words): # Will give index (idx) and current word (w) in all the words
        if w in tokenized_sentence: # If word is in tokenized sentence
            bag[idx] = 1 # Then the bag with this index will = 1

    return bag

## Testing bag_of_words function
    # sentence = ["hello", "how", "are", "you"]
    # words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    # bag = bag_of_words(sentence, words)
    # print(bag)

## For testing the preprocessing techniques
    # test_string = "This is a test?"
    # words = ["Organize, organizes, Organizing"]
    # print(test_string)
    # print(words)

    # test_string = tokenize(test_string)
    # print(test_string)

    # stemmed_string = [stem(w) for w in words]
    # print(stemmed_string)