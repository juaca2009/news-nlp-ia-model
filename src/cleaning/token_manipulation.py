import spacy

nlp = spacy.load('es_core_news_lg')

def get_tokens(text):
    doc = nlp(text)
    return [token for token in doc]

def remove_stopwords(tokens):
    clean_tokens = []
    for token in tokens:
        if not token.is_stop:
            clean_tokens.append(token)
    return clean_tokens

def apply_lemma(tokens):
    lemma_tokens = []
    for token in tokens:
        lemma_tokens.append(token.lemma_)
    return lemma_tokens

def clean_tokens(text):
    tokens = get_tokens(text)
    tokens = remove_stopwords(tokens)
    return apply_lemma(tokens)

if __name__ == "__main__":
    text = "Corriendo texto de prueba para probar el funcionamiento correcto de las funciones"
    print(clean_tokens(text))
