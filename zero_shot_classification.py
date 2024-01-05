from transformers import pipeline


def zero_shot_classification(image_urls, labels):
    model_name = "openai/clip-vit-large-patch14-336"
    classifier = pipeline("zero-shot-image-classification", model=model_name)

    results = []
    for i, image_url in enumerate(image_urls):
        scores = classifier(image_url, candidate_labels=labels)
        ordered_scores = sorted(scores, key=lambda x: labels.index(x["label"]))
        for score in ordered_scores:
            results.append(
                {
                    "image": i + 1,
                    "label": ", ".join(score["label"]),
                    "score": score["score"],
                }
            )

    return results
