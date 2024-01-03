from datasets.datasets import image_urls, labels
from clip_distance import calculate_similarity
from distance_data import similarity_cache


def filter_labels(
    label_number_1: int, current_label1: list, label_number_2: int, current_label2: list
):
    # ラベルをインデックスで取得
    all_label1_list = labels[label_number_1 - 1].split(", ")
    all_label2_list = labels[label_number_2 - 1].split(", ")
    image1 = image_urls[label_number_1 - 1]
    image2 = image_urls[label_number_2 - 1]

    # 1.0すでにあるももの一番遠いやつを見つける
    label_similarity_pairs_1 = []
    # 1.1current_labelsの各ラベルに対応する類似度を取得
    for label in current_label1:
        if label in similarity_cache[label_number_1 - 1]:
            # label_similarity_pairs_1.append(label)
            label_similarity_pairs_1.append(
                (label, similarity_cache[label_number_1 - 1][label])
            )
    # 1.3最小の類似度を持つラベルを選択
    min_current_label1_image1 = min(label_similarity_pairs_1, key=lambda pair: pair[1])[
        0
    ]

    # 2.0全ラベルの一番近いやつを見つける
    label1_image1_probs = similarity_cache[label_number_1 - 1]
    # 値で降順にソート
    sorted_labels_1_reverse = sorted(
        label1_image1_probs, key=label1_image1_probs.get, reverse=True
    )
    # current_label1に存在しない最初のラベルを取得
    max_label1_image1 = next(
        (label for label in sorted_labels_1_reverse if label not in current_label1),
        None,
    )

    # 3.0 all_label1とimage2の一番遠いやつ見つける
    label1_image2_probs = calculate_similarity(all_label1_list, image2)
    # 値で昇順にソート
    sorted_labels_2 = sorted(label1_image2_probs, key=label1_image2_probs.get)

    # current_label1に存在しない最初のラベルを取得
    min_label1_image2 = next(
        (label for label in sorted_labels_2 if label not in current_label1), None
    )

    # 4.0すでにあるももの一番近いやつを見つける
    # 値で降順にソート
    sorted_labels_2_reverse = sorted(
        label1_image2_probs, key=label1_image2_probs.get, reverse=True
    )
    # current_label1に存在する最初のラベルを取得
    max_current_label1_image2 = next(
        (label for label in sorted_labels_2_reverse if label in current_label1), None
    )

    # 5.0 new_label1を作成
    new_label1 = current_label1.copy()
    new_label1.remove(min_current_label1_image1)
    new_label1.append(max_label1_image1)
    new_label1.append(min_label1_image2)
    if max_current_label1_image2 in new_label1:
        new_label1.remove(max_current_label1_image2)

    # label2に関しても同様の処理
    label_similarity_pairs_2 = []
    for label in current_label2:
        if label in similarity_cache[label_number_2 - 1]:
            label_similarity_pairs_2.append(
                (label, similarity_cache[label_number_2 - 1][label])
            )
    min_current_label2_image2 = min(label_similarity_pairs_2, key=lambda pair: pair[1])[
        0
    ]

    label2_image2_probs = similarity_cache[label_number_2 - 1]
    sorted_labels_2_reverse = sorted(
        label2_image2_probs, key=label2_image2_probs.get, reverse=True
    )
    max_label2_image2 = next(
        (label for label in sorted_labels_2_reverse if label not in current_label2),
        None,
    )

    label2_image1_probs = calculate_similarity(all_label2_list, image1)
    sorted_labels_2 = sorted(label2_image1_probs, key=label2_image1_probs.get)
    min_label2_image1 = next(
        (label for label in sorted_labels_2 if label not in current_label2), None
    )

    sorted_labels_2_reverse = sorted(
        label2_image1_probs, key=label2_image1_probs.get, reverse=True
    )
    max_current_label2_image1 = next(
        (label for label in sorted_labels_2_reverse if label in current_label2), None
    )
    new_label2 = current_label2.copy()
    new_label2.remove(min_current_label2_image2)
    new_label2.append(max_label2_image2)
    new_label2.append(min_label2_image1)
    if max_current_label2_image1 in new_label2:
        new_label2.remove(max_current_label2_image1)

    # 重複を削除
    new_label1 = list(set(new_label1))
    new_label2 = list(set(new_label2))

    return new_label1, new_label2
