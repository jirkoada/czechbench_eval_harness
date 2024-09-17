import numpy as np

def lang_diff(metrics, sizes, weight_by_size):
    """Computes the mean relative difference between two sets of metrics (even and odd elements of the input metrics array)
    """
    comparisons = np.array([metrics[::2], metrics[1::2]])
    mean_rel_diff = np.mean(np.abs(comparisons[0] - comparisons[1]) / (np.max(comparisons, axis=0)+1e-9))
    return mean_rel_diff