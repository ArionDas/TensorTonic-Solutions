import numpy as np

def f1_micro(y_true, y_pred):
    y_true = np.asarray(y_true).ravel()
    y_pred = np.asarray(y_pred).ravel()

    labels = np.unique(np.concatenate([y_true, y_pred]))

    tp = fp = fn = 0

    for label in labels:
        tp += np.sum((y_true == label) & (y_pred == label))
        fp += np.sum((y_true != label) & (y_pred == label))
        fn += np.sum((y_true == label) & (y_pred != label))

    return 2 * tp / (2 * tp + fp + fn) if (tp + fp + fn) > 0 else 0.0