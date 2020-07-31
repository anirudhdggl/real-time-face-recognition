from PIL import Image
import sys
import numpy as np

def makeHist(twod, height, width):

	pattern = []

	# print("{}: {}".format(height,width))

	# for x in twod:
	# 	print(x)

	for i in range(1, height - 1):
		prev = twod[i - 1]
		curr = twod[i]
		nextR = twod[i + 1]
		for j in range(1, width - 1):
			# print(j)
			threshold = curr[j]
			val = 0
			val = val + 1 if threshold <= prev[j - 1] else val
			val = (val * 2) + 1 if threshold <= prev[j] else val * 2
			val = (val * 2) + 1 if threshold <= prev[j + 1] else val * 2
			val = (val * 2) + 1 if threshold <= curr[j - 1] else val * 2
			val = (val * 2) + 1 if threshold <= curr[j + 1] else val * 2
			val = (val * 2) + 1 if threshold <= nextR[j - 1] else val * 2
			val = (val * 2) + 1 if threshold <= nextR[j] else val * 2
			val = (val * 2) + 1 if threshold <= nextR[j + 1] else val * 2
			pattern.append(val)

	histogram = [0] * 256

	for i in pattern:
		histogram[i] += 1
	
	return histogram
