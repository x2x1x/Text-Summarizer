# Text-Summarizer

This code defines a function summarize that takes in a piece of text and a number of sentences, and returns a summary of the text.

The summary is created by first cleaning the text by removing any numbers in square brackets and replacing multiple spaces with a single space. The text is then tokenized and converted to lowercase, and the stop words (such as "the", "a", "an") are removed. The frequency of each word in the text is calculated, and the weighted frequency of each word is determined by dividing the frequency of each word by the maximum frequency of any word.

The text is then tokenized into sentences, and a score is calculated for each sentence by summing the weighted frequencies of the words in the sentence. The top num_sentences sentences with the highest scores are selected and joined together to create the summary.

The function can be called by passing in a piece of text and the desired number of sentences in the summary as arguments. The function will then return the summary as a string.
