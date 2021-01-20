# Sentiment analysis of text from emails
# Primary purpose is to set up the foundational framework for scaling up later


# Stanford CoreNLP Setup:
import stanza
corenlp_dir = './corenlp/'
stanza.install_corenlp(dir=corenlp_dir)
import os
os.environ['CORENLP_HOME'] = corenlp_dir
from stanza.server import CoreNLPClient

# Text input is for demonstration and prototyping purposes only
# Future goal is to create a data pipeline to feed all of the emails into CoreNLP
email_text = input("Enter email text: ") 

# Function for counting number of sentences
# Necessary for automatic parsing of text input no matter how many sentences there are

def count_sentences(email_text):
    punctuation_list = []
    for i in range(0, len(email_text)):
        if email_text[i] == '.':
            punctuation_list.append(i)
        elif email_text[i] == '!':
            punctuation_list.append(i)
        elif email_text[i] == '?':
            punctuation_list.append(i)
    sentence_count = list(range(0,len(punctuation_list)))
    return sentence_count

num_sentences = count_sentences(email_text)

# Python interface for the CoreNLP Client
with CoreNLPClient(
        annotators = ['tokenize', 'ssplit', 'sentiment'],
        timeout = 30000,
        memory = '16G') as client:
    ann = client.annotate(email_text)

# Breaks up the text into separate sentences, annotates them, and appends to a list:
sentence_list = []
for x in num_sentences:
    sentence_list.append(ann.sentence[x])

# Derives sentiment from each element within sentence_list, and appends to new list:
sentiment_of_sentences = []
for y in sentence_list:
    sentiment_of_sentences.append(y.sentiment)

# Determines overall sentiment within the email, based on elements within sentiment_of_sentences:
sentiment_score = 0
for z in sentiment_of_sentences:
    if z == 'Negative':
        sentiment_score -= 1
    elif z == 'Neutral':
        sentiment_score += 0
    elif z == 'Positive':
        sentiment_score += 1

print('Sentiment Score =', sentiment_score)


if sentiment_score > 0:
    print('Overall sentiment: Positive')
elif sentiment_score == 0:
    print('Overall sentiment: Neutral')
elif sentiment_score < 0:
    print('Overall sentiment: Negative')

