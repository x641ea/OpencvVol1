# 使い方
# python translate.py
# 上記のコードをコンパイルする時にペースト

import numpy as np
import argparse
import imutils
import cv2

# 引数パーサーを構築し、引数を解析する
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="logo.png",
	help="path to the input image")
args = vars(ap.parse_args())

# 画像を読み込んで、画面に表示
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# 画像を右に25ピクセル、下に50ピクセル移動
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)

# ここで、画像を左に50ピクセル、上に90ピクセルずらしてみましょう。
# XとY方向にそれぞれ負の値を指定して、画像を左に50ピクセル、
# 上に90ピクセルずらす
M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)

# imutilsのヘルパー関数を使って、画像を100ピクセル変換
# さらに、縮小することができる
shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)
