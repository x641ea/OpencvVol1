# 使い方
# python image_drawing.py
# コンパイルしたい時に上記のコードをターミナルにペースト

import argparse
import cv2

# 引数パーサーを構築し、引数を解析する
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="samplepic.png",
	help="path to the input image")
args = vars(ap.parse_args())

# 入力画像をディスクからロード
image = cv2.imread(args["image"])

# 顔の周りには円を、目の周りには2つの塗りつぶした円を、口の上には長方形を描く
cv2.circle(image, (190, 160), 100, (0, 0, 255), 2)
cv2.circle(image, (140, 114), 10, (0, 0, 255), -1)
cv2.circle(image, (220, 114), 10, (0, 0, 255), -1)
cv2.rectangle(image, (154, 170), (220, 210), (0, 0, 160), -1)

# スクリーン上に出力
cv2.imshow("Output", image)
cv2.waitKey(0)
