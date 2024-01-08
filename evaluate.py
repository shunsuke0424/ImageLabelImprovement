from data_formatter import format_for_evaluation, format_for_visualization


def calculate_f1_scores(zeroshot_result_data):
    data = format_for_evaluation(zeroshot_result_data)
    f1_scores = []
    labels = list(data[list(data.keys())[0]].keys())
    for j in range(len(data)):
        image_score_key = "image" + str(j + 1) + "_score"
        p_jj = data[image_score_key][labels[j]]
        sum_i = sum(
            data["image" + str(i + 1) + "_score"][labels[j]] for i in range(len(data))
        )
        precision = p_jj / sum_i if sum_i != 0 else 0
        recall = p_jj
        if precision + recall != 0:
            f1_scores.append((2 * precision * recall) / (precision + recall))
    return f1_scores


def find_low_performance_labels(zeroshot_result_data):
    data = format_for_visualization(zeroshot_result_data)
    incorrect_ratios = {}
    for i, item in enumerate(data):
        correct_label = item["label"]
        correct_image_score_key = f"image{i+1}_score"
        incorrect_scores = {
            key: value
            for key, value in item.items()
            if key != "label" and key != correct_image_score_key
        }
        highest_incorrect_score = max(incorrect_scores.values())
        correct_label_for_highest_incorrect_score = data[
            int(
                max(incorrect_scores, key=incorrect_scores.get)
                .replace("image", "")
                .replace("_score", "")
            )
            - 1
        ]["label"]
        incorrect_ratios[correct_label] = {
            "highest_incorrect_score": highest_incorrect_score,
            "correct_label_for_highest_incorrect_score": correct_label_for_highest_incorrect_score,
        }

    highest_incorrect_score_label = max(
        incorrect_ratios, key=lambda x: incorrect_ratios[x]["highest_incorrect_score"]
    )
    print(incorrect_ratios)
    # ここランダム性を持たせても面白そう、のデバッグ

    # そのスコアの本当の正解ラベルを見つける
    correct_label_for_highest_incorrect_score = incorrect_ratios[
        highest_incorrect_score_label
    ]["correct_label_for_highest_incorrect_score"]

    return highest_incorrect_score_label.split(
        ", "
    ), correct_label_for_highest_incorrect_score.split(", ")


def find_low_performance_labels_by_F1_score(zeroshot_result_data, f1_scores):
    # F1スコアが最も低いラベルのインデックスを取得
    min_f1_index = f1_scores.index(min(f1_scores))
    # F1スコアが最も低いラベルを取得するために、ラベルのリストが必要
    labels = list(
        format_for_evaluation(zeroshot_result_data)[
            list(format_for_evaluation(zeroshot_result_data).keys())[0]
        ].keys()
    )
    # 最も低いF1スコアのラベルを取得
    lowest_f1_label = labels[min_f1_index]

    # そのラベルの正解画像以外の画像のスコアで一番高い画像を見つける
    data = format_for_visualization(zeroshot_result_data)
    incorrect_scores = {}
    for item in data:
        if item["label"] == lowest_f1_label:
            for key, value in item.items():
                if key.endswith("_score") and key != f"image{min_f1_index+1}_score":
                    incorrect_scores[key] = value
            break
    highest_incorrect_image_key = max(incorrect_scores, key=incorrect_scores.get)
    highest_incorrect_image_index = (
        int(highest_incorrect_image_key.replace("image", "").replace("_score", "")) - 1
    )

    # その画像に対応する真の正解ラベルを見つける
    correct_label_for_highest_incorrect_image = data[highest_incorrect_image_index][
        "label"
    ]

    # 最終的に一番F1スコアが低いラベルと真の正解ラベルを返却する
    return lowest_f1_label.split(", "), correct_label_for_highest_incorrect_image.split(
        ", "
    )
