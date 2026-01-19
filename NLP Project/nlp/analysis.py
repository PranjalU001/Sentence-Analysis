import nltk
import spacy

# Load spaCy English model
try:
    nlp = spacy.load("en_core_web_sm")
except:
    import os
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def pos_tagging(tokens):
    return nltk.pos_tag(tokens)

def dependency_parsing(tokens):
    doc = nlp(" ".join(tokens))
    return [(token.text, token.dep_, token.head.text) for token in doc]

def named_entities(sentence):
    doc = nlp(sentence)
    return [(ent.text, ent.label_) for ent in doc.ents]

def lemmatization(tokens):
    doc = nlp(" ".join(tokens))
    return [token.lemma_ for token in doc]
