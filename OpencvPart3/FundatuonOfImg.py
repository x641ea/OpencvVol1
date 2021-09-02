# 使い方
# python basic_drawing.py
# コンパイルしたい時に上記をターミナルへペースト

import numpy as np
import cv2

# キャンバスを300×300ピクセルの3つのチャンネルを持つ画像として初期化する
# (赤、緑、青の3つのチャンネルを持つ300×300ピクセルの画像として初期化される（背景は黒)
canvas = np.zeros((300, 300, 3), dtype="uint8")

# キャンバスの左上から右下まで、緑の線を描く
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# 右上から左下に向けて、太さ3ピクセルの赤い線を描く
red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# 10x10から始まって60x60で終わる、50x50ピクセルの緑の正方形を描く
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# 別の長方形（厚さ5ピクセルの赤い矩形）を描く
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# 最終的な四角形の描画（青く塗りつぶされている
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# キャンバスを空の配列として再初期化した後、
# 中心(x, y)座標を計算します。キャンバスの中心(x, y)座標を計算する
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

# 25ピクセルから150ピクセルまで、25ピクセル単位で半径を増やしていくループ
for r in range(0, 175, 25):
	# 現在の半径サイズで白い円を描く
	cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# キャンバスをもう一度初期化
canvas = np.zeros((300, 300, 3), dtype="uint8")

# ランダムに25個の円を描く
for i in range(0, 25):
	# 半径の大きさを5～200の間でランダムに生成し、
	# 色をランダムに生成し、キャンバス上のランダムな点を選んで円を描く
	radius = np.random.randint(5, high=200)
	color = np.random.randint(0, high=256, size=(3,)).tolist()
	pt = np.random.randint(0, high=300, size=(2,))

	# キャンバスにランダムな円を描く
	cv2.circle(canvas, tuple(pt), radius, color, -1)

# スクリーン上に表示
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
