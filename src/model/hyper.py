from create_representation import load_data, bag_of_words, tf_idf, word_2_vec
from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabasz_score
from hyperopt import hp, fmin, tpe, Trials
import numpy as np

space = {
    'n_clusters': hp.choice('n_clusters', range(50, 100)),
    'init': hp.choice('init', ['k-means++', 'random']),
    'n_init': hp.choice('n_init', range(5, 10)),
    'max_iter': hp.choice('max_iter', range(10, 20))
}

def evaluate_bow(params):
    model = KMeans(**params, random_state=42)
    model.fit(bow_df)
    score = calinski_harabasz_score(bow_df, model.labels_)
    return -score

def hyper_bow():
    trials = Trials()
    best = fmin(
        fn=evaluate_bow,
        space=space,
        algo=tpe.suggest,
        max_evals=500,
        trials=trials
    )
    print("Mejores hiperparámetros encontrados:")
    print(best)

if __name__ == "__main__":
    df = load_data()
    df['title'] = df['title'].apply(lambda x: x.split(' '))
    columna_title_lista = df['title'].tolist()
    bow_df = bag_of_words(columna_title_lista)
    tf_df = tf_idf(columna_title_lista)
    w2v_df = word_2_vec(columna_title_lista)

    hyper_bow()




