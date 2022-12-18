import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def summarize(text, num_sentences):
    try:
        num_sentences = int(num_sentences)
    except ValueError:
        raise ValueError('num_sentences must be an integer or a string that can be cast to an integer')
    # Clean the text
    text = re.sub(r'\[[0-9]*\]', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    # Tokenize the text and convert to lowercase
    tokens = word_tokenize(text.lower())

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Calculate the frequency of each word
    word_frequencies = {}
    for word in tokens:
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1

    # Calculate the weighted frequency of each word
    max_frequency = max(word_frequencies.values())
    for word in word_frequencies:
        word_frequencies[word] = word_frequencies[word]/max_frequency

    # Tokenize the text and convert to lowercase
    sentence_tokens = nltk.sent_tokenize(text)
    sentence_scores = {}
    for sentence in sentence_tokens:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in word_frequencies:
                if sentence in sentence_scores:
                    sentence_scores[sentence] += word_frequencies[word]
                else:
                    sentence_scores[sentence] = word_frequencies[word]

    # Select the top `num_sentences` sentences with the highest score
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]

    # Join the selected sentences to create the summary
    summary = ' '.join(summary_sentences)
    return summary

text = input("Text You want to summarize: ")
num_sentences = input("How Many sentences it should be: ")

summary = summarize(text, num_sentences)
print(summary)
