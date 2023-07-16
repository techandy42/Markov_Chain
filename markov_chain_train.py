import numpy as np
import pandas as pd
import re

# Read the document
with open('document.txt', 'r') as file:
    document = file.read()

# Convert to lowercase
document = document.lower()

# Remove punctuation using regular expressions
document = re.sub(r'[^\w\s]', '', document)

# Split the document into words
words = document.split()

# Convert the words into a numpy array
word_array = np.array(words)
word_index = np.unique(word_array)

# Create a word_array x word_array pandas Dataframe
word_matrix = pd.DataFrame(0, index=word_index, columns=word_index)

# Train the matrix
prev_word = None;
for word in word_array:
  if prev_word is None:
    prev_word = word
    continue
  word_matrix.loc[prev_word, word] += 1
  prev_word = word

# Normalize the matrix
max_value = word_matrix.max().max()
word_matrix = word_matrix / max_value

# Store the matrix as a csv file
word_matrix.to_csv('markov_chain.csv')

