## Author: Yash Srivastava
## Date of last update: 19/02/2019

import cv2
import numpy as np
import csv

clicks = [['x', 'y']]
originC = []
XC = []
YC = []
origin = False
plots = False
axisX = False
axisY = False

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if origin == True:
            cv2.circle(img,(x,y),5,(0,255,0),2)
            originC.extend((x, y))
        elif axisX == True:
            cv2.circle(img,(x,y),5,(255,0,0),2)
            XC.extend((x, y))
            print("Enter the length of x-axis")
            xl = float(input())
            print("Enter the zero offset for x axis")
            global x_zero_offset
            x_zero_offset = float(input())
            global x_PixLength
            x_PixLength = float(euclidean(originC[0], originC[1], XC[0], XC[1]))
            global x_pixToUnitRatio
            x_pixToUnitRatio = float(x_PixLength)/float(xl)
            global cosine
            cosine = (XC[0]-originC[0])/x_PixLength
        elif axisY == True:
            cv2.circle(img,(x,y),5,(255,0,0),2)
            YC.extend((x, y))
            print("Enter the length of y-axis")
            yl = float(input())
            print("Enter the zero offset for y axis")
            global y_zero_offset
            y_zero_offset = float(input())
            global y_PixLength
            y_PixLength = float(euclidean(originC[0], originC[1], YC[0], YC[1]))
            global y_pixToUnitRatio
            y_pixToUnitRatio = float(y_PixLength)/float(yl)
        elif plots == True:
            cv2.circle(img,(x,y),5,(0,0,255),2)
            clicks.append(coordinate_calculator(x, y))

def euclidean(x1, y1, x2, y2):
    return np.sqrt((x2-x1)**2 + (y2-y1)**2)

def x_axis(x):
    return ((XC[1]-originC[1])/abs(XC[0]-originC[0]))*abs(x-originC[0]) + originC[1]

def y_axis(y):
    return ((YC[0]-originC[0])/abs(YC[1]-originC[1]))*abs(y-originC[1]) + originC[0]

def x_pixToUnit(pixels):
    return float(pixels)/float(x_pixToUnitRatio)

def y_pixToUnit(pixels):
    return float(pixels)/float(y_pixToUnitRatio)

def coordinate_calculator(x, y):
    eu_x = euclidean(x, y, y_axis(y), y)
    y_unit = y_pixToUnit(euclidean(x, y, x, x_axis(x))*cosine)+y_zero_offset
    x_unit = x_pixToUnit(euclidean(x, y, y_axis(y), y)*cosine)+x_zero_offset
    return [x_unit, y_unit]

print("Enter image name with extension")
img_file = input()
img = cv2.imread("graphs\\"+img_file)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord("o"):
        origin = True
        plots = False
        axisX = False
        axisY = False
    elif k == ord("x"):
        origin = False
        plots = False
        axisX = True
        axisY = False
    elif k == ord("y"):
        origin = False
        plots = False
        axisX = False
        axisY = True
    elif k == ord("p"):
        origin = False
        plots = True
        axisX = False
        axisY = False
    elif k == ord("s"):
        cv2.imwrite("plots\\"+img_file+"_plot.png", img)
        print("Plot image saved!")
    elif k == ord("f"):
        break
cv2.destroyAllWindows()

print("Enter the file name to which you need to save data")
F_name = input()

with open("plotDataFiles\\"+F_name+'.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(clicks)

csvFile.close()
print("done!")
