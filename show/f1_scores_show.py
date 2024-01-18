import matplotlib.pyplot as plt
import numpy as np

# ファイルからデータを読み込む
with open("result_data/f1_scores_history/20240118_171552.txt", "r") as f:
    data = [list(map(float, line.strip().strip("[]").split(", "))) for line in f]

# データを転置
data = list(map(list, zip(*data)))

# 各F値の遷移を別の色でプロット
colors = ["b", "g", "r", "c", "m", "y", "k", "orange", "purple", "brown"]
for i, d in enumerate(data):
    plt.plot(d, color=colors[i % len(colors)])

plt.title("Progression of F1 Scores")
plt.xlabel("Epoch")
plt.ylabel("F1 Score")


# 0.1刻みで薄いグレーの線を描画
for y in np.arange(0, 1, 0.1):
    plt.axhline(y=y, color="lightgray", linestyle="-", linewidth=0.5)

plt.show()
