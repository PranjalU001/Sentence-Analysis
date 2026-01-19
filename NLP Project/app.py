from flask import Flask, render_template, request
from nlp.preprocessing import clean_text, tokenize_and_normalize
from nlp.analysis import pos_tagging, dependency_parsing, named_entities, lemmatization
from nlp.vectorizer import tfidf_vectorize
from nlp.model import dummy_model_prediction
import nltk

# Ensure NLTK resources are downloaded
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        sentence = request.form.get("sentence", "")
        if sentence.strip():
            # Preprocessing
            cleaned = clean_text(sentence)
            tokens, normalized_tokens = tokenize_and_normalize(cleaned)

            # NLP Analysis
            pos = pos_tagging(normalized_tokens)
            dep = dependency_parsing(normalized_tokens)
            ner = named_entities(sentence)
            lemmas = lemmatization(normalized_tokens)

            # Vectorize and Dummy Model
            vector = tfidf_vectorize(normalized_tokens)
            prediction = dummy_model_prediction(vector)

            result = {
                "original": sentence,
                "cleaned": cleaned,
                "tokens": tokens,
                "normalized": normalized_tokens,
                "pos_tags": pos,
                "dependency": dep,
                "named_entities": ner,
                "lemmas": lemmas,
                "vector": vector,
                "prediction": prediction
            }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
