{
    'dataset_loader_train': {
        '__factory__': 'palladium.dataset.Table',
        'path': '../step1/iris.data',
        'names': [
            'sepal length',
            'sepal width',
            'petal length',
            'petal width',
            'species',
        ],
        'target_column': 'species',
        'sep': ',',
        'nrows': 100,
    },

    'dataset_loader_test': {
        '__copy__': 'dataset_loader_train',
        'nrows': None,
        'skiprows': 100,
    },

    'model_persister': {
        '__factory__': 'palladium.persistence.Database',
        'url': 'sqlite:///iris-model.db',
    },

    # NEW ---------------------------------------------------------------------
    'model': {
        '__factory__': 'model.create_pipeline',
    },

    'scoring': 'accuracy',

    'grid_search': {
        'param_grid': {
            'net__lr': [0.2, 0.3],
            'net__max_epochs': [100],
            'net__module_num_units': [5, 10, 20, 40]
        },
        'cv': 5,
        'verbose': 4,
        'n_jobs': 1,
    },
    # NEW ---------------------------------------------------------------------
}
