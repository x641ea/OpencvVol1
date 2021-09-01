# 使い方
# python loadimage.py --image yellingcat.png
# 上記のコードをコンパイルする時にペースト
# --imageの後にファイル内画像の名前を指定してサイズを取得できる
# さらにそれをスクリーン上に自動的に表示

import argparse
import cv2

# 引数parserを構築し、その引数を解析
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# (cv2.imread)によってディスクから画像を読み込み
# 幅，高さ，チャンネル数などの空間的な寸法を取得
image = cv2.imread(args["image"])
(h, w, c) = image.shape[:3]

# 画像の幅、高さ、チャンネル数を端末に表示
print("width: {} pixels".format(w))
print("height: {}  pixels".format(h))
print("channels: {}".format(c))

# 画像を表示してキー操作を待つ
cv2.imshow("Image", image)
cv2.waitKey(0)

# 画像をディスクに保存する
# （OpenCVは，画像のファイルタイプの変換を自動的に行う）
cv2.imwrite("yellingcat.png", image)
