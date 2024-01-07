from transformers import pipeline


def zero_shot_classification(image_urls, labels):
    model_name = "openai/clip-vit-large-patch14-336"
    classifier = pipeline("zero-shot-image-classification", model=model_name)

    results = []
    for i, image_url in enumerate(image_urls):
        labels_text_list = [", ".join(labels) for labels in labels]
        scores = classifier(image_url, candidate_labels=labels_text_list)
        ordered_scores = sorted(
            scores, key=lambda x: labels_text_list.index(x["label"])
        )
        for score in ordered_scores:
            results.append(
                {
                    "image": i + 1,
                    "label": score["label"],
                    "score": score["score"],
                }
            )

    return results
