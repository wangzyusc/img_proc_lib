import cv2 as cv
import numpy as np
import sys

path = "./"
prefix = "IMG_"
suffix = ".JPG"
text = '''3819
3820
3821
3822
3823
'''

def mean():
	thresholds = range(100, 210, 10)
	res = [np.zeros((h, w, 3), np.float32) for _ in thresholds]
	ratio = float(1) / len(files)
	for name in files:
	    img = cv.imread(path + name)
	    for index, threshold in enumerate(thresholds):
	    	mask = (img >= threshold)
	    	res[index] += ratio * img + mask * ratio * img
	for index, img in enumerate(res):
		cv.imwrite("./res-mean-" + str(thresholds[index]) + ".JPG", img)

def maxpool():
	res = np.zeros((h, w, 3), np.uint8)
	for name in files:
		img = cv.imread(path + name)
		res = cv.max(res, img)
	cv.imwrite("./res-maxpool.JPG", res)

if __name__ == "__main__":
	files = [prefix + line[0:4] + suffix for line in text.splitlines()]
	print files
	img = cv.imread(path + files[0])
	h, w = img.shape[:2]
	if len(sys.argv) < 2:
		print 'python stack.py [ mean | maxpool ]'
	elif sys.argv[1] == 'mean':
		mean()
	elif sys.argv[1] == 'maxpool':
		maxpool()
	else:
		print 'python stack.py [ mean | maxpool ]'