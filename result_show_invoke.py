import matplotlib.pyplot as plt
import numpy as np
from data_formatter import format_for_visualization

zeroshot_result_data = [
    {
        "image": 1,
        "label": "Tray ceiling Recessed lighting, Geometric picture frames, Glass vase with white flowers",
        "score": 0.5685943961143494,
    },
    {
        "image": 1,
        "label": "Arched doorways, Vaulted ceilings, White bed linens",
        "score": 0.03025234118103981,
    },
    {
        "image": 1,
        "label": "White vase with greenery, Plush throw blanket, Recessed lighting",
        "score": 0.002715709153562784,
    },
    {
        "image": 1,
        "label": "Wooden ceiling beams, Hinged closet door, Tassel curtain tie-backs",
        "score": 0.1548168808221817,
    },
    {
        "image": 1,
        "label": "Lace curtains, Light blue tea set, White ceiling",
        "score": 1.5913510651444085e-05,
    },
    {
        "image": 1,
        "label": "Beige wall paint above paneling, Paneled walls, Subtle wall texture",
        "score": 0.12588900327682495,
    },
    {
        "image": 1,
        "label": "Exposed dark beams, Chrome bath filler",
        "score": 0.004992457572370768,
    },
    {
        "image": 1,
        "label": "Neutral-toned bedding, Minimalistic design, White radiator heater",
        "score": 0.0001285878970520571,
    },
    {
        "image": 1,
        "label": "Practical room layout, Contemporary chair, Fluffy white area rug",
        "score": 0.003554729977622628,
    },
    {
        "image": 1,
        "label": "Gray upholstered bench, Geometric ceiling angles, Sliding door to balcony",
        "score": 0.10903994739055634,
    },
    {
        "image": 2,
        "label": "Tray ceiling Recessed lighting, Geometric picture frames, Glass vase with white flowers",
        "score": 0.0001584109413670376,
    },
    {
        "image": 2,
        "label": "Arched doorways, Vaulted ceilings, White bed linens",
        "score": 0.991204559803009,
    },
    {
        "image": 2,
        "label": "White vase with greenery, Plush throw blanket, Recessed lighting",
        "score": 7.623357760166982e-06,
    },
    {
        "image": 2,
        "label": "Wooden ceiling beams, Hinged closet door, Tassel curtain tie-backs",
        "score": 0.006991901900619268,
    },
    {
        "image": 2,
        "label": "Lace curtains, Light blue tea set, White ceiling",
        "score": 5.834074272570433e-07,
    },
    {
        "image": 2,
        "label": "Beige wall paint above paneling, Paneled walls, Subtle wall texture",
        "score": 0.0003999417822342366,
    },
    {
        "image": 2,
        "label": "Exposed dark beams, Chrome bath filler",
        "score": 0.0010394119890406728,
    },
    {
        "image": 2,
        "label": "Neutral-toned bedding, Minimalistic design, White radiator heater",
        "score": 6.138662683952134e-06,
    },
    {
        "image": 2,
        "label": "Practical room layout, Contemporary chair, Fluffy white area rug",
        "score": 1.8846625607693568e-05,
    },
    {
        "image": 2,
        "label": "Gray upholstered bench, Geometric ceiling angles, Sliding door to balcony",
        "score": 0.00017243361799046397,
    },
    {
        "image": 3,
        "label": "Tray ceiling Recessed lighting, Geometric picture frames, Glass vase with white flowers",
        "score": 0.20947515964508057,
    },
    {
        "image": 3,
        "label": "Arched doorways, Vaulted ceilings, White bed linens",
        "score": 0.45153912901878357,
    },
    {
        "image": 3,
        "label": "White vase with greenery, Plush throw blanket, Recessed lighting",
        "score": 0.037991270422935486,
    },
    {
        "image": 3,
        "label": "Wooden ceiling beams, Hinged closet door, Tassel curtain tie-backs",
        "score": 0.08811023831367493,
    },
    {
        "image": 3,
        "label": "Lace curtains, Light blue tea set, White ceiling",
        "score": 0.00043488346273079515,
    },
    {
        "image": 3,
        "label": "Beige wall paint above paneling, Paneled walls, Subtle wall texture",
        "score": 0.052959877997636795,
    },
    {
        "image": 3,
        "label": "Exposed dark beams, Chrome bath filler",
        "score": 0.020005106925964355,
    },
    {
        "image": 3,
        "label": "Neutral-toned bedding, Minimalistic design, White radiator heater",
        "score": 0.005846856161952019,
    },
    {
        "image": 3,
        "label": "Practical room layout, Contemporary chair, Fluffy white area rug",
        "score": 0.028620760887861252,
    },
    {
        "image": 3,
        "label": "Gray upholstered bench, Geometric ceiling angles, Sliding door to balcony",
        "score": 0.10501658171415329,
    },
    {
        "image": 4,
        "label": "Tray ceiling Recessed lighting, Geometric picture frames, Glass vase with white flowers",
        "score": 0.0003426732437219471,
    },
    {
        "image": 4,
        "label": "Arched doorways, Vaulted ceilings, White bed linens",
        "score": 0.47077447175979614,
    },
    {
        "image": 4,
        "label": "White vase with greenery, Plush throw blanket, Recessed lighting",
        "score": 4.61028866993729e-06,
    },
    {
        "image": 4,
        "label": "Wooden ceiling beams, Hinged closet door, Tassel curtain tie-backs",
        "score": 0.5224473476409912,
    },
    {
        "image": 4,
        "label": "Lace curtains, Light blue tea set, White ceiling",
        "score": 3.7028585211373866e-05,
    },
    {
        "image": 4,
        "label": "Beige wall paint above paneling, Paneled walls, Subtle wall texture",
        "score": 0.0053375097922980785,
    },
    {
        "image": 4,
        "label": "Exposed dark beams, Chrome bath filler",
        "score": 0.00031253049382939935,
    },
    {
        "image": 4,
        "label": "Neutral-toned bedding, Minimalistic design, White radiator heater",
        "score": 6.584074071724899e-06,
    },
    {
        "image": 4,
        "label": "Practical room layout, Contemporary chair, Fluffy white area rug",
        "score": 8.954660734161735e-05,
    },
    {
        "image": 4,
        "label": "Gray upholstered bench, Geometric ceiling angles, Sliding door to balcony",
        "score": 0.0006476233247667551,
    },
    {
        "image": 5,
        "label": "Tray ceiling Recessed lighting, Geometric picture frames, Glass vase with white flowers",
        "score": 0.10685917735099792,
    },
    {
        "image": 5,
        "label": "Arched doorways, Vaulted ceilings, White bed linens",
        "score": 0.33933231234550476,
    },
    {
        "image": 5,
        "label": "White vase with greenery, Plush throw blanket, Recessed lighting",
        "score": 0.00034754781518131495,
    },
    {
        "image": 5,
        "label": "Wooden ceiling beams, Hinged closet door, Tassel curtain tie-backs",
        "score": 0.01078581903129816,
    },
    {
        "image": 5,
        "label": "Lace curtains, Light blue tea set, White ceiling",
        "score": 0.35752490162849426,
    },
    {
        "image": 5,
        "label": "Beige wall paint above paneling, Paneled walls, Subtle wall texture",
        "score": 0.17134906351566315,
    },
    {
        "image": 5,
        "label": "Exposed dark beams, Chrome bath filler",
        "score": 0.004070333670824766,
    },
    {
        "image": 5,
        "label": "Neutral-toned bedding, Minimalistic design, White radiator heater",
        "score": 0.006646979134529829,
    },
    {
        "image": 5,
        "label": "Practical room layout, Contemporary chair, Fluffy white area rug",
        "score": 0.0014157365076243877,
    },
    {
        "image": 5,
        "label": "Gray upholstered bench, Geometric ceiling angles, Sliding door to balcony",
        "score": 0.0016681530978530645,
    },
    {
        "image": 6,
        "label": "Tray ceiling Recessed lighting, Geometric picture frames, Glass vase with white flowers",
        "score": 0.029177570715546608,
    },
    {
        "image": 6,
        "label": "Arched doorways, Vaulted ceilings, White bed linens",
        "score": 0.15112236142158508,
    },
    {
        "image": 6,
        "label": "White vase with greenery, Plush throw blanket, Recessed lighting",
        "score": 2.1009329429944046e-05,
    },
    {
        "image": 6,
        "label": "Wooden ceiling beams, Hinged closet door, Tassel curtain tie-backs",
        "score": 0.21305084228515625,
    },
    {
        "image": 6,
        "label": "Lace curtains, Light blue tea set, White ceiling",
        "score": 7.175360951805487e-05,
    },
    {
        "image": 6,
        "label": "Beige wall paint above paneling, Paneled walls, Subtle wall texture",
        "score": 0.3649609386920929,
    },
    {
        "image": 6,
        "label": "Exposed dark beams, Chrome bath filler",
        "score": 0.009351378306746483,
    },
    {
        "image": 6,
        "label": "Neutral-toned bedding, Minimalistic design, White radiator heater",
        "score": 0.001132081844843924,
    },
    {
        "image": 6,
        "label": "Practical room layout, Contemporary chair, Fluffy white area rug",
        "score": 0.0007645715377293527,
    },
    {
        "image": 6,
        "label": "Gray upholstered bench, Geometric ceiling angles, Sliding door to balcony",
        "score": 0.23034751415252686,
    },
    {
        "image": 7,
        "label": "Tray ceiling Recessed lighting, Geometric picture frames, Glass vase with white flowers",
        "score": 0.004836329258978367,
    },
    {
        "image": 7,
        "label": "Arched doorways, Vaulted ceilings, White bed linens",
        "score": 0.05650956183671951,
    },
    {
        "image": 7,
        "label": "White vase with greenery, Plush throw blanket, Recessed lighting",
        "score": 9.753374797583092e-06,
    },
    {
        "image": 7,
        "label": "Wooden ceiling beams, Hinged closet door, Tassel curtain tie-backs",
        "score": 0.16934989392757416,
    },
    {
        "image": 7,
        "label": "Lace curtains, Light blue tea set, White ceiling",
        "score": 3.9295344322454184e-05,
    },
    {
        "image": 7,
        "label": "Beige wall paint above paneling, Paneled walls, Subtle wall texture",
        "score": 0.0012627247488126159,
    },
    {
        "image": 7,
        "label": "Exposed dark beams, Chrome bath filler",
        "score": 0.5517970323562622,
    },
    {
        "image": 7,
        "label": "Neutral-toned bedding, Minimalistic design, White radiator heater",
        "score": 0.001392578473314643,
    },
    {
        "image": 7,
        "label": "Practical room layout, Contemporary chair, Fluffy white area rug",
        "score": 0.0005039743264205754,
    },
    {
        "image": 7,
        "label": "Gray upholstered bench, Geometric ceiling angles, Sliding door to balcony",
        "score": 0.21429891884326935,
    },
    {
        "image": 8,
        "label": "Tray ceiling Recessed lighting, Geometric picture frames, Glass vase with white flowers",
        "score": 0.054998934268951416,
    },
    {
        "image": 8,
        "label": "Arched doorways, Vaulted ceilings, White bed linens",
        "score": 0.1068073958158493,
    },
    {
        "image": 8,
        "label": "White vase with greenery, Plush throw blanket, Recessed lighting",
        "score": 0.00019873165001627058,
    },
    {
        "image": 8,
        "label": "Wooden ceiling beams, Hinged closet door, Tassel curtain tie-backs",
        "score": 0.027206873521208763,
    },
    {
        "image": 8,
        "label": "Lace curtains, Light blue tea set, White ceiling",
        "score": 1.4787373402214143e-05,
    },
    {
        "image": 8,
        "label": "Beige wall paint above paneling, Paneled walls, Subtle wall texture",
        "score": 0.16779014468193054,
    },
    {
        "image": 8,
        "label": "Exposed dark beams, Chrome bath filler",
        "score": 0.02733764797449112,
    },
    {
        "image": 8,
        "label": "Neutral-toned bedding, Minimalistic design, White radiator heater",
        "score": 0.014675748534500599,
    },
    {
        "image": 8,
        "label": "Practical room layout, Contemporary chair, Fluffy white area rug",
        "score": 0.017076851800084114,
    },
    {
        "image": 8,
        "label": "Gray upholstered bench, Geometric ceiling angles, Sliding door to balcony",
        "score": 0.5838929414749146,
    },
    {
        "image": 9,
        "label": "Tray ceiling Recessed lighting, Geometric picture frames, Glass vase with white flowers",
        "score": 0.04425078630447388,
    },
    {
        "image": 9,
        "label": "Arched doorways, Vaulted ceilings, White bed linens",
        "score": 0.01585726998746395,
    },
    {
        "image": 9,
        "label": "White vase with greenery, Plush throw blanket, Recessed lighting",
        "score": 0.005081578157842159,
    },
    {
        "image": 9,
        "label": "Wooden ceiling beams, Hinged closet door, Tassel curtain tie-backs",
        "score": 0.003637587884441018,
    },
    {
        "image": 9,
        "label": "Lace curtains, Light blue tea set, White ceiling",
        "score": 0.005577786825597286,
    },
    {
        "image": 9,
        "label": "Beige wall paint above paneling, Paneled walls, Subtle wall texture",
        "score": 0.05867142602801323,
    },
    {
        "image": 9,
        "label": "Exposed dark beams, Chrome bath filler",
        "score": 0.004063940141350031,
    },
    {
        "image": 9,
        "label": "Neutral-toned bedding, Minimalistic design, White radiator heater",
        "score": 0.2395169883966446,
    },
    {
        "image": 9,
        "label": "Practical room layout, Contemporary chair, Fluffy white area rug",
        "score": 0.28283214569091797,
    },
    {
        "image": 9,
        "label": "Gray upholstered bench, Geometric ceiling angles, Sliding door to balcony",
        "score": 0.34051060676574707,
    },
    {
        "image": 10,
        "label": "Tray ceiling Recessed lighting, Geometric picture frames, Glass vase with white flowers",
        "score": 0.09686896204948425,
    },
    {
        "image": 10,
        "label": "Arched doorways, Vaulted ceilings, White bed linens",
        "score": 0.05338440462946892,
    },
    {
        "image": 10,
        "label": "White vase with greenery, Plush throw blanket, Recessed lighting",
        "score": 0.0017380081117153168,
    },
    {
        "image": 10,
        "label": "Wooden ceiling beams, Hinged closet door, Tassel curtain tie-backs",
        "score": 0.0012674618046730757,
    },
    {
        "image": 10,
        "label": "Lace curtains, Light blue tea set, White ceiling",
        "score": 0.0001112220561481081,
    },
    {
        "image": 10,
        "label": "Beige wall paint above paneling, Paneled walls, Subtle wall texture",
        "score": 0.0010550039587542415,
    },
    {
        "image": 10,
        "label": "Exposed dark beams, Chrome bath filler",
        "score": 0.00937588233500719,
    },
    {
        "image": 10,
        "label": "Neutral-toned bedding, Minimalistic design, White radiator heater",
        "score": 0.0009344678837805986,
    },
    {
        "image": 10,
        "label": "Practical room layout, Contemporary chair, Fluffy white area rug",
        "score": 0.07375546544790268,
    },
    {
        "image": 10,
        "label": "Gray upholstered bench, Geometric ceiling angles, Sliding door to balcony",
        "score": 0.761509120464325,
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
