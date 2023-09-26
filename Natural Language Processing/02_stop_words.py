from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

ex = "This is an example of stop word filtration "
stopWords = set(stopwords.words("english"))
# print(stopWords)
words = word_tokenize(ex)
filter = [w for w in words if w not in stopWords]
print(filter)