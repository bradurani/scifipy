__author__ = 'brad'
import numpy as np
import scifipy.histogramhelpers as hh


def print_dict(d):
    for key, value in d.iteritems():
        print "[%s] = %s" % (key, '{0:.10f}'.format(value))


def summarize(list_nums):
    print "n: %s" % len(list_nums)
    print "mean: %s" % np.mean(list_nums)
    print "variance: %s" % np.var(list_nums)
    print "std dev: %s" % np.std(list_nums)


def summarize_hist(hist):
    print("first bucket: %s" % min(hist.keys()))
    print("last bucket: %s" % max(hist.keys()))
    print("mean hist: %s" % hh.hist_mean(hist))
    print("var hist %s" % hh.hist_var(hist))
    print("std dev hist: %s" % hh.hist_std_dev(hist))
    print("Total val: %s" % sum(hist.values()))