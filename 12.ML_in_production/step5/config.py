{
    'dataset_loader_train': {
        '__factory__': 'dataset.OpenML',
        'name': 'wine-quality-red',
    },

    'model_persister': {
        '__factory__': 'palladium.persistence.Database',
        'url': 'sqlite:///model.db',
    },

    'model': {
        '__factory__': 'model.create_pipeline',
        # YOUR CODE HERE:
        #
        # The new dataset has a different number of inputs and
        # outputs.  Adjust these parameters:
        #
        # 'module__num_inputs': 4,   # Number of features
        # 'module__num_outputs': 3,  # Number of classes
        'module__num_inputs': 11,
        'module__num_outputs': 1,

    },

    'scoring': 'accuracy',

    'grid_search': {
        'param_grid': {
            'net__lr': [0.1, 0.2],
            'net__max_epochs': [500],
            'net__module__num_units': [10, 20],
        },
        'cv': 5,
        'verbose': 4,
        'n_jobs': -1,
    },
}
