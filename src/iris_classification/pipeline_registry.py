"""Project pipelines."""
# from __future__ import annotations

# from kedro.framework.project import find_pipelines
# from kedro.pipeline import Pipeline


# def register_pipelines() -> dict[str, Pipeline]:
#     """Register the project's pipelines.

#     Returns:
#         A mapping from pipeline names to ``Pipeline`` objects.
#     """
#     pipelines = find_pipelines()
#     pipelines["__default__"] = sum(pipelines.values())
#     return pipelines

from kedro.pipeline import Pipeline
from iris_classification.pipelines.data_processing.pipeline import create_pipeline


def register_pipelines() -> dict[str, Pipeline]:
    data_processing_pipeline = create_pipeline()

    return {
        "__default__": data_processing_pipeline,
        "data_processing": data_processing_pipeline,
    }
