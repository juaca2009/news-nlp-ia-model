import logging.config

# Configuración de registro
logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': 'INFO'
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
})
