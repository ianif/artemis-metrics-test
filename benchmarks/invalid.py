# benchmarks/invalid.py
with open("artemis_results.json", "w") as f:
    f.write("{latency: 1.5")  # broken JSON
