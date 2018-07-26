# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/07/25 07:14'

import cv2
import numpy as np
from matplotlib import pyplot as plt


def plot_hist(img):
    """
    ヒストグラムを描写
    :param img:
    :return:
    """
    img_hist = np.histogram(img.ravel(), 256, [0, 256])
    hist = img_hist[0]
    plt.bar(np.arange(256), hist)
    plt.show()


def main():
    img = cv2.imread("paiza images/000.png", cv2.IMREAD_GRAYSCALE)
    cv2.imwrite("gray000.png", img)
    print(img)
    print(img.shape)
    print(img.ravel().shape)

    plot_hist(cv2.imread("paiza images/000.png", cv2.IMREAD_GRAYSCALE))
    plot_hist(cv2.imread("paiza images/001.png", cv2.IMREAD_GRAYSCALE))
    plot_hist(cv2.imread("paiza images/002.png", cv2.IMREAD_GRAYSCALE))


if __name__ == '__main__':
    main()