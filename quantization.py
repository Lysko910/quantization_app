import sys
import cv2 as cv
import numpy as np
from PIL import Image
from threading import Thread
import time


class quantization():
    def __init__(self, options, parameters):
        self.options = options
        self.parameters = parameters
        self.call_counter = 0

    def __del__(self):
        cv.destroyAllWindows()

    def show(self, img, name="Window"):
        cv.imshow(name, img)
        if self.call_counter < sum(self.options.values()):
            self.call_counter += 1
        else:
            cv.waitKey(0)

    def K_means(self, img, K=8, n=10, eps=1.0):
        Z = img.reshape((-1, 3))
        # convert to np.float32
        Z = np.float32(Z)

        # define criteria, number of clusters(K) and apply kmeans()
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, n, eps)
        K = 64
        ret, label, center = cv.kmeans(Z, K, None, criteria, n, cv.KMEANS_RANDOM_CENTERS)
        # Now convert back into uint8, and make original image
        center = np.uint8(center)
        res = center[label.flatten()]
        res2 = res.reshape((img.shape))
        return res2

    def wasz_algorytm1(self,img,param1,param2,param4):
        result_img = img
        # TO DO
        return result_img

    def wasz_algorytm2(self,img,param1,param2,param4):
        result_img = img
        # TO DO
        return result_img

    def wasz_algorytm3(self,img,param1,param2,param4):
        result_img = img
        # TO DO
        return result_img

    def wasz_algorytm4(self,img,param1,param2,param4):
        result_img = img
        # TO DO
        return result_img