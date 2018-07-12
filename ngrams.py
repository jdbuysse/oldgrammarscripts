from nltk.corpus import webtext
from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import TrigramAssocMeasures
words = [w.lower() for w in webtext.words('tenderButtons.txt')]
bcf = TrigramCollocationFinder.from_words(words)
bcf.nbest(TrigramAssocMeasures.likelihood_ratio, 4)


##from nltk.corpus import stopwords
##stopset = set(stopwords.words('english'))
##filter_stops = lambda w: len(w) < 3 or w in stopset
##bcf.apply_word_filter(filter_stops)
##bcf.nbest(BigramAssocMeasures.likelihood_ratio, 4)
