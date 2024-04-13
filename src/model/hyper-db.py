from create_representation import load_data, bag_of_words, tf_idf, word_2_vec
from sklearn.cluster import DBSCAN
from sklearn.metrics.pairwise import cosine_similarity
from hyperopt import hp, fmin, tpe, Trials
from hyperopt.early_stop import no_progress_loss
import numpy as np

eps_values = np.linspace(0.1, 2.0, 100)

space = {
    'eps': hp.choice('eps', eps_values),
    'min_samples': hp.choice('min_samples', range(1, 10)), 
    'metric': hp.choice('metric', ['euclidean', 'manhattan', 'cosine'])
}

def evaluate_bow(params):
    model = DBSCAN(**params)
    model.fit(similarity_matrix_bow)
    return -(len(set(model.labels_)) - (1 if -1 in model.labels_ else 0))

def hyper_bow():
    trials = Trials()
    early_stop = no_progress_loss(iteration_stop_count=10)
    best = fmin(
        fn=evaluate_bow,
        space=space,
        algo=tpe.suggest,
        max_evals=30, 
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

    similarity_matrix_bow = cosine_similarity(bow_df)

    tri = hyper_bow()