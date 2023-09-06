import json
import os
from bson import json_util  # pip install bson


def writeAJson(data, name: str):
    parsed_json = json.loads(json_util.dumps(data))

    if not os.path.isdir("./logs"):
        os.makedirs("./logs")

    with open(f"./logs/{name}.json", "w") as json_file:
        json.dump(parsed_json, json_file, indent=4, separators=(",", ": "))
