import json
from pathlib import Path


def get_model_performance():

    performance_file = (
        Path(__file__).resolve().parent.parent
        / "model_performance.json"
    )

    with open(performance_file, "r") as file:
        performance = json.load(file)

    return performance