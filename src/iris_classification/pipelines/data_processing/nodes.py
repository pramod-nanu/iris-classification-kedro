"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 1.0.0
"""
# type: ignore
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def load_iris_data() -> pd.DataFrame:
    iris = load_iris()

    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df["target"] = iris.target
    print(df.head())

    return df

def split_data(df):
    X = df.drop("target", axis=1)
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test

def train_model(X_train,y_train):
    model = LogisticRegression()
    model.fit(X_train,y_train)
    return model

def evaluate_model(model,X_test,y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test,y_pred)
    print(f"Model Accuracy: {accuracy}")
    return accuracy
