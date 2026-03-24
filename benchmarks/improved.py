# benchmarks/improved.py
import json

data = [
    {"latency": 1.0, "memory": 450, "cpu": 70},
    {"latency": 1.1, "memory": 460, "cpu": 72}
]

with open("artemis_results.json", "w") as f:
    json.dump(data, f)
