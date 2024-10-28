import numpy as np
import nltk
import re
from nltk.corpus import stopwords
from gensim.models import Word2Vec
import gensim.models.keyedvectors as word2vec
from transformers import AutoTokenizer
import spacy
import math

# Load the spaCy model for English language
nlp = spacy.load("en_core_web_sm")
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

def essay_to_wordlist(essay_v, remove_stopwords):
    """Remove the tagged labels and word tokenize the sentence using spaCy."""
    doc = nlp(essay_v)
    words = [token.lemma_ for token in doc if token.is_alpha]  # Get lemmas of words
    if remove_stopwords:
        words = [w for w in words if not nlp.vocab[w].is_stop]  # Remove stopwords using spaCy
    return words

def essay_to_sentences(essay_v):
    """Sentence tokenize the essay using spaCy."""
    doc = nlp(essay_v)
    return [[token.lemma_ for token in sent if token.is_alpha] for sent in doc.sents]

def remove_stopwords(sentences):
    stops = set(nlp.Defaults.stop_words)
    filtered_sentences = []
    for sent in sentences:
        words = sent.split()  # Split the sentence into words
        filtered_sentences.append(" ".join([word for word in words if word.lower() not in stops]))
    return filtered_sentences

def makeFeatureVec(words, model, num_features):
    """Make Feature Vector from the words list of an Essay."""
    featureVec = np.zeros((num_features,), dtype="float32")
    num_words = 0.
    index2word_set = set(model.index_to_key)
    for word in words:
        if word in index2word_set:
            num_words += 1
            featureVec = np.add(featureVec, model[word])
    if num_words > 0:
        featureVec = np.divide(featureVec, num_words)
    return featureVec

def getAvgFeatureVecs(essays, model, num_features):
    """Generate the word vectors for Word2Vec model."""
    essayFeatureVecs = np.zeros((len(essays), num_features), dtype="float32")
    for idx, essay in enumerate(essays):
        essayFeatureVecs[idx] = makeFeatureVec(essay, model, num_features)
    return essayFeatureVecs