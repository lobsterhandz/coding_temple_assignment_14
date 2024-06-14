import re
import os

# Define positive and negative words
positive_words = ["amazing", "enjoy", "beautiful", "wonderful", "breathtaking", "relaxed", "stunning", "memorable", "excellent", "delicious", "fantastic", "enlightening"]
negative_words = ["bad", "disappointing", "poor", "lackluster", "scarce", "overcrowded"]

def read_travel_blogs(filename):
    print(f"Current working directory: {os.getcwd()}")
    print(f"Looking for file: {filename}")
    
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist in the directory {os.getcwd()}.")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

def count_sentiment_words(text, positive_words, negative_words):
    positive_count = 0
    negative_count = 0

    words = re.findall(r'\b\w+\b', text.lower())
    for word in words:
        if word in positive_words:
            positive_count += 1
        elif word in negative_words:
            negative_count += 1

    return positive_count, negative_count

def generate_summary_report(filename):
    text = read_travel_blogs(filename)
    if text:
        positive_count, negative_count = count_sentiment_words(text, positive_words, negative_words)
        print("Sentiment Analysis Summary:")
        print(f"Positive words: {positive_count}")
        print(f"Negative words: {negative_count}")

# The file is in the same directory
filename = 'travel_blogs.txt'
generate_summary_report(filename)
