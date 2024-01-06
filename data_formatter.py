from collections import OrderedDict


def format_for_evaluation(results):
    formatted_results = {}
    for result in results:
        image_score_label = f"image{result['image']}_score"
        if image_score_label not in formatted_results:
            formatted_results[image_score_label] = {}
        formatted_results[image_score_label][result["label"]] = result["score"]
    return formatted_results


def format_for_visualization(results):
    # labels = list(set([result["label"] for result in results]))
    labels = list(
        OrderedDict.fromkeys(
            result["label"] for result in results if result["image"] == 1
        )
    )
    formatted_results = []
    for label in labels:
        label_results = {"label": label}
        label_results.update(
            {
                f"image{result['image']}_score": result["score"]
                for result in results
                if result["label"] == label
            }
        )
        formatted_results.append(label_results)
    return formatted_results
