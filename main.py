#Raw Dataset containing items with their respective numerical scores 
dataset = [
    {"id": "item_1", "scores": [0.2, 0.4, 0.3]},
    {"id": "item_2", "scores": [0.8, 0.9, 0.7]},
    {"id": "item_3", "scores": [0.5, 0.5, 0.5]},
]


def process_item_score(item_id, scores):
    #this function calculates avg score for an item and classifies it as high or low
    avg = sum(scores) / len(scores)
    if avg > 0.5:
        label = "high"
    else:
        label = "low"
    return {"id": item_id, "avg": round(avg, 2), "label": label}

processed_results = []
for item in dataset:
    result = process_item_score(item["id"], item["scores"])
    print(result)


