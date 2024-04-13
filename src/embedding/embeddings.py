from sentence_transformers import SentenceTransformer
from clean import execute
import numpy as np
import logs
import logging

def create_embedding():
    logging.info('Carga modelo de embedding')
    model = SentenceTransformer('hiiamsid/sentence_similarity_spanish_es')
    news_list = execute()
    logging.info('Creacion de embeddings')
    sentence_embeddings = model.encode(news_list)
    logging.info('Normalizacion de embeddings')
    lengths = np.linalg.norm(sentence_embeddings, axis=1, keepdims=True)
    normalized_embeddings = sentence_embeddings / lengths
    return sentence_embeddings, normalized_embeddings