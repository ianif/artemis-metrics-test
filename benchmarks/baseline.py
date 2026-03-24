# benchmarks/baseline.py
import json

data = [
    {"latency": 2.0, "memory": 500, "cpu": 80},
    {"latency": 2.1, "memory": 510, "cpu": 82}
]

with open("artemis_results.json", "w") as f:
    json.dump(data, f)
