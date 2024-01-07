from data_formatter import format_for_evaluation, format_for_visualization


# 以下はデータを事前に加工するか否かのコード
# 今の所そのまま直のデータを扱う方針
# for key in data.keys():
#     data[key] = {k: v * 1000 for k, v in data[key].items()}
# for key in data.keys():
#     data[key] = {k: int(v) for k, v in data[key].items()}
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
