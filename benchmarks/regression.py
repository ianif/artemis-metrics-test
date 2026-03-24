# benchmarks/regression.py
import json

data = [
    {"latency": 3.0, "memory": 600, "cpu": 90},
    {"latency": 3.2, "memory": 620, "cpu": 95}
]

with open("artemis_results.json", "w") as f:
    json.dump(data, f)
