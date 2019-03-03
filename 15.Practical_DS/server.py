from flask import Flask, jsonify, request
import pickle
import pandas as pd
from joblib import load
import time
import json

app = Flask(__name__)
model = load('logreg.joblib')
START_TIME = 0
with open('imputations.json', 'r') as f:
    imputations = json.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    START_TIME = time.time()
    basket = request.json['basket']
    zipCode = request.json['zipCode']
    totalAmount = request.json['totalAmount']
    p = probability(
        basket or imputations['basket'], 
        zipCode or imputations['zipCode'], 
        totalAmount or imputations['totalAmount'] 
    )
    log = {
        'request': {
            'basket': basket,
            'zipCode': zipCode,
            'totalAmount': totalAmount
        },
        'response': p
    }
    with open('log.txt', 'a') as f:
        f.write(json.dumps(log) + '\n')
    print('time: ', time.time() - START_TIME)
    return jsonify({'probability': p}), 201

def probability(basket, zipCode, totalAmount):
    print("Processing request: {},{},{}".format(basket, zipCode, totalAmount))

    df = pd.DataFrame([(basket, zipCode, totalAmount)], columns=['basket', 'zipCode', 'totalAmount'])
    
    for i in range(6):
        df['cat' + str(i)] = df.basket.apply(lambda x: x.count(i))
    
    #df["zipCode"] = df["zipCode"].astype('category',categories=list(range(1000,10000)))
    df["zipCode"] = pd.Categorical(df["zipCode"], categories=list(range(1000,10000)))
    dummies = pd.get_dummies(df.zipCode, prefix="zip")
    
    df = pd.concat([df, dummies], axis=1)
    df = df.drop(['basket', 'zipCode'], 1)
    return model.predict_proba(df)[0][1]

if __name__ == "__main__":
	app.run()