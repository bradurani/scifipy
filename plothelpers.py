__author__ = 'Brad Urani'

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import scifipy.histogramhelpers as hh

class PlotHelpers(object):
    def __init__(self):
        pass

    def histogram_with_pdf(self, hist):
        mu = hh.hist_mean(hist)
        std_dev = hh.hist_std_dev(hist)
        width_list = self.width_list(hist)
        plt.bar(hist.keys(), hist.values(), width_list, facecolor='g', alpha=0.75)
        x = np.linspace(min(hist.keys()), max(hist.keys()), 1000)
        plt.plot(x, mlab.normpdf(x, mu, std_dev) * np.mean(width_list), linewidth=5, c='r')
        plt.grid(True)
        plt.show()
        return mu, std_dev


    def double_histogram(self, hist1, hist2):
        plt.bar(hist1.keys(), hist1.values(), self.width_list(hist1), facecolor='g', alpha=0.5)
        plt.bar(hist2.keys(), hist2.values(), self.width_list(hist2), facecolor='b', alpha=0.5)
        plt.grid(True)
        plt.show()

    def width_list(self, hist):
        bins = hist.keys()
        diffs = [bins[n]-bins[n-1] for n in range(1, len(bins))]
        diffs.append(np.mean(diffs)) #add one for the last bar
        return diffs

    def histogram(self, hist):
        plt.bar(hist.keys(), hist.values(), self.width_list(hist), facecolor='g', alpha=0.5)
        plt.grid(True)
        plt.show()