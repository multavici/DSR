from palladium.config import get_config
from sklearn.datasets import fetch_openml

def main():
    config = get_config()
    persister = config['model_persister']
    model = persister.read()
    dataset = fetch_openml('wine-quality-red')
    for x, y in zip(dataset.feature_names, model.feature_importances_):
        print(x + ': ' + str(y))

if __name__ == '__main__':
    main()