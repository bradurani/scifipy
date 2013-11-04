import scipy.stats
import numpy as np
import collections

class HistogramFactory(object):

    def __init__(self):
        return

    def normal_random_rounded_histogram(self, mean, std_dev, bin_width, sample_size=1000000):
        """
        @param std_dev:
        @param bin_width:
        @param sample_size:
        @return:
        """
        experimental = np.random.normal(mean, std_dev, sample_size)
        rounded = map(lambda i: int(i), experimental)
        bins = range(min(rounded), max(rounded) + bin_width * 2, bin_width)
        histogram, bin_edges = scipy.histogram(rounded, bins)
        return self._sorted_dict(zip(bin_edges, histogram))

    def sliced_histogram(self, slice_bucket, hist):
        if slice_bucket > max(hist.keys()):
            raise "current bucket is passed the end of your model"
        ret = filter(lambda (k, v): k > slice_bucket, hist.items())
        return self._sorted_dict(ret)

    def pmf(self, hist):
        """Returns a PMF or probability mass function
        Args:
            hist: a pre-generated histogram.
        """
        total = sum(hist.values())
        factor = 1.0 / total
        norm_hist = map(lambda i: (i[0], i[1] * factor), hist.items())
        return self._sorted_dict(norm_hist)

    @staticmethod
    def _sorted_dict(tuple_list):
        return collections.OrderedDict(sorted(tuple_list))