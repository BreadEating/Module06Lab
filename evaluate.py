from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

# Load the same dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split data - use same random_state for consistency
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Load the trained model
model_path = os.path.join("artifacts", "model.pkl")
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}. Run train.py first.")

clf = joblib.load(model_path)

# Make predictions on test data
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Print results
print(f"Model Accuracy: {accuracy:.4f}")
print("\nDetailed Classification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Save accuracy to file for threshold checking
results_path = os.path.join("artifacts", "evaluation_results.txt")
with open(results_path, "w") as f:
    f.write(f"accuracy: {accuracy:.4f}\n")

print(f"\nResults saved to {results_path}")