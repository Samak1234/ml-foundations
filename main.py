# Raw Dataset containing items with their respective numerical scores
dataset = [
    {"id": "item_1", "scores": [0.2, 0.4, 0.3]},
    {"id": "item_2", "scores": [0.8, 0.9, 0.7]},
    {"id": "item_3", "scores": [0.5, 0.5, 0.5]},
    {"id": "item_4", "scores": []}
]


def process_item_score(item_id, scores):
    # Safety check: returns early if score list is empty
    if not len(scores):
        return {"id": item_id, "avg": 0.0, "label": "N/A"}

    avg = sum(scores) / len(scores)

    if avg > 0.5:
        label = "high"
    else:
        label = "low"

    return {
        "id": item_id,
        "avg": round(avg, 2),
        "label": label
    }


# Process dataset
processed_results = []

for item in dataset:
    result = process_item_score(
        item["id"],
        item["scores"]
    )

    processed_results.append(result)


# Print processed results
for record in processed_results:
    print(record)


# Import functions and test data from metrics.py
from metrics import (
    calculate_confusion_matrix,
    calculate_accuracy,
    y_true,
    y_pred
)


# Calculate confusion matrix
matrix = calculate_confusion_matrix(y_true, y_pred)

print(matrix)


# Calculate accuracy using TP, TN, FP and FN
accuracy = calculate_accuracy(
    matrix["TP"],
    matrix["TN"],
    matrix["FP"],
    matrix["FN"]
)

print(accuracy)