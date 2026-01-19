import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download punkt once
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

stop_words = set(stopwords.words("english"))

def clean_text(text):
    # Lowercase
    text = text.lower()
    # Remove special characters and numbers
    text = re.sub(r'[^a-z\s]', '', text)
    return text

def tokenize_and_normalize(text):
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords
    normalized = [t for t in tokens if t not in stop_words]
    return tokens, normalized
