# Sample evaluation data
y_true = ["high", "high", "low", "high", "low"]

y_pred = ["high", "low", "low", "high", "high"]


def calculate_confusion_matrix(y_true, y_pred):

    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have the same length")

    tp = 0
    tn = 0
    fp = 0
    fn = 0

    for true, pred in zip(y_true, y_pred):

        if true == "high" and pred == "high":
            tp += 1

        elif true == "low" and pred == "low":
            tn += 1

        elif true == "high" and pred == "low":
            fn += 1

        elif true == "low" and pred == "high":
            fp += 1

        else:
            raise ValueError("Labels must be 'high' or 'low'")

    return {
        "TP": tp,
        "FP": fp,
        "TN": tn,
        "FN": fn
    }


def calculate_accuracy(tp, tn, fp, fn):

    total = tp + tn + fp + fn

    if total == 0:
        return 0.0

    return (tp + tn) / total


def calculate_precision(tp, fp):

    if tp + fp == 0:
        return 0.0

    return tp / (tp + fp)


def calculate_recall(tp, fn):

    if tp + fn == 0:
        return 0.0

    return tp / (tp + fn)


def calculate_f1_score(precision, recall):

    if precision + recall == 0:
        return 0.0

    return 2 * precision * recall / (precision + recall)


def calculate_specificity(tn, fp):

    if tn + fp == 0:
        return 0.0

    return tn / (tn + fp)


def calculate_TPR(tp, fn):

    if tp + fn == 0:
        return 0.0

    return tp / (tp + fn)


def calculate_FPR(fp, tn):

    if fp + tn == 0:
        return 0.0

    return fp / (fp + tn)


def calculate_FNR(fn, tp):

    if fn + tp == 0:
        return 0.0

    return fn / (fn + tp)


def calculate_all_metrics(matrix):

    tp = matrix["TP"]
    fp = matrix["FP"]
    tn = matrix["TN"]
    fn = matrix["FN"]

    precision = calculate_precision(tp, fp)
    recall = calculate_recall(tp, fn)

    return {
        "accuracy": calculate_accuracy(tp, tn, fp, fn),
        "precision": precision,
        "recall": recall,
        "f1_score": calculate_f1_score(precision, recall),
        "specificity": calculate_specificity(tn, fp),
        "TPR": calculate_TPR(tp, fn),
        "FPR": calculate_FPR(fp, tn),
        "FNR": calculate_FNR(fn, tp)
    }