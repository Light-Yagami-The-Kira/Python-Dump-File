from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Hello there! Wishing you a warm and delightful day! May your path be filled with joy, success, and wonderful moments. Remember to embrace every opportunity that comes your way and cherish the precious moments with your loved ones. Have a fantastic day ahead!"
print(sent_tokenize(example_text))
print(word_tokenize(example_text))