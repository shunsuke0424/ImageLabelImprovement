import matplotlib.pyplot as plt
import numpy as np
from data_formatter import format_for_visualization

zeroshot_result_data = [
    {
        "image": 1,
        "label": "Textured carpet flooring, Contemporary wall sconces, Geometric picture frames",
        "score": 0.7875693440437317,
    },
    {
        "image": 1,
        "label": "Recessed lighting, Vaulted ceilings, Cast iron coat hanger",
        "score": 0.008012184873223305,
    },
    {
        "image": 1,
        "label": "Two-toned kitchen cabinetry, Wood and metal staircase railing, Mounted wall mirrors",
        "score": 0.10904508829116821,
    },
    {
        "image": 1,
        "label": "Tassel curtain tie-backs, Wooden ceiling beams, Hardwood floors",
        "score": 0.023065686225891113,
    },
    {
        "image": 1,
        "label": "White ceiling, White painted radiator, Porcelain table lamps",
        "score": 0.02004493772983551,
    },
    {
        "image": 1,
        "label": "Striped wallpaper, Dual pendant lights, Paneled walls",
        "score": 0.025290988385677338,
    },
    {
        "image": 1,
        "label": "Black metal staircase spindles, A-frame ceiling, Black vertical window frames",
        "score": 0.006979693192988634,
    },
    {
        "image": 1,
        "label": "Recessed wall nooks, Orange-red color accents, Abstract graffiti wall art",
        "score": 0.008154937997460365,
    },
    {
        "image": 1,
        "label": "Visible texture in wooden flooring, Single bed with brown cover, Clean lines in room design",
        "score": 0.005675522144883871,
    },
    {
        "image": 1,
        "label": "Light filtering through windows, Shadow play on walls, White sheer curtains",
        "score": 0.0061616492457687855,
    },
    {
        "image": 2,
        "label": "Textured carpet flooring, Contemporary wall sconces, Geometric picture frames",
        "score": 0.036659177392721176,
    },
    {
        "image": 2,
        "label": "Recessed lighting, Vaulted ceilings, Cast iron coat hanger",
        "score": 0.39860713481903076,
    },
    {
        "image": 2,
        "label": "Two-toned kitchen cabinetry, Wood and metal staircase railing, Mounted wall mirrors",
        "score": 0.003953063860535622,
    },
    {
        "image": 2,
        "label": "Tassel curtain tie-backs, Wooden ceiling beams, Hardwood floors",
        "score": 0.2137826830148697,
    },
    {
        "image": 2,
        "label": "White ceiling, White painted radiator, Porcelain table lamps",
        "score": 0.09125161170959473,
    },
    {
        "image": 2,
        "label": "Striped wallpaper, Dual pendant lights, Paneled walls",
        "score": 0.0389985665678978,
    },
    {
        "image": 2,
        "label": "Black metal staircase spindles, A-frame ceiling, Black vertical window frames",
        "score": 0.012455398216843605,
    },
    {
        "image": 2,
        "label": "Recessed wall nooks, Orange-red color accents, Abstract graffiti wall art",
        "score": 0.08428487926721573,
    },
    {
        "image": 2,
        "label": "Visible texture in wooden flooring, Single bed with brown cover, Clean lines in room design",
        "score": 0.07602531462907791,
    },
    {
        "image": 2,
        "label": "Light filtering through windows, Shadow play on walls, White sheer curtains",
        "score": 0.04398220404982567,
    },
    {
        "image": 3,
        "label": "Textured carpet flooring, Contemporary wall sconces, Geometric picture frames",
        "score": 0.24684827029705048,
    },
    {
        "image": 3,
        "label": "Recessed lighting, Vaulted ceilings, Cast iron coat hanger",
        "score": 0.03283807262778282,
    },
    {
        "image": 3,
        "label": "Two-toned kitchen cabinetry, Wood and metal staircase railing, Mounted wall mirrors",
        "score": 0.06940532475709915,
    },
    {
        "image": 3,
        "label": "Tassel curtain tie-backs, Wooden ceiling beams, Hardwood floors",
        "score": 0.04177379608154297,
    },
    {
        "image": 3,
        "label": "White ceiling, White painted radiator, Porcelain table lamps",
        "score": 0.11591898649930954,
    },
    {
        "image": 3,
        "label": "Striped wallpaper, Dual pendant lights, Paneled walls",
        "score": 0.2397647351026535,
    },
    {
        "image": 3,
        "label": "Black metal staircase spindles, A-frame ceiling, Black vertical window frames",
        "score": 0.013189186342060566,
    },
    {
        "image": 3,
        "label": "Recessed wall nooks, Orange-red color accents, Abstract graffiti wall art",
        "score": 0.004029109142720699,
    },
    {
        "image": 3,
        "label": "Visible texture in wooden flooring, Single bed with brown cover, Clean lines in room design",
        "score": 0.183978870511055,
    },
    {
        "image": 3,
        "label": "Light filtering through windows, Shadow play on walls, White sheer curtains",
        "score": 0.052253663539886475,
    },
    {
        "image": 4,
        "label": "Textured carpet flooring, Contemporary wall sconces, Geometric picture frames",
        "score": 0.0038389507681131363,
    },
    {
        "image": 4,
        "label": "Recessed lighting, Vaulted ceilings, Cast iron coat hanger",
        "score": 0.010682470165193081,
    },
    {
        "image": 4,
        "label": "Two-toned kitchen cabinetry, Wood and metal staircase railing, Mounted wall mirrors",
        "score": 0.00018166692461818457,
    },
    {
        "image": 4,
        "label": "Tassel curtain tie-backs, Wooden ceiling beams, Hardwood floors",
        "score": 0.8954620361328125,
    },
    {
        "image": 4,
        "label": "White ceiling, White painted radiator, Porcelain table lamps",
        "score": 0.0014428832801058888,
    },
    {
        "image": 4,
        "label": "Striped wallpaper, Dual pendant lights, Paneled walls",
        "score": 0.038501642644405365,
    },
    {
        "image": 4,
        "label": "Black metal staircase spindles, A-frame ceiling, Black vertical window frames",
        "score": 0.0005327301332727075,
    },
    {
        "image": 4,
        "label": "Recessed wall nooks, Orange-red color accents, Abstract graffiti wall art",
        "score": 0.0005751469288952649,
    },
    {
        "image": 4,
        "label": "Visible texture in wooden flooring, Single bed with brown cover, Clean lines in room design",
        "score": 0.043088555335998535,
    },
    {
        "image": 4,
        "label": "Light filtering through windows, Shadow play on walls, White sheer curtains",
        "score": 0.0056937867775559425,
    },
    {
        "image": 5,
        "label": "Textured carpet flooring, Contemporary wall sconces, Geometric picture frames",
        "score": 0.02443660981953144,
    },
    {
        "image": 5,
        "label": "Recessed lighting, Vaulted ceilings, Cast iron coat hanger",
        "score": 0.013605095446109772,
    },
    {
        "image": 5,
        "label": "Two-toned kitchen cabinetry, Wood and metal staircase railing, Mounted wall mirrors",
        "score": 0.0024198289029300213,
    },
    {
        "image": 5,
        "label": "Tassel curtain tie-backs, Wooden ceiling beams, Hardwood floors",
        "score": 0.013137205503880978,
    },
    {
        "image": 5,
        "label": "White ceiling, White painted radiator, Porcelain table lamps",
        "score": 0.6521468162536621,
    },
    {
        "image": 5,
        "label": "Striped wallpaper, Dual pendant lights, Paneled walls",
        "score": 0.15572522580623627,
    },
    {
        "image": 5,
        "label": "Black metal staircase spindles, A-frame ceiling, Black vertical window frames",
        "score": 0.002176794223487377,
    },
    {
        "image": 5,
        "label": "Recessed wall nooks, Orange-red color accents, Abstract graffiti wall art",
        "score": 0.0014361548237502575,
    },
    {
        "image": 5,
        "label": "Visible texture in wooden flooring, Single bed with brown cover, Clean lines in room design",
        "score": 0.05001163110136986,
    },
    {
        "image": 5,
        "label": "Light filtering through windows, Shadow play on walls, White sheer curtains",
        "score": 0.08490470796823502,
    },
    {
        "image": 6,
        "label": "Textured carpet flooring, Contemporary wall sconces, Geometric picture frames",
        "score": 0.001184821012429893,
    },
    {
        "image": 6,
        "label": "Recessed lighting, Vaulted ceilings, Cast iron coat hanger",
        "score": 0.0002682299818843603,
    },
    {
        "image": 6,
        "label": "Two-toned kitchen cabinetry, Wood and metal staircase railing, Mounted wall mirrors",
        "score": 0.011353273876011372,
    },
    {
        "image": 6,
        "label": "Tassel curtain tie-backs, Wooden ceiling beams, Hardwood floors",
        "score": 0.0013269467744976282,
    },
    {
        "image": 6,
        "label": "White ceiling, White painted radiator, Porcelain table lamps",
        "score": 0.0036191579420119524,
    },
    {
        "image": 6,
        "label": "Striped wallpaper, Dual pendant lights, Paneled walls",
        "score": 0.9809102416038513,
    },
    {
        "image": 6,
        "label": "Black metal staircase spindles, A-frame ceiling, Black vertical window frames",
        "score": 0.0003646108671091497,
    },
    {
        "image": 6,
        "label": "Recessed wall nooks, Orange-red color accents, Abstract graffiti wall art",
        "score": 0.0002158822608180344,
    },
    {
        "image": 6,
        "label": "Visible texture in wooden flooring, Single bed with brown cover, Clean lines in room design",
        "score": 0.0004936167970299721,
    },
    {
        "image": 6,
        "label": "Light filtering through windows, Shadow play on walls, White sheer curtains",
        "score": 0.000263213092694059,
    },
    {
        "image": 7,
        "label": "Textured carpet flooring, Contemporary wall sconces, Geometric picture frames",
        "score": 0.0002234786661574617,
    },
    {
        "image": 7,
        "label": "Recessed lighting, Vaulted ceilings, Cast iron coat hanger",
        "score": 0.0014809862477704883,
    },
    {
        "image": 7,
        "label": "Two-toned kitchen cabinetry, Wood and metal staircase railing, Mounted wall mirrors",
        "score": 0.00048338601482100785,
    },
    {
        "image": 7,
        "label": "Tassel curtain tie-backs, Wooden ceiling beams, Hardwood floors",
        "score": 0.03652079030871391,
    },
    {
        "image": 7,
        "label": "White ceiling, White painted radiator, Porcelain table lamps",
        "score": 0.00030545558547601104,
    },
    {
        "image": 7,
        "label": "Striped wallpaper, Dual pendant lights, Paneled walls",
        "score": 0.001627721474505961,
    },
    {
        "image": 7,
        "label": "Black metal staircase spindles, A-frame ceiling, Black vertical window frames",
        "score": 0.9081065654754639,
    },
    {
        "image": 7,
        "label": "Recessed wall nooks, Orange-red color accents, Abstract graffiti wall art",
        "score": 6.289999146247283e-05,
    },
    {
        "image": 7,
        "label": "Visible texture in wooden flooring, Single bed with brown cover, Clean lines in room design",
        "score": 0.04084576293826103,
    },
    {
        "image": 7,
        "label": "Light filtering through windows, Shadow play on walls, White sheer curtains",
        "score": 0.010343018919229507,
    },
    {
        "image": 8,
        "label": "Textured carpet flooring, Contemporary wall sconces, Geometric picture frames",
        "score": 0.0026001008227467537,
    },
    {
        "image": 8,
        "label": "Recessed lighting, Vaulted ceilings, Cast iron coat hanger",
        "score": 8.941252599470317e-05,
    },
    {
        "image": 8,
        "label": "Two-toned kitchen cabinetry, Wood and metal staircase railing, Mounted wall mirrors",
        "score": 0.03440655767917633,
    },
    {
        "image": 8,
        "label": "Tassel curtain tie-backs, Wooden ceiling beams, Hardwood floors",
        "score": 2.2067315512686037e-05,
    },
    {
        "image": 8,
        "label": "White ceiling, White painted radiator, Porcelain table lamps",
        "score": 0.0025635329075157642,
    },
    {
        "image": 8,
        "label": "Striped wallpaper, Dual pendant lights, Paneled walls",
        "score": 0.0023911665193736553,
    },
    {
        "image": 8,
        "label": "Black metal staircase spindles, A-frame ceiling, Black vertical window frames",
        "score": 0.0002405781706329435,
    },
    {
        "image": 8,
        "label": "Recessed wall nooks, Orange-red color accents, Abstract graffiti wall art",
        "score": 0.9535468220710754,
    },
    {
        "image": 8,
        "label": "Visible texture in wooden flooring, Single bed with brown cover, Clean lines in room design",
        "score": 0.003998490050435066,
    },
    {
        "image": 8,
        "label": "Light filtering through windows, Shadow play on walls, White sheer curtains",
        "score": 0.00014127520262263715,
    },
    {
        "image": 9,
        "label": "Textured carpet flooring, Contemporary wall sconces, Geometric picture frames",
        "score": 0.12703470885753632,
    },
    {
        "image": 9,
        "label": "Recessed lighting, Vaulted ceilings, Cast iron coat hanger",
        "score": 0.0001739908184390515,
    },
    {
        "image": 9,
        "label": "Two-toned kitchen cabinetry, Wood and metal staircase railing, Mounted wall mirrors",
        "score": 0.002160588977858424,
    },
    {
        "image": 9,
        "label": "Tassel curtain tie-backs, Wooden ceiling beams, Hardwood floors",
        "score": 0.0004201190313324332,
    },
    {
        "image": 9,
        "label": "White ceiling, White painted radiator, Porcelain table lamps",
        "score": 0.16045619547367096,
    },
    {
        "image": 9,
        "label": "Striped wallpaper, Dual pendant lights, Paneled walls",
        "score": 0.0452568456530571,
    },
    {
        "image": 9,
        "label": "Black metal staircase spindles, A-frame ceiling, Black vertical window frames",
        "score": 0.001370033947750926,
    },
    {
        "image": 9,
        "label": "Recessed wall nooks, Orange-red color accents, Abstract graffiti wall art",
        "score": 0.021695593371987343,
    },
    {
        "image": 9,
        "label": "Visible texture in wooden flooring, Single bed with brown cover, Clean lines in room design",
        "score": 0.49557745456695557,
    },
    {
        "image": 9,
        "label": "Light filtering through windows, Shadow play on walls, White sheer curtains",
        "score": 0.14585450291633606,
    },
    {
        "image": 10,
        "label": "Textured carpet flooring, Contemporary wall sconces, Geometric picture frames",
        "score": 0.07056841999292374,
    },
    {
        "image": 10,
        "label": "Recessed lighting, Vaulted ceilings, Cast iron coat hanger",
        "score": 0.002633127849549055,
    },
    {
        "image": 10,
        "label": "Two-toned kitchen cabinetry, Wood and metal staircase railing, Mounted wall mirrors",
        "score": 0.01240647491067648,
    },
    {
        "image": 10,
        "label": "Tassel curtain tie-backs, Wooden ceiling beams, Hardwood floors",
        "score": 0.0016361098969355226,
    },
    {
        "image": 10,
        "label": "White ceiling, White painted radiator, Porcelain table lamps",
        "score": 0.06201161444187164,
    },
    {
        "image": 10,
        "label": "Striped wallpaper, Dual pendant lights, Paneled walls",
        "score": 0.06864073127508163,
    },
    {
        "image": 10,
        "label": "Black metal staircase spindles, A-frame ceiling, Black vertical window frames",
        "score": 0.01750272512435913,
    },
    {
        "image": 10,
        "label": "Recessed wall nooks, Orange-red color accents, Abstract graffiti wall art",
        "score": 0.0011723802890628576,
    },
    {
        "image": 10,
        "label": "Visible texture in wooden flooring, Single bed with brown cover, Clean lines in room design",
        "score": 0.13475650548934937,
    },
    {
        "image": 10,
        "label": "Light filtering through windows, Shadow play on walls, White sheer curtains",
        "score": 0.6286720037460327,
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
