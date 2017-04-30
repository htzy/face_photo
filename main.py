# coding:utf-8
from __future__ import print_function

import os
from glob import glob

import cv2


def detect(file_name):
    # 获取训练好的人脸的参数数据，这里直接从GitHub上使用默认值
    face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')

    # 读取图片
    image = cv2.imread(file_name)

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
        face_big = cv2.resize(face, (224, 224))
        face_small = cv2.resize(face, (32, 32))
        cv2.imwrite("results/224/" + os.path.basename(file_name).split('.')[0] + "_" + str(i) + ".jpg", face_big)
        cv2.imwrite("results/32/" + os.path.basename(file_name).split('.')[0] + "_" + str(i) + ".jpg", face_small)
        i += 1


if __name__ == '__main__':
    # if os.path.exists('results') is False:
    if not os.path.exists('results/224'):
        os.makedirs(r'results/224')
    if not os.path.exists('results/32'):
        os.makedirs(r'results/32')

    file_list = glob('images/liguangfu/*.jpg')
    for filename in file_list:
        detect(filename)
