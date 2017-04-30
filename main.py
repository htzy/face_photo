# coding:utf-8
from __future__ import print_function

import os
from glob import glob

import cv2


def detect(filename):
    # 获取训练好的人脸的参数数据，这里直接从GitHub上使用默认值
    face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')

    # 读取图片
    image = cv2.imread(filename)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 探测图片中的人脸
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.15,
        minNeighbors=5,
        minSize=(5, 5),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    print("发现{0}个人脸!".format(len(faces)))

    for i, (x, y, w, h) in enumerate(faces):
        face = image[y: y + h, x: x + w, :]
        face = cv2.resize(face, (96, 96))
        cv2.imwrite("results/" + os.path.basename(filename).split('.')[0] + "_" + str(i) + ".jpg", face)
        i += 1


if __name__ == '__main__':
    if os.path.exists('results') is False:
        os.mkdir('results')

    file_list = glob('images/liguangfu/*.jpg')
    for filename in file_list:
        detect(filename)
