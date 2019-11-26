# import the packages
import cv2
import numpy as np
import argparse

# argument parser construction
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--source", required=True, help="Path to Source Image")
ap.add_argument("-t", "--target", required=True, help="Path to Target Image")
args = vars(ap.parse_args())

def image_stats(image):
    (l, a, b) = cv2.split(image)

    (lMean, lStd) = (l.mean(), l.std())
    (aMean, aStd) = (a.mean(), a.std())
    (bMean, bStd) = (b.mean(), b.std())

    return (lMean, lStd, aMean, aStd, bMean, bStd)

def color_transfer(x, y):
    # compute the source and target images in to LAB format
    source = cv2.cvtColor(x, cv2.COLOR_BGR2LAB).astype("float32")
    target = cv2.cvtColor(y, cv2.COLOR_BGR2LAB).astype("float32")

    # compute color statistics for the source and target images
    (lMeanSrc, lStdSrc, aMeanSrc, aStdSrc, bMeanSrc, bStdSrc) = image_stats(source)
    (lMeanTar, lStdTar, aMeanTar, aStdTar, bMeanTar, bStdTar) = image_stats(target)

    # subsctract the mean from the target image
    (l, a, b) = cv2.split(target)
    l -= lMeanTar
    a -= aMeanTar
    b -= bMeanTar

    # scale by standard deviation
    l = (lStdTar / lStdSrc) * l
    a = (aStdTar / aStdSrc) * a
    b = (bStdTar / bStdSrc) * b

    # add the source mean
    l += lMeanSrc
    a += aMeanSrc
    b += bMeanSrc

    # clip the pixel intensities to [0, 255] if they fall outside this range
    l = np.clip(l, 0, 255)
    a = np.clip(a, 0, 255)
    b = np.clip(b, 0, 255)

    # merge the channels together and convert it back to BGR color space
    output = cv2.merge([l,a,b])
    output = cv2.cvtColor(output.astype("uint8"), cv2.COLOR_LAB2BGR)

    return output


x = cv2.imread(args["source"])
y = cv2.imread(args["target"])
transfer_image = color_transfer(x, y)
cv2.imshow("Transferred Image", transfer_image)
cv2.waitKey(0)