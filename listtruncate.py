import numpy as np
import sys


def truncate_std_devs(t, std_devs_top_discarded, std_devs_bottom_discarded, selector=lambda i: i):
    std_dev = np.std(map(selector, t))
    mean = np.mean(map(selector, t))
    max_val = sys.maxint if std_devs_top_discarded is None else mean + (std_dev * std_devs_top_discarded)
    min_val = -sys.maxint - 1 if std_devs_top_discarded is None else mean - (std_dev * std_devs_bottom_discarded)
    return filter(lambda i: max_val >= selector(i) >= min_val, t)
