from dstoolbox.pipeline import PipelineY
import numpy as np
from sklearn.base import BaseEstimator
from sklearn.base import TransformerMixin
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from skorch import NeuralNetClassifier
import torch
from torch import nn
import torch.nn.functional as F


torch.manual_seed(7)


class MyModule(nn.Module):
    def __init__(self, num_inputs=4, num_units=10, num_outputs=3):
        super(MyModule, self).__init__()

        self.dense0 = nn.Linear(num_inputs, num_units)
        self.nonlin = F.relu
        self.dropout = nn.Dropout(0.5)
        self.dense1 = nn.Linear(num_units, 10)
        self.output = nn.Linear(10, num_outputs)

    def forward(self, X, **kwargs):
        X = self.nonlin(self.dense0(X))
        X = self.dropout(X)
        X = F.relu(self.dense1(X))
        X = F.softmax(self.output(X), dim=-1)
        return X


class Cast(BaseEstimator, TransformerMixin):
    def __init__(self, dtype):
        self.dtype = dtype

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        Xt = X.astype(self.dtype)
        return Xt


def create_pipeline(
    device='cpu',  # or 'cuda'
    max_epochs=50,
    lr=0.1,
    **kwargs
):
    return PipelineY([
        ('cast', Cast(np.float32)),
        ('scale', StandardScaler()),
        ('net', NeuralNetClassifier(
            MyModule,
            device=device,
            max_epochs=max_epochs,
            lr=lr,
            train_split=None,
            **kwargs,
        ))],
        y_transformer=LabelEncoder(),
        predict_use_inverse=True,
        )
