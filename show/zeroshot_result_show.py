import matplotlib.pyplot as plt
import numpy as np



def show(data):
    # ラベルとスコアを抽出
    labels = [item["label"] for item in data]
    scores_image = [[item[f"image{i+1}_score"] for i in range(10)] for item in data]

    # 描画
    plt.figure(figsize=(10, 6))

    y = np.arange(len(labels))  # ラベルの位置
    width = 0.1  # バーの幅

    colors = [
        "skyblue",
        "orange",
        "green",
        "red",
        "purple",
        "brown",
        "pink",
        "gray",
        "olive",
        "cyan",
    ]
    for i in range(10):
        plt.barh(
            y - width * 4.5 + width * i,
            [scores[i] for scores in scores_image],
            width,
            color=colors[i],
            label=f"Image {i+1}",
        )

    plt.xlabel("Score")
    plt.ylabel("Description")
    plt.title("Visualization of Bedroom Design Preferences")
    plt.yticks(y, labels)  # y軸のラベルを設定
    plt.legend()  # 凡例を表示
    plt.gca().invert_yaxis()  # Y軸を反転させる
    plt.show()


# for item in data:
#     item["label"] = ", ".join(item["label"])
# # ラベルとスコアを抽出
# labels = [item["label"] for item in data]
# scores_image1 = [item["image1_score"] for item in data]
# scores_image2 = [item["image2_score"] for item in data]
# scores_image3 = [item["image3_score"] for item in data]
# scores_image4 = [item["image4_score"] for item in data]

# # 描画
# plt.figure(figsize=(10, 6))

# y = np.arange(len(labels))  # ラベルの位置
# width = 0.2  # バーの幅

# plt.barh(y - width * 1.5, scores_image1, width, color="skyblue", label="Image 1")
# plt.barh(y - width / 2, scores_image2, width, color="orange", label="Image 2")
# plt.barh(y + width / 2, scores_image3, width, color="green", label="Image 3")
# plt.barh(y + width * 1.5, scores_image4, width, color="red", label="Image 4")

# plt.xlabel("Score")
# plt.ylabel("Description")
# plt.title("Visualization of Bedroom Design Preferences")
# plt.yticks(y, labels)  # y軸のラベルを設定
# plt.legend()  # 凡例を表示
# plt.gca().invert_yaxis()  # Y軸を反転させる
# plt.show()


def show_for_four_labels(data):
    # ラベルとスコアを抽出
    labels = [item["label"] for item in data]
    scores_image1 = [item["image1_score"] for item in data]
    scores_image2 = [item["image2_score"] for item in data]
    scores_image3 = [item["image3_score"] for item in data]
    scores_image4 = [item["image4_score"] for item in data]

    # 描画
    plt.figure(figsize=(10, 6))

    y = np.arange(len(labels))  # ラベルの位置
    width = 0.2  # バーの幅

    plt.barh(y - width * 1.5, scores_image1, width, color="skyblue", label="Image 1")
    plt.barh(y - width / 2, scores_image2, width, color="orange", label="Image 2")
    plt.barh(y + width / 2, scores_image3, width, color="green", label="Image 3")
    plt.barh(y + width * 1.5, scores_image4, width, color="red", label="Image 4")

    plt.xlabel("Score")
    plt.ylabel("Description")
    plt.title("Visualization of Bedroom Design Preferences")
    plt.yticks(y, labels)  # y軸のラベルを設定
    plt.legend()  # 凡例を表示
    plt.gca().invert_yaxis()  # Y軸を反転させる
    plt.show()
