import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd

def load_iris_data_set():
    iris = load_iris()
    irisFile = pd.read_csv("../data/Iris.csv")
    print(irisFile.info())
    print(irisFile.describe())
    return iris


def train_data_model(iris):
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=50, test_size=0.25)
    dtc_classifier = tree.DecisionTreeClassifier()
    dtc_classifier = dtc_classifier.fit(iris.data, iris.target)
    y_pred = dtc_classifier.predict(X_test)
    print("Train data accuracy:", accuracy_score(y_true=y_train, y_pred=dtc_classifier.predict(X_train)))
    print("Test data accuracy:", accuracy_score(y_true=y_test, y_pred=y_pred))
    return dtc_classifier


if __name__ == '__main__':
    iris_data = load_iris_data_set()
    print("")
    print(iris_data)
    print("iris dataset keys")
    print(iris_data.keys())
    print("iris dataset values")
    print(iris_data.get("data"))
    dtc_classifier_result = train_data_model(iris_data)
    tree.plot_tree(dtc_classifier_result)
    plt.title('IRIS Data set')
    plt.savefig("../data/iris_data_set_result.png");
    plt.show()
