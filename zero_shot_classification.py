from transformers import pipeline

image_urls = [
    "https://baseline-images-repository.s3.ap-northeast-1.amazonaws.com/0f42320ef887416fb8ed9b91b6641cfc.jpg",
    "https://baseline-images-repository.s3.ap-northeast-1.amazonaws.com/2d9efbd449f54a8ca2d563f9fab3e9bc.jpg",
    "https://baseline-images-repository.s3.ap-northeast-1.amazonaws.com/3ecb492d5019411785bab293ff4f74ee.jpg",
    "https://baseline-images-repository.s3.ap-northeast-1.amazonaws.com/4cc8ffa4a220460f974971ef2da47296.jpg",
    "https://baseline-images-repository.s3.ap-northeast-1.amazonaws.com/8d51f41d9ce04dfdaae944da9c6d3847.jpg",
    "https://baseline-images-repository.s3.ap-northeast-1.amazonaws.com/9c4a59f437744d9c9b91e936def4b540.jpg",
    "https://baseline-images-repository.s3.ap-northeast-1.amazonaws.com/14a8edbbe4b14a05b1b5782a884fb6bf.jpg",
    "https://baseline-images-repository.s3.ap-northeast-1.amazonaws.com/126fdbcf213d4d5d95674ccba62fc72b.jpg",
    "https://baseline-images-repository.s3.ap-northeast-1.amazonaws.com/980150b99a2946a0894c33df8fb616d2.jpg",
    "https://baseline-images-repository.s3.ap-northeast-1.amazonaws.com/0f5c56e60cbf429eb30903125c3035b6.jpg",
]
labels = [
    "a neutral color palette with a wainscoted wall, decorative vases on a wooden dresser, and a bed with patterned throw pillows against a backdrop of large windows offering a view of the landscape.",
    "a luxurious bedroom with a vaulted ceiling featuring wooden beams, an ornate wrought iron bed frame, and an elegant fireplace as focal points.",
    "a neutral color palette, with hardwood floors and contemporary decor, including a cozy bed, a dresser with a curved front, and multiple round mirrors on the wall.",
    "a traditional wooden four-poster bed with pink and white bedding, an ornate wrought iron chandelier, and dark wood flooring that complements the arched wooden doors.",
    "floral wallpaper, antique wooden furniture, and a patterned quilt on the bed.",
    "elegant wall paneling, a unique striped wallpaper, and a cozy bed with plush pillows.",
    "a high vaulted ceiling with exposed dark wooden beams, a large bed with a purple comforter, and expansive windows that allow for plenty of natural light.",
    "modern and minimalist with a striking red storage bench, a single abstract painting on the wall, and a bed dressed in gray with red accent pillows.",
    "a decorative red and black patterned wallpaper on one wall, a modern low-profile bed with a brown cover, and a minimalist cream-colored chaise lounge with a matching pillow.",
    "a large bed with decorative pillows, a modern chaise lounge by a wide window offering an expansive view, and contemporary art pieces on the walls.",
]

results = {f"image{i+1}_score": {} for i in range(len(image_urls))}
model_name = "openai/clip-vit-large-patch14-336"

classifier = pipeline("zero-shot-image-classification", model=model_name)

for i, image_url in enumerate(image_urls):
    scores = classifier(image_url, candidate_labels=labels)
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
