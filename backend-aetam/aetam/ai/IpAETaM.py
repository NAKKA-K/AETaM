# -*- coding: utf-8 -*-
import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt

class IpAETaM:
    dump = []
    def __init__(self, cups):#引数は画像データ
        self.cups = cups
        self.width = 600
        self.height = 400
        self.ColorProcess()

    def ColorProcess(self):#料理色処理
        circles, cups_circles = self.__ImageProcess()
        blue, green, red, bc, gc, rc, cc, maxcolor = 0, 0, 0, 0, 0, 0, 0, [0, 0]
        if circles is not None and len(circles) > 0:
            circles = circles[0]
            cups_color = [cups_circles] * circles.shape[0]
            for (x, y, r) in circles:#料理検出
                x, y, r = int(x), int(y), int(r)
                yy, xx = np.ogrid[0:self.height, 0:self.width]
                matrix = (yy - y) ** 2 + (xx - x) ** 2 > r * r
                temp_cups_circles = np.copy(cups_circles)
                temp_cups_circles[matrix] = 0
                cups_color[cc] = temp_cups_circles
                cc += 1
            matrix = cups_color[0] == 0
            for cc in range(1, circles.shape[0]):#料理色抽出
                matrix = (matrix == True) & (cups_color[cc] == 0)
            cups_circles[matrix] = 0
            for x in range(0, self.width):#色取得
                for y in range(0, self.height):
                    if (cups_circles[y, x, 0] != 0) & (cups_circles[y, x, 1] != 0) & (cups_circles[y, x, 2] != 0):
                        if (cups_circles[y, x, 0] >= cups_circles[y, x, 1]) & (cups_circles[y, x, 0] >= cups_circles[y, x, 2]):
                            blue += cups_circles[y, x, 0]
                            bc += 1
                        elif (cups_circles[y, x, 1] >= cups_circles[y, x, 0]) & (cups_circles[y, x, 1] >= cups_circles[y, x, 2]):
                            green += cups_circles[y, x, 1]
                            gc += 1
                        elif (cups_circles[y, x, 2] >= cups_circles[y, x, 0]) & (cups_circles[y, x, 2] >= cups_circles[y, x, 1]):
                            red += cups_circles[y, x, 2]
                            rc += 1
            blue, green, red = blue // bc, green // gc, red // rc#色平均
            if green > blue:
                maxcolor = [green, -1]
            else:
                maxcolor[0] = blue
            if red > maxcolor[0]:
                maxcolor[1] = 1
            self.dump.append(maxcolor[1])

        elif not circles:
            print('円を検出できませんでした')

    def __ImageProcess(self):#画像加工
        self.cups = cv2.resize(self.cups,(self.width, self.height), interpolation = cv2.INTER_LANCZOS4)#リサイズ
        cups_preprocessed  = cv2.cvtColor(cv2.GaussianBlur(self.cups, (5, 5), 0), cv2.COLOR_BGR2GRAY)#加重平均グレスケ
        cups_edges = cv2.Canny(cups_preprocessed, threshold1=80, threshold2=80)#エッジ
        circles = cv2.HoughCircles(cups_edges, cv2.HOUGH_GRADIENT, dp=1.5, minDist=80, minRadius=80, maxRadius=140)
        cups_circles = np.copy(self.cups)
        return circles, cups_circles

#cups = cv2.imread('images/cups4.jpg')#画像読み込み
#print(IpAETaM(cups).dump)
