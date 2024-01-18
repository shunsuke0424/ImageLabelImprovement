from distance_data import similarity_cache

# ラベル群
data1 = [
    [
        "Decorative ceramic vases",
        "High baseboards",
        "Beige upholstered bench",
        "Cable railing on staircase",
        "Light switch plates",
        "Matching wood-framed pictures",
        "Coordinated picture frames",
    ],
    [
        "Exposed wooden beams",
        "Wrought iron bed frame",
        "Fire burning in fireplace",
        "Vaulted ceilings",
        "Classical painting in gilded frame",
        "Outdoor lantern-style light fixture",
    ],
    [
        "Striped upholstered bench",
        "Decorative straw hats on wall",
        "Mounted wall mirrors",
        "French doors with transom windows",
        "Gray wall paint",
        "Under-cabinet lighting",
        "Indoor potted plants",
    ],
    [
        "Textured ceiling finish",
        "Floral bed linens",
        "Framed floral artwork",
        "Intricate area rug",
        "Patterned curtains",
    ],
    [
        "Sheer window drapery",
        "Decorative bed pillows",
        "Vintage telephone",
        "Intricate carpet design",
        "Traditional room decor",
        "Porcelain table lamps",
        "White baseboards",
    ],
    [
        "Minimalist decor style",
        "Symmetrical wall design",
        "White bedding",
        "Dark wood trim",
        "Warm ambient light",
        "Spacious room layout",
        "Glass in pendant lights",
    ],
    [
        "Wall-mounted air vents",
        "Multi-level living spaces",
        "Exposed dark beams",
        "Elevated bedroom area",
        "Frameless circular wall mirror",
        "Lush greenery outside the window",
    ],
    [
        "High ceilings",
        "Compact living space",
        "Flush mounted ceiling lights",
        "Orange-red color accents",
        "Recessed wall nooks",
        "White door frames",
        "Accent lighting in art niche",
    ],
    [
        "Hardwood flooring",
        "Fluffy white area rug",
        "Blended interior decor",
        "Architectural room features",
        "Cozy room atmosphere",
        "Patterned wallpaper accent wall",
    ],
    [
        "Floor to ceiling windows",
        "Light filtering through windows",
        "HVAC vent on the floor",
        "Recessed lighting",
        "Sliding door to balcony",
    ],
]
data2 = [
    [
        "Beige carpet runner",
        "Beige upholstered bench",
        "Matching wood-framed pictures",
        "Tray ceiling Recessed lighting",
        "Bathroom mirror with wood frame",
        "Large picture windows",
        "Wainscoting on lower walls",
        "Silver drawer handles",
        "Reflection in mirror",
        "Ventilation grilles on the floor",
        "Dark wood nightstands",
        "Square ceiling vent",
    ],
    [
        "Arched doorways",
        "Beige upholstered bench",
        "Wall sconces with dome shades",
        "Leather ottoman",
        "Vaulted ceilings",
        "Framed wall mirror",
        "Balcony overlooking greenery",
        "Cast iron coat hanger",
    ],
    [
        "Ceramic canisters on counter",
        "Two-toned kitchen cabinetry",
        "Striped upholstered bench",
        "Mounted wall mirrors",
        "White vase with greenery",
        "Wall cutout looking into kitchen",
        "Recessed lighting",
    ],
    [
        "Brass door handles",
        "Sheer curtain under drapery",
        "Traditional room decor",
        "Stone-top bedside table",
        "Hinged closet door",
        "Beamed ceiling",
        "Intricate area rug",
    ],
    [
        "Carved wood details",
        "Wooden side table",
        "Delicate porcelain figurines",
        "Ceiling medallion",
        "Lace curtains",
        "Patchwork quilt",
        "White ceiling",
        "Dual sash windows",
    ],
    [
        "View into adjacent room",
        "Neutral color palette",
        "White painted doors",
        "Built-in bookshelves in other room",
        "Solid wood entry door",
        "Dual pendant lights",
        "Crown molding",
        "Ventilation grill on the floor",
        "Dark wood trim",
        "Paneled walls",
    ],
    [
        "Chrome bath filler",
        "White tiled walls in the bathroom",
        "Large window panes",
        "Black curtain dividing the room",
        "Black bed frame",
        "Exposed dark beams",
        "Square wall-mounted sink",
    ],
    [
        "Orange-red color accents",
        "Visible tree outside window",
        "Minimalistic design",
        "White door frames",
        "White ceiling",
        "Accent lighting in art niche",
        "Floor vent",
        "Structural column in room",
    ],
    [
        "Hardwood flooring",
        "Urban view from the window",
        "Single bed with brown cover",
        "Black venetian blinds",
        "Slanted ceiling",
        "Gray skirting on accent wall",
        "Geometric form of wardrobe",
        "Simple bed frame",
    ],
    [
        "City view",
        "Outdoor patio area",
        "High-end",
        "Modern bed frame",
        "Large windows",
        "Vaulted ceiling",
        "Matching bedside lamps",
        "Uniform ceiling height",
        "Clean",
        "Recessed lighting",
    ],
]

# ラベル群を類似度に置き換える
similarity_scores = []
avg_similarity_scores = []
for label_group in data2:
    group_scores = []
    # ラベル群をカンマで区切って要素に分ける
    for label in label_group:
        # similarity_cacheを適切なインデックスを呼び出して辞書型データを取得する
        for similarity_dict in similarity_cache:
            # その中のkeyと要素を探索してスコアに置き換える
            if label in similarity_dict:
                group_scores.append(similarity_dict[label])
                break
    # スコアの算術平均を計算
    average_score = sum(group_scores) / len(group_scores) if group_scores else 0
    avg_similarity_scores.append(average_score)
    similarity_scores.append(group_scores)
x = sum(similarity_scores, [])
print(x)
# スコアの算術平均の算術平均を計算
avg_similarity_scores = sum(x) / len(x) if x else 0
print(avg_similarity_scores)


# ラベル群を類似度に置き換えて並べ替える
sorted_labels = []
for label_group in data1:
    # ラベルとスコアの辞書を作成
    label_scores = {}
    for label in label_group:
        for similarity_dict in similarity_cache:
            if label in similarity_dict:
                label_scores[label] = similarity_dict[label]
                break
    # スコアが高い順に並べ替え
    sorted_group = sorted(label_scores.items(), key=lambda x: x[1], reverse=True)
    sorted_labels_only = [label for label, score in sorted_group]
    sorted_labels.append(sorted_labels_only)

print(sorted_labels)
labels_text_list = [", ".join(labels) for labels in sorted_labels]
print(labels_text_list)
