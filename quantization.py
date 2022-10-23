import sys
import cv2 as cv
import numpy as np
from PIL import Image
from threading import Thread
import time

class quantization():
    def __init__(self):
        pass
    def __del__(self):
        cv.destroyAllWindows()

    def show(self,img,name = "Window"):
        cv.imshow(name,img)
        cv.waitKey(0)

    def K_means(self,img,K=8,n=10,eps=1.0):
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


class CustomThread(Thread):
    # constructor
    def __init__(self):
        # execute the base constructor
        Thread.__init__(self)
        # set a default value
        self.value = None
        self.foo = None

    def get_function(self,functio):
        self.foo = functio

    # function executed in a new thread
    def run(self):
        self.value = self.foo

if __name__ == "__main__":
    mod = int(input("podaj : 1-normal , 2-threads"))
    img = cv.imread('marriage.jpg')
    obj = quantization()
    obj2 = quantization()

    if mod ==2:
        t_start = time.time()
        thread = CustomThread()
        thread.get_function(obj.K_means(img,K=16,n=10))

        thread2 = CustomThread()
        thread2.get_function(obj2.K_means(img, K=16, n=10))
        # start the thread
        thread.start()
        thread2.start()
        # wait for the thread to finish
        thread.join()
        thread2.join()
        # get the value returned from the thread
        k_mean_img = thread.value
        k_mean_img2 = thread2.value
        #obj.show(k_mean_img,"k_mean_img")
        #obj.show(k_mean_img2,"k_mean_img2")
        t_stop = time.time()
    else:
        t_start = time.time()
        k_mean_img = obj.K_means(img, K=16, n=10)
        k_mean_img2 = obj2.K_means(img, K=16, n=10)
        t_stop = time.time()

    print(str((t_stop-t_start))+ "s")