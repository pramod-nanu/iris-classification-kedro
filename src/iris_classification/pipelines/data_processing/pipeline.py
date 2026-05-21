"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 1.0.0
"""

from kedro.pipeline import Pipeline, node
from .nodes import evaluate_model, load_iris_data,split_data,train_model,evaluate_model


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=load_iris_data,
                inputs=None,
                outputs="iris_data",
                name="load_iris_node",
            ),
            node(
                func=split_data,
                inputs = 'iris_data',
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
            node(
                func=train_model,
                inputs=["X_train","y_train"],
                outputs='trained_model',
                name="train_model_node",
            ),
            node(
                func=evaluate_model,
                inputs=["trained_model","X_test","y_test"],
                outputs="model_metrics",
                name="evaluate_model_node",
            )
        ]
    )
