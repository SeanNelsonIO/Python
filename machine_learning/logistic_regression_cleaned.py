
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets










def sigmoid_function(z):
    return 1 / (1 + np.exp(-z))


def cost_function(h, y):
    return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()


def log_likelihood(X, Y, weights):
    scores = np.dot(X, weights)
    return np.sum(Y * scores - np.log(1 + np.exp(scores)))



def logistic_reg(alpha, X, y, max_iterations=70000):
    theta = np.zeros(X.shape[1])

    for iterations in range(max_iterations):
        z = np.dot(X, theta)
        h = sigmoid_function(z)
        gradient = np.dot(X.T, h - y) / y.size
        theta = theta - alpha * gradient  
        z = np.dot(X, theta)
        h = sigmoid_function(z)
        J = cost_function(h, y)
        if iterations % 100 == 0:
            print(f"loss: {J} \t")  
    return theta




if __name__ == "__main__":
    iris = datasets.load_iris()
    X = iris.data[:, :2]
    y = (iris.target != 0) * 1

    alpha = 0.1
    theta = logistic_reg(alpha, X, y, max_iterations=70000)
    print("theta: ", theta)  

    def predict_prob(X):
        return sigmoid_function(
            np.dot(X, theta)
        )  

    plt.figure(figsize=(10, 6))
    plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color="b", label="0")
    plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color="r", label="1")
    (x1_min, x1_max) = (X[:, 0].min(), X[:, 0].max())
    (x2_min, x2_max) = (X[:, 1].min(), X[:, 1].max())
    (xx1, xx2) = np.meshgrid(np.linspace(x1_min, x1_max), np.linspace(x2_min, x2_max))
    grid = np.c_[xx1.ravel(), xx2.ravel()]
    probs = predict_prob(grid).reshape(xx1.shape)
    plt.contour(xx1, xx2, probs, [0.5], linewidths=1, colors="black")

    plt.legend()
    plt.show()
