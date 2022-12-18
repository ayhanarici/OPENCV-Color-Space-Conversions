# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 12:42:39 2022

@author: Ayhan
"""
import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX
org = (10, 20)
fontScale = .50
color = (255, 0, 0)
thickness = 1
imagelist=[]
image = cv2.imread('Istanbul.jpg')
procImage=image
image = cv2.resize(image, (0, 0), None, .3, .3)
procImage = cv2.resize(procImage, (0, 0), None, .3, .3)
image = cv2.putText(image, 'Original Picture', org, font,fontScale, color, thickness, cv2.LINE_AA)

#for details https://docs.opencv.org/3.4/d8/d01/group__imgproc__color__conversions.html
#RGB2YCrCb
YCrCb = cv2.cvtColor(procImage, cv2.COLOR_RGB2YCrCb)
#YCrCb_3_channel = cv2.cvtColor(YCrCb, cv2.COLOR_YCrCb2BGR)
YCrCb=cv2.putText(YCrCb, 'RGB2YCrCb', org, font,fontScale, color, thickness, cv2.LINE_AA)
horizontal = np.hstack((image, YCrCb))
imagelist.append(horizontal)
#RGB2GRAY
gray = cv2.cvtColor(procImage, cv2.COLOR_RGB2GRAY)
gray_3_channel = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
gray_3_channel=cv2.putText(gray_3_channel, 'RGB2GRAY', org, font,fontScale, color, thickness, cv2.LINE_AA)
horizontal = np.hstack((image, gray_3_channel))
imagelist.append(horizontal)
#RGB2RGBA
rgba = cv2.cvtColor(procImage, cv2.COLOR_RGB2RGBA)
rgba_3_channel = cv2.cvtColor(rgba, cv2.COLOR_RGBA2BGR)
rgba_3_channel=cv2.putText(rgba_3_channel, 'RGB2RGBA', org, font,fontScale, color, thickness, cv2.LINE_AA)
horizontal = np.hstack((image, rgba_3_channel))
imagelist.append(horizontal)
#RGB2HSV
hsv = cv2.cvtColor(procImage, cv2.COLOR_RGB2HSV)
hsv=cv2.putText(hsv, 'RGB2HSV', org, font,fontScale, color, thickness, cv2.LINE_AA)
horizontal = np.hstack((image, hsv))
imagelist.append(horizontal)
#RGB2Luv
luv = cv2.cvtColor(procImage, cv2.COLOR_RGB2Luv)
luv=cv2.putText(luv, 'RGB2Luv', org, font,fontScale, color, thickness, cv2.LINE_AA)
horizontal = np.hstack((image, luv))
imagelist.append(horizontal)
#RGB2HLS 
hls = cv2.cvtColor(procImage, cv2.COLOR_RGB2HLS)
hls=cv2.putText(hls, 'RGB2HLS', org, font,fontScale, color, thickness, cv2.LINE_AA)
horizontal = np.hstack((image, hls))
imagelist.append(horizontal)

vertical = np.concatenate([imagelist[x] for x in range(len(imagelist))])

cv2.imshow('OPENCV Color Space Conversions', vertical)
cv2.waitKey()
