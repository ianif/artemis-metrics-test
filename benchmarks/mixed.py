# benchmarks/mixed.py
import json

data = [
    {"latency": 1.5},
    {"memory": 500},
    {"cpu": 75}
]

with open("artemis_results.json", "w") as f:
    json.dump(data, f)
