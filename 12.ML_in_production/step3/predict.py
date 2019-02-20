import sys

from palladium.config import get_config


def predict(features):
    # Get hold of the Palladium configuration in config.py:
    config = get_config()
    # Use the model_persister to load the trained model:
    model = config['model_persister'].read()
    # From here on, it's plain scikit-learn:
    result = model.predict_proba([features])[0]
    for class_, proba in zip(model.classes_, result):
        print("{}: {:.1f}%".format(class_, proba*100))


if __name__ == '__main__':
    predict([float(v) for v in sys.argv[1:]])
