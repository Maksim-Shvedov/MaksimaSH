# TODO решите задачу
import json
def task() -> float:
    name_of_file = "input.json"
    with open(name_of_file) as f:
        data_of_json = json.load(f)
    result = sum([item["score"] * item["weight"] for item in data_of_json])
    return round(result, 3)
print(task())
