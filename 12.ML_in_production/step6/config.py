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
        #'__factory__': 'model.create_pipeline',
        '__factory__': 'sklearn.ensemble.RandomForestRegressor',
        # YOUR CODE HERE:
        #
        # The new dataset has a different number of inputs and
        # outputs.  Adjust these parameters:
        #
        # 'module__num_inputs': 4,   # Number of features
        # 'module__num_outputs': 3,  # Number of classes
        #'module__num_inputs': 11,
        #'module__num_outputs': 1,
        #'n_estimators': 64,
        #'min_samples_split': 0.02,

    },

    'scoring': 'neg_mean_absolute_error',

    'grid_search': {
        'param_grid': {
            #'net__lr': [0.1],
            #'net__max_epochs': [200],
            #'net__module__num_units': [20],
            'max_depth': [4, 5, 6],
            #'n_estimators': [50, 100, 150],
            #'criterion': ['mae'],
            'min_samples_split': [2, 3]
        },
        #'cv': 5,
        #'verbose': 4,
        #'n_jobs': -1,
    },
}
