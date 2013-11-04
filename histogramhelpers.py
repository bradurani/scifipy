import numpy as np

def hist_mean(hist):
    return sum(v * f for v,f in hist.items()) / total_observations(hist)
def hist_var(hist):
    mu = hist_mean(hist)
    return sum (((v - mu)**2) * f for v,f in hist.items()) / total_observations(hist)
def hist_std_dev(hist):
    return np.sqrt(hist_var(hist))
def total_observations(hist):
    return sum(f for _,f in hist.items())