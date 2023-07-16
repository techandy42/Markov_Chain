import pandas as pd

# Load the CSV file as a DataFrame
word_matrix = pd.read_csv('markov_chain.csv', index_col=0)

# Read the first word 
first_word = input("Enter the first word: ")

# Read the number of output words
num_words = int(input("Enter the number of words to be generated: "))

words = []
current_word = first_word
for i in range(num_words):
  words.append(current_word)
  current_word = word_matrix.loc[current_word].idxmax()
  print(current_word)

