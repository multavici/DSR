import numpy as np


def sigmoid(Z):
    return 1/(1+np.exp(-Z))


def sigmoid_backward(dA, Z):
    sig = sigmoid(Z)
    # if np.any(sig == 1.0): 
    #     print(sig)
    #     print("1 spotted")
    #     sig -= np.finfo(float).eps
    #     print("bla", sig)
    #     print(np.any(sig == 1.0))
    # if np.any(sig == 0.0): 
    #     print("0 spotted")
    #     sig += np.finfo(float).eps
    #     print(sig)
    return dA * sig * (1 - sig)


def relu(Z):
    # WORKSHOP #5: code the ReLU activation function
    # if np.any(Z == 1.0): 
    #     print("1 spotted")
    #     Z -= np.finfo(float).eps
    #     print(Z)
    # if np.any(Z == 0.0): 
    #     print("0 spotted")
    #     Z += np.finfo(float).eps
    return Z * (Z > 0)


def relu_backward(dA, Z):
    # WORKSHOP #5: code the ReLU activation function
    # if np.any(Z == 1.0): 
    #     print("1 spotted")
    #     Z -= np.finfo(float).eps
    #     print(Z)
    # if np.any(Z == 0.0): 
    #     print("0 spotted")
    #     Z += np.finfo(float).eps
    return dA * (Z > 0)
