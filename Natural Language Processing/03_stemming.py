from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
ex = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]


text = "All pythoners should work pythonly with python. Their pythoning is pythoned effectively."

text_tokens = word_tokenize(text)

for w in text_tokens:
    print(ps.stem(w))