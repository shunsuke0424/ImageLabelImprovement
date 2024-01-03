from transformers import pipeline
import random

image_urls = [
    "https://baseline-images-repository.s3.ap-northeast-1.amazonaws.com/2d9efbd449f54a8ca2d563f9fab3e9bc.jpg",
    "https://baseline-images-repository.s3.ap-northeast-1.amazonaws.com/3ecb492d5019411785bab293ff4f74ee.jpg",
    "https://baseline-images-repository.s3.ap-northeast-1.amazonaws.com/4cc8ffa4a220460f974971ef2da47296.jpg",
    "https://baseline-images-repository.s3.ap-northeast-1.amazonaws.com/14a8edbbe4b14a05b1b5782a884fb6bf.jpg",
]
labels = [
    "Vaulted ceilings, Exposed wooden beams, Recessed lighting, White ceiling panels, Arched doorways, Hardwood floors, Wrought iron balcony railing, Outdoor lantern-style light fixture, Heavy drapery, Neutral wall color, Decorative window valances, Wrought iron bed frame, Patchwork quilt, Decorative throw pillows, White bed linens, Bedside lamps with bell shades, Framed wall mirror, Wall-mounted light fixtures, Intricate area rugs, Ornate wood furniture, Upholstered armchair, Wood-paneled lower walls, French doors leading to balcony, Balcony overlooking greenery, Classical painting in gilded frame, Beige upholstered bench, Carved wood headboard, Plush white carpet, Stone fireplace, Fire burning in fireplace, Sun design on fireplace mantel, Chandelier with candle-style lights, High-backed wooden chair, Leather ottoman, Vaulted ceiling in living area, Wall sconces with dome shades, Wooden writing desk, Decorative plates on the wall, Cast iron coat hanger, Wooden staircase, Recessed wall niche, Built-in wooden shelving, Flat-screen TV, Ceiling fan with light, Tall wooden armoire, Wall recess for art display, Small wooden side table, Decorative vase on table, Wooden floor vent, Wooden door with glass panes",
    "Coffered ceilings, Recessed lighting, Gray wall paint, White trim and molding, Dark hardwood flooring, Contemporary kitchen cabinets, Stainless steel appliances, Light granite countertops, Under-cabinet lighting, French doors with transom windows, Framed botanical prints, Cream upholstered armchair, Decorative bed pillows, Tufted fabric headboard, Gray patterned bedding, Plush throw blanket, Glass-top side tables, Mounted wall mirrors, Wooden dresser with curved design, Woven area rug, White ceiling fan, Large window with mountain view, Heavy fabric curtains, Wooden blinds, Decorative wall art, Round wooden side table, Beige fabric ottoman, Indoor potted plants, Wicker basket plant holder, Wooden crate used as shelf, Assorted decorative objects on dresser, White vase with greenery, Striped upholstered bench, White baseboards, Wall cutout looking into kitchen, Abstract sculpture on kitchen counter, Silver drawer pulls, Ceramic canisters on counter, Light switch plates, Dark wood entry door, Off-white ceiling, Two-toned kitchen cabinetry, Stacked stone backsplash, Kitchen sink with gooseneck faucet, Bedside lamps with cylindrical shades, Beige carpet runner, Black metal table legs, Wood and metal staircase railing, Decorative straw hats on wall, Distressed wood mirror frame",
    "Beamed ceiling, Wooden ceiling beams, Recessed lighting, Cream-colored walls, Hardwood floors, Arched wooden door, Arched doorways, Framed floral artwork, Wrought iron chandelier, Patterned curtains, Ornate curtain rods, Glass-paneled windows, Wooden armchair, Patterned fabric on chair, Decorative throw pillow, Wooden side table, Table lamp with beige shade, Wrought iron bed frame, Quilted bedspread, Decorative bed pillows, Carved wooden headboard, Matching wooden footboard, Intricate area rug, Brass door handles, Wall-mounted mirror, Dark wood furniture, Stone-top bedside table, Vintage-style telephone, Tassel curtain tie-backs, Embellished trunk, Beaded table lamp, Patterned vase, Wooden floor vent, Dark wood closet doors, White ceiling, Bedside reading light, Floral bed linens, Area rug with floral design, Dark wood baseboards, Warm-toned wood finishes, Textured ceiling finish, Small framed wall art, Carved wood details on furniture, Light switch plates, Cozy room atmosphere, Air vent in ceiling, Sheer curtain under drapery, Hinged closet door, Soft natural light, Traditional room decor",
    "A-frame ceiling, Exposed dark beams, White painted ceiling boards, Large window panes, Black vertical window frames, Recessed ceiling lights, Wall-mounted air vents, Sheer window shades, Gray walls, Dark hardwood flooring, Floating staircase with metal railing, Purple bedspread, White baseboards, Minimalist interior design, Open floor plan, Stainless steel kitchen appliances, White kitchen cabinetry, Kitchen island with bar seating, Glass pendant lights over kitchen island, Modern white freestanding bathtub, Chrome bath filler, Tile flooring in the bathroom, Mounted towel warmer, Square wall-mounted sink, Frameless circular wall mirror, Elevated bedroom area, Purple flooring in bedroom area, Wall-mounted bedside lamps, Black metal staircase spindles, Ceiling-mounted projector, Black curtain dividing the room, Wall-mounted flat-screen TV, Light wood paneling on lower walls, White tiled walls in the bathroom, Contemporary art on the wall, Sliding door leading to the bathroom, Black bed frame, White bed linens, Black ceiling fan, Open shelving in the kitchen, Metal heating radiators, Lush greenery outside the window, White interior doors, Stacked books on the kitchen counter, White countertops, Built-in kitchen oven, Inset cooktop on the island, Clean lines in interior architecture, Downlights in kitchen area, Multi-level living spaces",
]
# 単語数の宣言
word_count = 9
# 初回のラベル選択
random_labels = [
    [word.strip() for word in random.sample(label.split(","), word_count)]
    if len(label.split(",")) >= word_count
    else [word.strip() for word in label.split(",")]
    for label in labels
]


results = {f"image{i+1}_score": {} for i in range(len(image_urls))}
model_name = "openai/clip-vit-large-patch14-336"

classifier = pipeline("zero-shot-image-classification", model=model_name)

for i, image_url in enumerate(image_urls):
    scores = classifier(image_url, candidate_labels=random_labels)
    for j, score in enumerate(scores):
        results[f"image{i+1}_score"][f"label{j+1}"] = score["score"] * 1000

print(results)


def zero_shot_classification(image_urls, labels):
    results = []
    # モデル名を指定します。ここではOpenAIのCLIPモデルを使用します。
    model_name = "openai/clip-vit-large-patch14-336"

    # Zero-shot image classificationパイプラインを作成します。
    classifier = pipeline("zero-shot-image-classification", model=model_name)
    # 初期の結果リストを作成します。各ラベルに対して、スコアを格納した辞書を作成し、リストに追加します。
    for label in labels:
        results.append({"label": label})

    for i, image_url in enumerate(image_urls):
        scores = classifier(image_url, candidate_labels=labels)
        for score in scores:
            for result in results:
                if result["label"] == score["label"]:
                    result.update({f"image{i+1}_score": score["score"]})
    print(results)
    return results
