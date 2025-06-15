import sys

# Read accuracy from evaluation results
with open("artifacts/evaluation_results.txt", "r") as f:
    line = f.readline().strip()
    accuracy = float(line.split(":")[1].strip())

# Check if accuracy meets threshold
threshold = 0.80
if accuracy >= threshold:
    print(f"PASS: Accuracy {accuracy:.4f} meets threshold {threshold}")
    sys.exit(0)
else:
    print(f"FAIL: Accuracy {accuracy:.4f} below threshold {threshold}")
    sys.exit(1)