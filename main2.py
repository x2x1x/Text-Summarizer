import os
import sys
import tkinter as tk
import tkinter.simpledialog as simpledialog
from tkinter.filedialog import asksaveasfile
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import codecs

nltk.download('punkt')
nltk.download('stopwords')

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

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

def save_text(summarized):
    file = asksaveasfile(mode='w', defaultextension=".txt")
    if file:  # Check if file is not None
        f = codecs.open(file.name, 'w', encoding='utf-8')
        f.write(summarized)  # Write the summary to the file
        f.close()  # Close the file

def on_button_click():
    # Clear the text in the output window
    output_text.delete(1.0, tk.END)

    # This function will be called when the button is clicked
    text = simpledialog.askstring("Input", "Text To summarize: ", parent=window)
    if text:  # Check if text is not None
        num_sentences = simpledialog.askstring("Input", "How many sentences the text should be: ", parent=window)
        if num_sentences:  # Check if num_sentences is not None
            summarized = summarize(text, num_sentences)
            output_text.insert(tk.END, f"{summarized}\n")

def on_save_button_click():
    summarized = output_text.get(1.0, tk.END)  # Get the summary from the output text widget
    save_text(summarized)  # Save the summary to a file

# Create the main window
window = tk.Tk()
window.wm_title("Summarizer")

# Create a button widget
save_button = tk.Button(text="Save", command=on_save_button_click)

# Create a button widget
button = tk.Button(text="Summarize", command=on_button_click)

# Place the button on the window
button.pack()

# Place the button on the window
save_button.pack()

# Create a text widget to display the output
output_text = tk.Text(window)

# Place the text widget on the window
output_text.pack()

# Run the Tkinter event loop
window.mainloop()
