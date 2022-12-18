# Text-Summarizer

The summarize program is a tool that generates a summary of a given piece of text. It does this by first cleaning the text to remove any numbers in square brackets and replacing multiple spaces with a single space. The cleaned text is then tokenized and converted to lowercase, and stop words are removed. The program calculates the frequency of each word in the text, and determines the weighted frequency of each word by dividing the frequency of each word by the maximum frequency of any word.

Next, the program tokenizes the text into sentences and calculates a score for each sentence by summing the weighted frequencies of the words in the sentence. The top **num_sentences** with the highest scores are selected and joined together to create the summary.

To use the summarize program, simply pass in a piece of text and the desired number of sentences in the summary as arguments. The program will then return the summary as a string.
