import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec

NAME_FILE = 'noticias.csv'

def load_data():
    try:
        return pd.read_csv(NAME_FILE, sep=',')
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{NAME_FILE}'. La ejecución se detendrá.")
        raise SystemExits
    
def bag_of_words(words):
    strings = [' '.join(tokens) for tokens in words]
    vectorizer = CountVectorizer()
    matriz_bow = vectorizer.fit_transform(strings)
    return pd.DataFrame(matriz_bow.toarray(), columns=vectorizer.get_feature_names_out())

def tf_idf(words):
    strings = [' '.join(tokens) for tokens in words]
    tfidf_vectorizer = TfidfVectorizer()
    tf = tfidf_vectorizer.fit_transform(strings)
    return pd.DataFrame(tf.toarray(), columns=tfidf_vectorizer.get_feature_names_out())

def word_2_vec(words):
    return Word2Vec(sentences=words, vector_size=100, window=5, min_count=1, workers=4)

    
if __name__ == "__main__":
    df = load_data()
    df['title'] = df['title'].apply(lambda x: x.split(' '))
    #para obtener lista con listas de strings
    columna_title_lista = df['title'].tolist() 
    filtrado = [titulo_lista for tipo, titulo_lista in zip(df['type_new'], columna_title_lista) if tipo == 'Politica']

    df = tf_idf(columna_title_lista)
    print(df)
    #df.to_csv('prueba.csv', index=False)
    