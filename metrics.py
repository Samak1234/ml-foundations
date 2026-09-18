# Sample evaluation data
y_true = ["high", "high", "low", "high", "low"]

y_pred = ["high", "low", "low", "high", "high"]


def calculate_confusion_matrix(y_true, y_pred):

    # Start all counts at 0
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

        else:
            fp += 1

    return {
        "TP": tp,
        "FP": fp,
        "TN": tn,
        "FN": fn
    }


def calculate_accuracy(tp, tn, fp, fn):

    accuracy = (tp + tn) / (tp + tn + fp + fn)

    return accuracy

def calculate_precision(tp,fp):

    precision = tp/(tp+fp)

    return precision 


def calculate_recall(tp,fn):

    recall = tp/(tp+fn)

    return recall

def calculate_specificity(tn,fp):

    specificity = tn/(tn+fp)

    return specificity

def calculate_TPR(tp,fn):

    TPR = tp/(tp+fn)

    return TPR

def calculate_FPR(fp,tn):

    FPR = fp/(fp + tn)

    return FPR 


