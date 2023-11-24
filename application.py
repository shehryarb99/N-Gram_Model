# Import the required libraries
import streamlit as st
import nltk
from nltk.util import ngrams

# Download the 'punkt' resource
nltk.download('punkt')

# Define a function to generate n-grams from a text
def generate_ngrams(text, n):
  # Tokenize the text into words
  words = nltk.word_tokenize(text)
  # Generate the n-grams
  ngrams_list = list(ngrams(words, n))
  # Return the n-grams as a list of tuples
  return ngrams_list

# Create a streamlit app
st.title("N-gram Generator")
st.write("This app allows you to input a text passage and then outputs the n-grams extracted from that text.")

# Get the user input for the text passage
text = st.text_area("Enter your text passage here:")

# Get the user input for the n value
n = st.slider("Select the n value for n-grams:", min_value=1, max_value=5, value=2)

# Check if the text is not empty
if text:
  # Generate the n-grams from the text
  ngrams = generate_ngrams(text, n)
  # Display the n-grams as a table
  st.write(f"The {n}-grams extracted from the text are:")
  st.table(ngrams)
