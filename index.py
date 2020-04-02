from rgbhistogram import RGBHistogram
import argparse
import pickle
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
args = vars(ap.parse_args())

index = {}
desc = RGBHistogram([16, 16, 16])
for imagePath in os.listdir(args["dataset"]):
	# load the image, describe it using our RGB histogram
	# descriptor, and update the index
	image = cv2.imread(os.path.join(args["dataset"], imagePath))
	image = cv2.resize(image, (166, 400))
	features = desc.describe(image)
	index[imagePath] = features

f = open(args["index"], "wb")
f.write(pickle.dumps(index))
f.close()
# show how many images we indexed
print("[INFO] done...indexed {} images".format(len(index)))