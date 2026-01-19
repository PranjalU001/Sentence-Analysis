from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

def tfidf_vectorize(tokens):
    text = [" ".join(tokens)]
    return vectorizer.fit_transform(text).toarray()
