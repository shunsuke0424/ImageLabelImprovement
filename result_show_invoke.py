import matplotlib.pyplot as plt
import numpy as np
from data_formatter import format_for_visualization

zeroshot_result_data = [
    {
        "image": 1,
        "label": "Decorative ceramic vases, High baseboards, Beige upholstered bench, Cable railing on staircase, Light switch plates, Matching wood-framed pictures, Coordinated picture frames",
        "score": 0.7673078179359436,
    },
    {
        "image": 1,
        "label": "Exposed wooden beams, Balcony overlooking greenery, Recessed lighting, Vaulted ceilings, Ceiling fan with light, Classical painting in gilded frame, Wall recess for art display",
        "score": 0.004694561939686537,
    },
    {
        "image": 1,
        "label": "Striped upholstered bench, Wicker basket plant holder, Bedside lamps with cylindrical shades, Mounted wall mirrors, Dark hardwood flooring, Stainless steel appliances, Under-cabinet lighting",
        "score": 0.013253578916192055,
    },
    {
        "image": 1,
        "label": "Area rug with floral design, Tassel curtain tie-backs, Wooden ceiling beams, Cream-colored walls, Patterned curtains, Carved wood details on furniture",
        "score": 0.0033839468378573656,
    },
    {
        "image": 1,
        "label": "Decorative bed pillows, Floral arrangement in vase, Brass door handle, White baseboards, Carved wooden vanity mirror, Patchwork quilt, Vintage telephone",
        "score": 0.0012539401650428772,
    },
    {
        "image": 1,
        "label": "White painted doors, Symmetrical wall design, Rectangular wall mirror, Wall-mounted framed art, Dark wood trim, Warm ambient light, Glass in pendant lights",
        "score": 0.1300256848335266,
    },
    {
        "image": 1,
        "label": "Black bed frame, Large window panes, A-frame ceiling, Sheer window shades, Lush greenery outside the window, Clean lines in interior architecture",
        "score": 0.003280159318819642,
    },
    {
        "image": 1,
        "label": "High ceilings, Compact living space, Flush mounted ceiling lights, Orange-red color accents, Recessed wall nooks, White door frames, Accent lighting in art niche",
        "score": 0.05165420100092888,
    },
    {
        "image": 1,
        "label": "Red window blinds, Sleek wardrobe handles, Visible texture in wooden flooring, Single bed with brown cover, Beige throw pillow, Patterned wallpaper accent wall",
        "score": 0.0011015841737389565,
    },
    {
        "image": 1,
        "label": "Hardwood flooring, Nightstands with drawers, Light filtering through windows, Spacious and airy atmosphere, Wall-mounted flat-screen TV, City view",
        "score": 0.0240445826202631,
    },
    {
        "image": 2,
        "label": "Decorative ceramic vases, High baseboards, Beige upholstered bench, Cable railing on staircase, Light switch plates, Matching wood-framed pictures, Coordinated picture frames",
        "score": 0.01946774497628212,
    },
    {
        "image": 2,
        "label": "Exposed wooden beams, Balcony overlooking greenery, Recessed lighting, Vaulted ceilings, Ceiling fan with light, Classical painting in gilded frame, Wall recess for art display",
        "score": 0.8461893200874329,
    },
    {
        "image": 2,
        "label": "Striped upholstered bench, Wicker basket plant holder, Bedside lamps with cylindrical shades, Mounted wall mirrors, Dark hardwood flooring, Stainless steel appliances, Under-cabinet lighting",
        "score": 0.0006526486249640584,
    },
    {
        "image": 2,
        "label": "Area rug with floral design, Tassel curtain tie-backs, Wooden ceiling beams, Cream-colored walls, Patterned curtains, Carved wood details on furniture",
        "score": 0.03804220259189606,
    },
    {
        "image": 2,
        "label": "Decorative bed pillows, Floral arrangement in vase, Brass door handle, White baseboards, Carved wooden vanity mirror, Patchwork quilt, Vintage telephone",
        "score": 0.004616125952452421,
    },
    {
        "image": 2,
        "label": "White painted doors, Symmetrical wall design, Rectangular wall mirror, Wall-mounted framed art, Dark wood trim, Warm ambient light, Glass in pendant lights",
        "score": 0.020150912925601006,
    },
    {
        "image": 2,
        "label": "Black bed frame, Large window panes, A-frame ceiling, Sheer window shades, Lush greenery outside the window, Clean lines in interior architecture",
        "score": 0.01064401026815176,
    },
    {
        "image": 2,
        "label": "High ceilings, Compact living space, Flush mounted ceiling lights, Orange-red color accents, Recessed wall nooks, White door frames, Accent lighting in art niche",
        "score": 0.04966306313872337,
    },
    {
        "image": 2,
        "label": "Red window blinds, Sleek wardrobe handles, Visible texture in wooden flooring, Single bed with brown cover, Beige throw pillow, Patterned wallpaper accent wall",
        "score": 0.0012068486539646983,
    },
    {
        "image": 2,
        "label": "Hardwood flooring, Nightstands with drawers, Light filtering through windows, Spacious and airy atmosphere, Wall-mounted flat-screen TV, City view",
        "score": 0.009367203339934349,
    },
    {
        "image": 3,
        "label": "Decorative ceramic vases, High baseboards, Beige upholstered bench, Cable railing on staircase, Light switch plates, Matching wood-framed pictures, Coordinated picture frames",
        "score": 0.22365128993988037,
    },
    {
        "image": 3,
        "label": "Exposed wooden beams, Balcony overlooking greenery, Recessed lighting, Vaulted ceilings, Ceiling fan with light, Classical painting in gilded frame, Wall recess for art display",
        "score": 0.018671009689569473,
    },
    {
        "image": 3,
        "label": "Striped upholstered bench, Wicker basket plant holder, Bedside lamps with cylindrical shades, Mounted wall mirrors, Dark hardwood flooring, Stainless steel appliances, Under-cabinet lighting",
        "score": 0.13566948473453522,
    },
    {
        "image": 3,
        "label": "Area rug with floral design, Tassel curtain tie-backs, Wooden ceiling beams, Cream-colored walls, Patterned curtains, Carved wood details on furniture",
        "score": 0.007845879532396793,
    },
    {
        "image": 3,
        "label": "Decorative bed pillows, Floral arrangement in vase, Brass door handle, White baseboards, Carved wooden vanity mirror, Patchwork quilt, Vintage telephone",
        "score": 0.012472542002797127,
    },
    {
        "image": 3,
        "label": "White painted doors, Symmetrical wall design, Rectangular wall mirror, Wall-mounted framed art, Dark wood trim, Warm ambient light, Glass in pendant lights",
        "score": 0.05498464033007622,
    },
    {
        "image": 3,
        "label": "Black bed frame, Large window panes, A-frame ceiling, Sheer window shades, Lush greenery outside the window, Clean lines in interior architecture",
        "score": 0.20034097135066986,
    },
    {
        "image": 3,
        "label": "High ceilings, Compact living space, Flush mounted ceiling lights, Orange-red color accents, Recessed wall nooks, White door frames, Accent lighting in art niche",
        "score": 0.08005041629076004,
    },
    {
        "image": 3,
        "label": "Red window blinds, Sleek wardrobe handles, Visible texture in wooden flooring, Single bed with brown cover, Beige throw pillow, Patterned wallpaper accent wall",
        "score": 0.016768472269177437,
    },
    {
        "image": 3,
        "label": "Hardwood flooring, Nightstands with drawers, Light filtering through windows, Spacious and airy atmosphere, Wall-mounted flat-screen TV, City view",
        "score": 0.24954530596733093,
    },
    {
        "image": 4,
        "label": "Decorative ceramic vases, High baseboards, Beige upholstered bench, Cable railing on staircase, Light switch plates, Matching wood-framed pictures, Coordinated picture frames",
        "score": 0.0007108512800186872,
    },
    {
        "image": 4,
        "label": "Exposed wooden beams, Balcony overlooking greenery, Recessed lighting, Vaulted ceilings, Ceiling fan with light, Classical painting in gilded frame, Wall recess for art display",
        "score": 0.16328303515911102,
    },
    {
        "image": 4,
        "label": "Striped upholstered bench, Wicker basket plant holder, Bedside lamps with cylindrical shades, Mounted wall mirrors, Dark hardwood flooring, Stainless steel appliances, Under-cabinet lighting",
        "score": 1.5033429917821195e-05,
    },
    {
        "image": 4,
        "label": "Area rug with floral design, Tassel curtain tie-backs, Wooden ceiling beams, Cream-colored walls, Patterned curtains, Carved wood details on furniture",
        "score": 0.8297433257102966,
    },
    {
        "image": 4,
        "label": "Decorative bed pillows, Floral arrangement in vase, Brass door handle, White baseboards, Carved wooden vanity mirror, Patchwork quilt, Vintage telephone",
        "score": 0.0029075858183205128,
    },
    {
        "image": 4,
        "label": "White painted doors, Symmetrical wall design, Rectangular wall mirror, Wall-mounted framed art, Dark wood trim, Warm ambient light, Glass in pendant lights",
        "score": 0.0013396971626207232,
    },
    {
        "image": 4,
        "label": "Black bed frame, Large window panes, A-frame ceiling, Sheer window shades, Lush greenery outside the window, Clean lines in interior architecture",
        "score": 0.0004532938764896244,
    },
    {
        "image": 4,
        "label": "High ceilings, Compact living space, Flush mounted ceiling lights, Orange-red color accents, Recessed wall nooks, White door frames, Accent lighting in art niche",
        "score": 0.0004964596009813249,
    },
    {
        "image": 4,
        "label": "Red window blinds, Sleek wardrobe handles, Visible texture in wooden flooring, Single bed with brown cover, Beige throw pillow, Patterned wallpaper accent wall",
        "score": 0.0006812746869400144,
    },
    {
        "image": 4,
        "label": "Hardwood flooring, Nightstands with drawers, Light filtering through windows, Spacious and airy atmosphere, Wall-mounted flat-screen TV, City view",
        "score": 0.0003694825281854719,
    },
    {
        "image": 5,
        "label": "Decorative ceramic vases, High baseboards, Beige upholstered bench, Cable railing on staircase, Light switch plates, Matching wood-framed pictures, Coordinated picture frames",
        "score": 0.021407177671790123,
    },
    {
        "image": 5,
        "label": "Exposed wooden beams, Balcony overlooking greenery, Recessed lighting, Vaulted ceilings, Ceiling fan with light, Classical painting in gilded frame, Wall recess for art display",
        "score": 0.0023069533053785563,
    },
    {
        "image": 5,
        "label": "Striped upholstered bench, Wicker basket plant holder, Bedside lamps with cylindrical shades, Mounted wall mirrors, Dark hardwood flooring, Stainless steel appliances, Under-cabinet lighting",
        "score": 5.040161340730265e-05,
    },
    {
        "image": 5,
        "label": "Area rug with floral design, Tassel curtain tie-backs, Wooden ceiling beams, Cream-colored walls, Patterned curtains, Carved wood details on furniture",
        "score": 0.05028070881962776,
    },
    {
        "image": 5,
        "label": "Decorative bed pillows, Floral arrangement in vase, Brass door handle, White baseboards, Carved wooden vanity mirror, Patchwork quilt, Vintage telephone",
        "score": 0.9222113490104675,
    },
    {
        "image": 5,
        "label": "White painted doors, Symmetrical wall design, Rectangular wall mirror, Wall-mounted framed art, Dark wood trim, Warm ambient light, Glass in pendant lights",
        "score": 0.0006599423359148204,
    },
    {
        "image": 5,
        "label": "Black bed frame, Large window panes, A-frame ceiling, Sheer window shades, Lush greenery outside the window, Clean lines in interior architecture",
        "score": 0.0005710954428650439,
    },
    {
        "image": 5,
        "label": "High ceilings, Compact living space, Flush mounted ceiling lights, Orange-red color accents, Recessed wall nooks, White door frames, Accent lighting in art niche",
        "score": 0.0006084307678975165,
    },
    {
        "image": 5,
        "label": "Red window blinds, Sleek wardrobe handles, Visible texture in wooden flooring, Single bed with brown cover, Beige throw pillow, Patterned wallpaper accent wall",
        "score": 0.0013032559072598815,
    },
    {
        "image": 5,
        "label": "Hardwood flooring, Nightstands with drawers, Light filtering through windows, Spacious and airy atmosphere, Wall-mounted flat-screen TV, City view",
        "score": 0.000600729021243751,
    },
    {
        "image": 6,
        "label": "Decorative ceramic vases, High baseboards, Beige upholstered bench, Cable railing on staircase, Light switch plates, Matching wood-framed pictures, Coordinated picture frames",
        "score": 0.03346812725067139,
    },
    {
        "image": 6,
        "label": "Exposed wooden beams, Balcony overlooking greenery, Recessed lighting, Vaulted ceilings, Ceiling fan with light, Classical painting in gilded frame, Wall recess for art display",
        "score": 0.03200618550181389,
    },
    {
        "image": 6,
        "label": "Striped upholstered bench, Wicker basket plant holder, Bedside lamps with cylindrical shades, Mounted wall mirrors, Dark hardwood flooring, Stainless steel appliances, Under-cabinet lighting",
        "score": 0.0491420216858387,
    },
    {
        "image": 6,
        "label": "Area rug with floral design, Tassel curtain tie-backs, Wooden ceiling beams, Cream-colored walls, Patterned curtains, Carved wood details on furniture",
        "score": 0.03480791673064232,
    },
    {
        "image": 6,
        "label": "Decorative bed pillows, Floral arrangement in vase, Brass door handle, White baseboards, Carved wooden vanity mirror, Patchwork quilt, Vintage telephone",
        "score": 0.0021854720544070005,
    },
    {
        "image": 6,
        "label": "White painted doors, Symmetrical wall design, Rectangular wall mirror, Wall-mounted framed art, Dark wood trim, Warm ambient light, Glass in pendant lights",
        "score": 0.8110162615776062,
    },
    {
        "image": 6,
        "label": "Black bed frame, Large window panes, A-frame ceiling, Sheer window shades, Lush greenery outside the window, Clean lines in interior architecture",
        "score": 0.001296411151997745,
    },
    {
        "image": 6,
        "label": "High ceilings, Compact living space, Flush mounted ceiling lights, Orange-red color accents, Recessed wall nooks, White door frames, Accent lighting in art niche",
        "score": 0.020242609083652496,
    },
    {
        "image": 6,
        "label": "Red window blinds, Sleek wardrobe handles, Visible texture in wooden flooring, Single bed with brown cover, Beige throw pillow, Patterned wallpaper accent wall",
        "score": 0.0008242691983468831,
    },
    {
        "image": 6,
        "label": "Hardwood flooring, Nightstands with drawers, Light filtering through windows, Spacious and airy atmosphere, Wall-mounted flat-screen TV, City view",
        "score": 0.01501078624278307,
    },
    {
        "image": 7,
        "label": "Decorative ceramic vases, High baseboards, Beige upholstered bench, Cable railing on staircase, Light switch plates, Matching wood-framed pictures, Coordinated picture frames",
        "score": 0.0002740768832154572,
    },
    {
        "image": 7,
        "label": "Exposed wooden beams, Balcony overlooking greenery, Recessed lighting, Vaulted ceilings, Ceiling fan with light, Classical painting in gilded frame, Wall recess for art display",
        "score": 0.038699135184288025,
    },
    {
        "image": 7,
        "label": "Striped upholstered bench, Wicker basket plant holder, Bedside lamps with cylindrical shades, Mounted wall mirrors, Dark hardwood flooring, Stainless steel appliances, Under-cabinet lighting",
        "score": 0.00016422678891103715,
    },
    {
        "image": 7,
        "label": "Area rug with floral design, Tassel curtain tie-backs, Wooden ceiling beams, Cream-colored walls, Patterned curtains, Carved wood details on furniture",
        "score": 2.445568679831922e-05,
    },
    {
        "image": 7,
        "label": "Decorative bed pillows, Floral arrangement in vase, Brass door handle, White baseboards, Carved wooden vanity mirror, Patchwork quilt, Vintage telephone",
        "score": 1.4303864190878812e-05,
    },
    {
        "image": 7,
        "label": "White painted doors, Symmetrical wall design, Rectangular wall mirror, Wall-mounted framed art, Dark wood trim, Warm ambient light, Glass in pendant lights",
        "score": 0.00015331624308601022,
    },
    {
        "image": 7,
        "label": "Black bed frame, Large window panes, A-frame ceiling, Sheer window shades, Lush greenery outside the window, Clean lines in interior architecture",
        "score": 0.9480457305908203,
    },
    {
        "image": 7,
        "label": "High ceilings, Compact living space, Flush mounted ceiling lights, Orange-red color accents, Recessed wall nooks, White door frames, Accent lighting in art niche",
        "score": 0.0003008971980307251,
    },
    {
        "image": 7,
        "label": "Red window blinds, Sleek wardrobe handles, Visible texture in wooden flooring, Single bed with brown cover, Beige throw pillow, Patterned wallpaper accent wall",
        "score": 0.0002748052647802979,
    },
    {
        "image": 7,
        "label": "Hardwood flooring, Nightstands with drawers, Light filtering through windows, Spacious and airy atmosphere, Wall-mounted flat-screen TV, City view",
        "score": 0.012049158103764057,
    },
    {
        "image": 8,
        "label": "Decorative ceramic vases, High baseboards, Beige upholstered bench, Cable railing on staircase, Light switch plates, Matching wood-framed pictures, Coordinated picture frames",
        "score": 0.007962328381836414,
    },
    {
        "image": 8,
        "label": "Exposed wooden beams, Balcony overlooking greenery, Recessed lighting, Vaulted ceilings, Ceiling fan with light, Classical painting in gilded frame, Wall recess for art display",
        "score": 0.0022766985930502415,
    },
    {
        "image": 8,
        "label": "Striped upholstered bench, Wicker basket plant holder, Bedside lamps with cylindrical shades, Mounted wall mirrors, Dark hardwood flooring, Stainless steel appliances, Under-cabinet lighting",
        "score": 0.001018251059576869,
    },
    {
        "image": 8,
        "label": "Area rug with floral design, Tassel curtain tie-backs, Wooden ceiling beams, Cream-colored walls, Patterned curtains, Carved wood details on furniture",
        "score": 2.4946832127170637e-05,
    },
    {
        "image": 8,
        "label": "Decorative bed pillows, Floral arrangement in vase, Brass door handle, White baseboards, Carved wooden vanity mirror, Patchwork quilt, Vintage telephone",
        "score": 4.927747795591131e-05,
    },
    {
        "image": 8,
        "label": "White painted doors, Symmetrical wall design, Rectangular wall mirror, Wall-mounted framed art, Dark wood trim, Warm ambient light, Glass in pendant lights",
        "score": 0.032065607607364655,
    },
    {
        "image": 8,
        "label": "Black bed frame, Large window panes, A-frame ceiling, Sheer window shades, Lush greenery outside the window, Clean lines in interior architecture",
        "score": 0.00013017700985074043,
    },
    {
        "image": 8,
        "label": "High ceilings, Compact living space, Flush mounted ceiling lights, Orange-red color accents, Recessed wall nooks, White door frames, Accent lighting in art niche",
        "score": 0.9195760488510132,
    },
    {
        "image": 8,
        "label": "Red window blinds, Sleek wardrobe handles, Visible texture in wooden flooring, Single bed with brown cover, Beige throw pillow, Patterned wallpaper accent wall",
        "score": 0.001061023329384625,
    },
    {
        "image": 8,
        "label": "Hardwood flooring, Nightstands with drawers, Light filtering through windows, Spacious and airy atmosphere, Wall-mounted flat-screen TV, City view",
        "score": 0.0358356237411499,
    },
    {
        "image": 9,
        "label": "Decorative ceramic vases, High baseboards, Beige upholstered bench, Cable railing on staircase, Light switch plates, Matching wood-framed pictures, Coordinated picture frames",
        "score": 0.018824502825737,
    },
    {
        "image": 9,
        "label": "Exposed wooden beams, Balcony overlooking greenery, Recessed lighting, Vaulted ceilings, Ceiling fan with light, Classical painting in gilded frame, Wall recess for art display",
        "score": 0.005253944080322981,
    },
    {
        "image": 9,
        "label": "Striped upholstered bench, Wicker basket plant holder, Bedside lamps with cylindrical shades, Mounted wall mirrors, Dark hardwood flooring, Stainless steel appliances, Under-cabinet lighting",
        "score": 0.008123821578919888,
    },
    {
        "image": 9,
        "label": "Area rug with floral design, Tassel curtain tie-backs, Wooden ceiling beams, Cream-colored walls, Patterned curtains, Carved wood details on furniture",
        "score": 0.001224602572619915,
    },
    {
        "image": 9,
        "label": "Decorative bed pillows, Floral arrangement in vase, Brass door handle, White baseboards, Carved wooden vanity mirror, Patchwork quilt, Vintage telephone",
        "score": 0.012653055600821972,
    },
    {
        "image": 9,
        "label": "White painted doors, Symmetrical wall design, Rectangular wall mirror, Wall-mounted framed art, Dark wood trim, Warm ambient light, Glass in pendant lights",
        "score": 0.006772847380489111,
    },
    {
        "image": 9,
        "label": "Black bed frame, Large window panes, A-frame ceiling, Sheer window shades, Lush greenery outside the window, Clean lines in interior architecture",
        "score": 0.024344459176063538,
    },
    {
        "image": 9,
        "label": "High ceilings, Compact living space, Flush mounted ceiling lights, Orange-red color accents, Recessed wall nooks, White door frames, Accent lighting in art niche",
        "score": 0.044314030557870865,
    },
    {
        "image": 9,
        "label": "Red window blinds, Sleek wardrobe handles, Visible texture in wooden flooring, Single bed with brown cover, Beige throw pillow, Patterned wallpaper accent wall",
        "score": 0.5058093070983887,
    },
    {
        "image": 9,
        "label": "Hardwood flooring, Nightstands with drawers, Light filtering through windows, Spacious and airy atmosphere, Wall-mounted flat-screen TV, City view",
        "score": 0.37267953157424927,
    },
    {
        "image": 10,
        "label": "Decorative ceramic vases, High baseboards, Beige upholstered bench, Cable railing on staircase, Light switch plates, Matching wood-framed pictures, Coordinated picture frames",
        "score": 0.0008284780778922141,
    },
    {
        "image": 10,
        "label": "Exposed wooden beams, Balcony overlooking greenery, Recessed lighting, Vaulted ceilings, Ceiling fan with light, Classical painting in gilded frame, Wall recess for art display",
        "score": 0.00047125553828664124,
    },
    {
        "image": 10,
        "label": "Striped upholstered bench, Wicker basket plant holder, Bedside lamps with cylindrical shades, Mounted wall mirrors, Dark hardwood flooring, Stainless steel appliances, Under-cabinet lighting",
        "score": 0.0002890565665438771,
    },
    {
        "image": 10,
        "label": "Area rug with floral design, Tassel curtain tie-backs, Wooden ceiling beams, Cream-colored walls, Patterned curtains, Carved wood details on furniture",
        "score": 5.929873168497579e-06,
    },
    {
        "image": 10,
        "label": "Decorative bed pillows, Floral arrangement in vase, Brass door handle, White baseboards, Carved wooden vanity mirror, Patchwork quilt, Vintage telephone",
        "score": 5.695827894669492e-06,
    },
    {
        "image": 10,
        "label": "White painted doors, Symmetrical wall design, Rectangular wall mirror, Wall-mounted framed art, Dark wood trim, Warm ambient light, Glass in pendant lights",
        "score": 0.002019317587837577,
    },
    {
        "image": 10,
        "label": "Black bed frame, Large window panes, A-frame ceiling, Sheer window shades, Lush greenery outside the window, Clean lines in interior architecture",
        "score": 0.004182156175374985,
    },
    {
        "image": 10,
        "label": "High ceilings, Compact living space, Flush mounted ceiling lights, Orange-red color accents, Recessed wall nooks, White door frames, Accent lighting in art niche",
        "score": 0.003932835999876261,
    },
    {
        "image": 10,
        "label": "Red window blinds, Sleek wardrobe handles, Visible texture in wooden flooring, Single bed with brown cover, Beige throw pillow, Patterned wallpaper accent wall",
        "score": 6.805214798077941e-05,
    },
    {
        "image": 10,
        "label": "Hardwood flooring, Nightstands with drawers, Light filtering through windows, Spacious and airy atmosphere, Wall-mounted flat-screen TV, City view",
        "score": 0.988197386264801,
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
