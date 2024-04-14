import optuna
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from embeddings import create_embedding
from optuna.storages import _CachedStorage
import numpy as np
import logs
import logging

def objective(trial):
    n_clusters = trial.suggest_int('n_clusters', 500, 1500)
    max_iter = trial.suggest_int('max_iter', 50, 500, log=True)
    n_init = trial.suggest_int('n_init', 10, 12, log=True)
    model = KMeans(n_clusters=n_clusters, init='k-means++', max_iter=max_iter, n_init=n_init)
    model.fit(embedding)
    score = silhouette_score(embedding, model.labels_)
    print(f"Params: {trial.params}, Score: {score}")
    return score

def hyper_k():
    study = optuna.create_study(direction='maximize', sampler=optuna.samplers.CmaEsSampler())
    study.optimize(objective, n_trials=500, n_jobs=12)
    best_params = study.best_params
    print("Best params:", best_params)

if __name__ == "__main__":
    embedding, n_embedding = create_embedding()
    logging.info('Busqueda hiperparametros')
    tri = hyper_k()