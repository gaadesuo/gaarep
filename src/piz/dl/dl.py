# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/07/29 04:04'


import cv2
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def main():
    targets_date = pd.read_csv(r"C:\Users\gaa\Documents\NetBeansProjects\gaarep\PythonProject\src\piz\dl\y_classified.csv")
    # print(targets_date["Kirishima"])

    images = []
    for i in range(100):
        file = (r"C:\Users\gaa\Documents\NetBeansProjects\gaarep\PythonProject\src\piz\dl\paiza images/%03d.png"%(i))
        img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        images.append(img)

    images_date = np.empty((100, len(images[0].ravel())), int)
    for i in range(100):
        images_date[i] = np.array([images[i].ravel()])
    # print(images_date.shape)

    x_train, x_test, y_train, y_test = train_test_split(images_date, targets_date["Kirishima"], random_state=0)
    print(x_train)
    #print(x_test)
    #print(y_train)
    #print(y_test)


if __name__ == '__main__':
    main()