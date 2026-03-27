# benchmarks/invalid.py
try:
    with open("artemis_results.json", "w") as f:
        f.write("{latency: 1.5")  # broken JSON
except (IOError, OSError) as e:
    print(f"Error writing to file: {e}")