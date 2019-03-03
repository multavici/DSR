from flask import Flask, jsonify, request
import pandas as pd
from sklearn.externals import joblib
import os

app = Flask(__name__)
classifier = joblib.load('../model/model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    basket = request.json['basket']
    zipCode = request.json['zipCode']
    totalAmount = request.json['totalAmount']
    p = probability(basket, zipCode, totalAmount)

    return jsonify({'probability': p}), 201

def probability(basket, zipCode, totalAmount):
    print("Processing request: {},{},{}".format(basket, zipCode, totalAmount))

    df = pd.DataFrame(data={'basket': [basket], 'totalAmount': [totalAmount], 
                  'zipCode': [zipCode]})

    df['c_0'] = df.basket.map(lambda x: x.count(0))
    df['c_1'] = df.basket.map(lambda x: x.count(1))
    df['c_2'] = df.basket.map(lambda x: x.count(2))
    df['c_3'] = df.basket.map(lambda x: x.count(3))
    df['c_4'] = df.basket.map(lambda x: x.count(4))

    df["zipCode"] = df["zipCode"].astype('category',categories=[i for i in list(range(1000,10000))])
    dummies = pd.get_dummies(df.zipCode)
    df2 = pd.concat([df, dummies], axis=1)
    df3 = df2.drop(["basket", "zipCode"], axis=1)
    
    return classifier.predict_proba(df3)[0][1]

if __name__ == "__main__":
    app.run()