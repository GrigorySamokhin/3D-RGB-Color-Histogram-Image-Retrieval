import numpy as np

class Searcher:
	def __init__(self, index):
		# store our index of images
		self.index = index

	def search(self, queryFeatures):
		# initialize our dictionary of results
		results = {}
		# loop over the index
		for (k, features) in self.index.items():
			d = self.chi2_distance(features, queryFeatures)
			results[k] = d
		# sort our results, so that the smaller distances (i.e. the
		# more relevant images are at the front of the list)
		results = sorted([(v, k) for (k, v) in results.items()])
		# return our results
		return results

	def chi2_distance(self, histA, histB, eps = 1e-10):
		# compute the chi-squared distance
		d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
			for (a, b) in zip(histA, histB)])
		return d