# Raw Dataset containing items with their respective numerical scores 
dataset = [
    {"id": "item_1", "scores": [0.2, 0.4, 0.3]},
    {"id": "item_2", "scores": [0.8, 0.9, 0.7]},
    {"id": "item_3", "scores": [0.5, 0.5, 0.5]},
    {"id": "item_4", "scores": []}
]


def process_item_score(item_id, scores):
    # this function calculates avg score for an item and classifies it as high or low
    # Safety check: returns early with default values if the score list is empty to prevent a division-by-zero crash.
    if not len(scores):  # fixed: trigger the early return only when scores is EMPTY
        return {"id": item_id, "avg": 0.0, "label": "N/A"}
    avg = sum(scores) / len(scores)
    if avg > 0.5:
        label = "high"
    else:
        label = "low"
    return {"id": item_id, "avg": round(avg, 2), "label": label}


processed_results = []
for item in dataset:
    result = process_item_score(item["id"], item["scores"])
    processed_results.append(result)

for record in processed_results:
    print(record)

