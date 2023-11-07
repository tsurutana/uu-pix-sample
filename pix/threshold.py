import cv2
from django.conf import settings
import os

def getThresholdImage(fileurl):
    src, dst = getFileNames(fileurl)
    img = cv2.imread(str(settings.MEDIA_ROOT) + src, cv2.IMREAD_GRAYSCALE)
    result = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    cv2.imwrite(str(settings.MEDIA_ROOT) + dst, result)
    return settings.MEDIA_URL + dst

def getFileNames(fileurl): # ファイルのURLから「ファイル名」と「-copyを付けたファイル名」を返す
    src = os.path.basename(fileurl)
    name, ext = os.path.splitext(src)
    dst = name + '-copy' + ext
    return src, dst
