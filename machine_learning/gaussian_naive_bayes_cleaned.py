
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


def main():

    

    
    iris = load_iris()

    
    X = iris["data"]  
    Y = iris["target"]
    x_train, x_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.3, random_state=1
    )

    
    NB_model = GaussianNB()
    NB_model.fit(x_train, y_train)

    
    plot_confusion_matrix(
        NB_model,
        x_test,
        y_test,
        display_labels=iris["target_names"],
        cmap="Blues",
        normalize="true",
    )
    plt.title("Normalized Confusion Matrix - IRIS Dataset")
    plt.show()


if __name__ == "__main__":
    main()
