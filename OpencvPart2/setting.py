# コンパイルする時の使い方
# python setting.py　をターミナルかコマンドプロンプトでペースト

# 必要なパッケージ
from matplotlib import pyplot as plt
import argparse  # argparseを使うためにインポート
import cv2

# 引数パーサーを構築し、引数を解析する
# ArgumentParser(argparse)を使うと
# python program.py test.txt --alpha 0.01
# のように，プログラムで処理したいファイル名や何かのパラメータなどを実行時に指定できる
# argparseはヘルプと使用方法のメッセージを作成し、引数の指定に誤りがあった場合にエラーを発生させる
# argparseモジュールを使用することで簡潔にメッセージの作成と引数の解析を行うことができる
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="samplepic.png",
	help="path to the input image")
args = vars(ap.parse_args())

# 画像を読み込んで、その空間的な寸法（幅と高さ）を取得し、
# オリジナルの画像を画面に表示
image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
cv2.imshow("original", image)

# image は，原点(0, 0)を画像の左上に置いたNumPyの配列
(b, g, r) = image[0, 0]
print("(0, 0)での画素 - 赤: {}, 緑: {}, 青: {}".format(r, g, b))

# x=50, y=20に位置する画素にアクセス
(b, g, r) = image[20, 50]
print("(50, 20)での画素 - 赤: {}, 緑: {}, 青: {}".format(r, g, b))

# (50, 20)のピクセルを更新し、赤に設定する
image[20, 50] = (0, 0, 255)
(b, g, r) = image[20, 50]
print("(50, 20)での画素 - 赤: {}, 緑: {}, 青: {}".format(r, g, b))

# 幅と高さを2で割っただけの画像の中心を計算
(cX, cY) = (w // 2, h // 2)

# NumPyの配列を使用しているので、配列の一部分を適用して、
# 画像から関心のある大きな塊や領域を取り出すことができます。
# image -- ここでは，画像の左上隅を取り出しています．
tl = image[0:cY, 0:cX]
cv2.imshow("Top-Left Corner", tl)

# 同様に、画像の右上、右下、左下を切り整えて 画像の右上、右下、左下を切り取りして、
# 画面に表示することができる
tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]
cv2.imshow("Top-Right Corner", tr)
cv2.imshow("Bottom-Right Corner", br)
cv2.imshow("Bottom-Left Corner", bl)

# 元画像の左上を緑にする。
image[0:cY, 0:cX] = (0, 255, 0)

# 更新された画像を表示
cv2.imshow("Updated", image)
cv2.waitKey(0)
