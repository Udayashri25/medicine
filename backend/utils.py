import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import numpy as np
import gensim.downloader as api
from backend.medicine_data import datasets

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))


def load_word_vectors():
    return api.load("glove-wiki-gigaword-100")


def preprocess_text(text):
    tokens = word_tokenize(text)
    return [token.lower() for token in tokens if token.lower() not in stop_words]


def calculate_similarity(word1, word2, word_vectors):
    if word1 in word_vectors and word2 in word_vectors:
        v1, v2 = word_vectors[word1], word_vectors[word2]
        return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    return 0


def suggest_medicine(symptoms, concern, medical_data, word_vectors):
    suggestions = []
    if concern in medical_data:
        return medical_data[concern]
    for symptom in symptoms:
        for issue, meds in medical_data.items():
            score = calculate_similarity(symptom, issue, word_vectors)
            if score > 0.5:
                suggestions.extend(meds)
    return list(set(suggestions))


def load_medicine_data():
    return datasets
