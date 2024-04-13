from hyperopt import hp, fmin, tpe, Trials
from hyperopt.early_stop import no_progress_loss
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from embeddings import create_embedding
import numpy as np
import logs
import logging

space = {
    'n_clusters': hp.loguniform('n_clusters', np.log(10), np.log(6300)),
    'init': hp.choice('init', ['k-means++', 'random']), 
    'n_init': hp.choice('n_init', range(10, 15)),
    'max_iter': hp.choice('max_iter', range(1, 2))
}

def evaluate_k(params):
    params['n_clusters'] = int(params['n_clusters'])
    model = KMeans(**params, random_state=42)
    model.fit(embedding)
    score = silhouette_score(embedding, model.labels_)
    return -score

def hyper_k():
    trials = Trials()
    early_stop = no_progress_loss(iteration_stop_count=200)
    best = fmin(
        fn=evaluate_k,
        space=space,
        algo=tpe.suggest,
        max_evals=350, 
        trials=trials,
        early_stop_fn=early_stop
    )
    print("Mejores hiperparámetros encontrados:")
    print(best)
    return trials

if __name__ == "__main__":
    embedding, n_embedding = create_embedding()
    logging.info('Busqueda hiperparametros')
    tri = hyper_k()