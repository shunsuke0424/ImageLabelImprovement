import matplotlib.pyplot as plt
import numpy as np
from data_formatter import format_for_visualization

zeroshot_result_data = [
    {
        "image": 1,
        "label": "Patterned drapery, Flower arrangement on bedside table, Glass-top side table, Indoor plant decorations, Two-tone wood flooring, Reflection in mirror, Geometric picture frames, White orchids, Sliding closet doors",
        "score": 0.6861869692802429,
    },
    {
        "image": 1,
        "label": "French doors leading to balcony, Wall sconces with dome shades, White ceiling panels, Classical painting in gilded frame, Ceiling fan with light, Wooden floor vent, Exposed wooden beams, Arched doorways, Framed wall mirror",
        "score": 0.010247240774333477,
    },
    {
        "image": 1,
        "label": "Wooden dresser with curved design, Mounted wall mirrors, Silver drawer pulls, Round wooden side table, Woven area rug, Bedside lamps with cylindrical shades, Under-cabinet lighting, Gray wall paint, Decorative bed pillows",
        "score": 0.3011356294155121,
    },
    {
        "image": 1,
        "label": "Ornate curtain rods, Intricate area rug, Warm-toned wood finishes, Wooden floor vent, Carved wood details on furniture, Textured ceiling finish, Traditional room decor, Tassel curtain tie-backs, Decorative bed pillows",
        "score": 0.002430171240121126,
    },
    {
        "image": 2,
        "label": "Patterned drapery, Flower arrangement on bedside table, Glass-top side table, Indoor plant decorations, Two-tone wood flooring, Reflection in mirror, Geometric picture frames, White orchids, Sliding closet doors",
        "score": 0.00834642257541418,
    },
    {
        "image": 2,
        "label": "French doors leading to balcony, Wall sconces with dome shades, White ceiling panels, Classical painting in gilded frame, Ceiling fan with light, Wooden floor vent, Exposed wooden beams, Arched doorways, Framed wall mirror",
        "score": 0.7425777316093445,
    },
    {
        "image": 2,
        "label": "Wooden dresser with curved design, Mounted wall mirrors, Silver drawer pulls, Round wooden side table, Woven area rug, Bedside lamps with cylindrical shades, Under-cabinet lighting, Gray wall paint, Decorative bed pillows",
        "score": 0.01993335783481598,
    },
    {
        "image": 2,
        "label": "Ornate curtain rods, Intricate area rug, Warm-toned wood finishes, Wooden floor vent, Carved wood details on furniture, Textured ceiling finish, Traditional room decor, Tassel curtain tie-backs, Decorative bed pillows",
        "score": 0.22914256155490875,
    },
    {
        "image": 3,
        "label": "Patterned drapery, Flower arrangement on bedside table, Glass-top side table, Indoor plant decorations, Two-tone wood flooring, Reflection in mirror, Geometric picture frames, White orchids, Sliding closet doors",
        "score": 0.11483073234558105,
    },
    {
        "image": 3,
        "label": "French doors leading to balcony, Wall sconces with dome shades, White ceiling panels, Classical painting in gilded frame, Ceiling fan with light, Wooden floor vent, Exposed wooden beams, Arched doorways, Framed wall mirror",
        "score": 0.025256354361772537,
    },
    {
        "image": 3,
        "label": "Wooden dresser with curved design, Mounted wall mirrors, Silver drawer pulls, Round wooden side table, Woven area rug, Bedside lamps with cylindrical shades, Under-cabinet lighting, Gray wall paint, Decorative bed pillows",
        "score": 0.8459940552711487,
    },
    {
        "image": 3,
        "label": "Ornate curtain rods, Intricate area rug, Warm-toned wood finishes, Wooden floor vent, Carved wood details on furniture, Textured ceiling finish, Traditional room decor, Tassel curtain tie-backs, Decorative bed pillows",
        "score": 0.013918889686465263,
    },
    {
        "image": 4,
        "label": "Patterned drapery, Flower arrangement on bedside table, Glass-top side table, Indoor plant decorations, Two-tone wood flooring, Reflection in mirror, Geometric picture frames, White orchids, Sliding closet doors",
        "score": 0.0008877433720044792,
    },
    {
        "image": 4,
        "label": "French doors leading to balcony, Wall sconces with dome shades, White ceiling panels, Classical painting in gilded frame, Ceiling fan with light, Wooden floor vent, Exposed wooden beams, Arched doorways, Framed wall mirror",
        "score": 0.05746058002114296,
    },
    {
        "image": 4,
        "label": "Wooden dresser with curved design, Mounted wall mirrors, Silver drawer pulls, Round wooden side table, Woven area rug, Bedside lamps with cylindrical shades, Under-cabinet lighting, Gray wall paint, Decorative bed pillows",
        "score": 0.000492765277158469,
    },
    {
        "image": 4,
        "label": "Ornate curtain rods, Intricate area rug, Warm-toned wood finishes, Wooden floor vent, Carved wood details on furniture, Textured ceiling finish, Traditional room decor, Tassel curtain tie-backs, Decorative bed pillows",
        "score": 0.9411589503288269,
    },
]

data = format_for_visualization(zeroshot_result_data)
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
