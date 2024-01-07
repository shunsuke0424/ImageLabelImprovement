import matplotlib.pyplot as plt
import numpy as np


data = [
    {
        "label": "The room features a neutral color palette with a wainscoted wall, decorative vases on a wooden dresser, and a bed with patterned throw pillows against a backdrop of large windows offering a view of the landscape.",
        "image1_score": 0.020824531093239784,
        "image2_score": 0.017061607912182808,
        "image3_score": 0.0756632536649704,
        "image4_score": 0.002530330792069435,
        "image5_score": 0.00043176888721063733,
        "image6_score": 0.0013439827598631382,
        "image7_score": 0.002168673789128661,
        "image8_score": 0.0006245629629120231,
        "image9_score": 0.015007242560386658,
        "image10_score": 0.02980458177626133,
    },
    {
        "label": "The room features a luxurious bedroom with a vaulted ceiling featuring wooden beams, an ornate wrought iron bed frame, and an elegant fireplace as focal points.",
        "image1_score": 0.002409138949587941,
        "image2_score": 0.4109475910663605,
        "image3_score": 0.01116167102009058,
        "image4_score": 0.2042691707611084,
        "image5_score": 0.0003148062387481332,
        "image6_score": 0.0016618367517367005,
        "image7_score": 0.00974956713616848,
        "image8_score": 0.0003341578703839332,
        "image9_score": 0.00045959794078953564,
        "image10_score": 0.00042106900946237147,
    },
    {
        "label": "The room features a neutral color palette, with hardwood floors and contemporary decor, including a cozy bed, a dresser with a curved front, and multiple round mirrors on the wall.",
        "image1_score": 0.9693500399589539,
        "image2_score": 0.2537890672683716,
        "image3_score": 0.8995612859725952,
        "image4_score": 0.009333834983408451,
        "image5_score": 0.004350036382675171,
        "image6_score": 0.17378686368465424,
        "image7_score": 0.013550606556236744,
        "image8_score": 0.5517884492874146,
        "image9_score": 0.08297012001276016,
        "image10_score": 0.06821490824222565,
    },
    {
        "label": "The room features a traditional wooden four-poster bed with pink and white bedding, an ornate wrought iron chandelier, and dark wood flooring that complements the arched wooden doors.",
        "image1_score": 2.3782595235388726e-05,
        "image2_score": 0.013125627301633358,
        "image3_score": 7.248015754157677e-05,
        "image4_score": 0.5247419476509094,
        "image5_score": 0.0021342711988836527,
        "image6_score": 0.0002774613385554403,
        "image7_score": 0.0007609146414324641,
        "image8_score": 2.798269451886881e-05,
        "image9_score": 0.00012486003106459975,
        "image10_score": 4.950151833327254e-06,
    },
    {
        "label": "The room features floral wallpaper, antique wooden furniture, and a patterned quilt on the bed.",
        "image1_score": 0.00014578891568817198,
        "image2_score": 0.008019357919692993,
        "image3_score": 0.0002762342628557235,
        "image4_score": 0.19923987984657288,
        "image5_score": 0.9901738166809082,
        "image6_score": 0.09432242065668106,
        "image7_score": 0.00015586495283059776,
        "image8_score": 0.001132698031142354,
        "image9_score": 0.033870212733745575,
        "image10_score": 6.064567060093395e-06,
    },
    {
        "label": "The room features elegant wall paneling, a unique striped wallpaper, and a cozy bed with plush pillows.",
        "image1_score": 0.0015345084248110652,
        "image2_score": 0.041543953120708466,
        "image3_score": 0.002577617997303605,
        "image4_score": 0.025007717311382294,
        "image5_score": 0.0013848053058609366,
        "image6_score": 0.7145559787750244,
        "image7_score": 0.008063043467700481,
        "image8_score": 0.005350988823920488,
        "image9_score": 0.2543565332889557,
        "image10_score": 0.001001012627966702,
    },
    {
        "label": "The room features a high vaulted ceiling with exposed dark wooden beams, a large bed with a purple comforter, and expansive windows that allow for plenty of natural light.",
        "image1_score": 0.0002924066793639213,
        "image2_score": 0.1978902816772461,
        "image3_score": 0.003589167958125472,
        "image4_score": 0.025689486414194107,
        "image5_score": 8.834222171572037e-06,
        "image6_score": 8.122958388412371e-05,
        "image7_score": 0.9481136202812195,
        "image8_score": 0.0002631493844091892,
        "image9_score": 0.0002331771538592875,
        "image10_score": 0.0003606426471378654,
    },
    {
        "label": "The room is modern and minimalist with a striking red storage bench, a single abstract painting on the wall, and a bed dressed in gray with red accent pillows.",
        "image1_score": 0.0015652155270799994,
        "image2_score": 0.00023456399503629655,
        "image3_score": 0.0007277094991877675,
        "image4_score": 1.469549533794634e-05,
        "image5_score": 4.035301117255585e-06,
        "image6_score": 8.570060163037851e-05,
        "image7_score": 4.176422589807771e-05,
        "image8_score": 0.2893419563770294,
        "image9_score": 0.08657743781805038,
        "image10_score": 0.0005800127401016653,
    },
    {
        "label": "The room features a decorative red and black patterned wallpaper on one wall, a modern low-profile bed with a brown cover, and a minimalist cream-colored chaise lounge with a matching pillow.",
        "image1_score": 0.0007498865015804768,
        "image2_score": 0.0022271033376455307,
        "image3_score": 0.0007829820387996733,
        "image4_score": 0.002288930118083954,
        "image5_score": 0.0008359201601706445,
        "image6_score": 0.004924202803522348,
        "image7_score": 0.00028114535962231457,
        "image8_score": 0.01799898035824299,
        "image9_score": 0.27081483602523804,
        "image10_score": 0.00042232131818309426,
    },
    {
        "label": "The room features a large bed with decorative pillows, a modern chaise lounge by a wide window offering an expansive view, and contemporary art pieces on the walls.",
        "image1_score": 0.0031047919765114784,
        "image2_score": 0.05516090989112854,
        "image3_score": 0.005587554071098566,
        "image4_score": 0.0068840449675917625,
        "image5_score": 0.00036169757368043065,
        "image6_score": 0.008960291743278503,
        "image7_score": 0.01711474545300007,
        "image8_score": 0.13313709199428558,
        "image9_score": 0.2555859386920929,
        "image10_score": 0.8991844058036804,
    },
]


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
