from create_representation import load_data, bag_of_words, tf_idf, word_2_vec
from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabasz_score, davies_bouldin_score
from hyperopt import hp, fmin, tpe, Trials
from hyperopt.early_stop import no_progress_loss
import numpy as np

space = {
    'n_clusters': hp.loguniform('n_clusters', np.log(10), np.log(300)),
    'init': hp.choice('init', ['k-means++']), 
    'n_init': hp.choice('n_init', range(5, 15)),
    'max_iter': hp.choice('max_iter', range(1, 2))
}

def evaluate_bow(params):
    params['n_clusters'] = int(params['n_clusters'])
    model = KMeans(**params, random_state=42)
    model.fit(bow_df)
    score = davies_bouldin_score(bow_df, model.labels_)
    return score

def hyper_bow():
    trials = Trials()
    early_stop = no_progress_loss(iteration_stop_count=100)
    best = fmin(
        fn=evaluate_bow,
        space=space,
        algo=tpe.suggest,
        max_evals=400, 
        trials=trials,
        early_stop_fn=early_stop
    )
    print("Mejores hiperparámetros encontrados:")
    print(best)
    return trials

if __name__ == "__main__":
    df = load_data()
    df['title'] = df['title'].apply(lambda x: x.split(' '))
    columna_title_lista = df['title'].tolist()
    bow_df = bag_of_words(columna_title_lista)
    tf_df = tf_idf(columna_title_lista)
    w2v_df = word_2_vec(columna_title_lista)

    tri = hyper_bow()