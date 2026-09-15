# Sample evaluation data
y_true = ["high", "high", "low",  "high", "low"]
y_pred = ["high", "low",  "low",  "high", "high"]

def calculate_confusion_matrix(y_true, y_pred):
    tp = fp = tn = fn = 0
    for true, pred in zip(y_true, y_pred):
        if true == "high" and pred == "high":
            tp += 1
        elif true == "low" and pred == "low":
            tn += 1
        elif true == "high" and pred == "low":
            fn += 1
        else:
            fp += 1

    return {"TP": tp, "FP": fp, "TN": tn, "FN": fn}