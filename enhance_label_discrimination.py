from datasets.datasets import image_urls, labels
from clip_distance import calculate_similarity
from distance_data import similarity_cache
import numpy as np


def enhance_label_discrimination(
    label_number_1: int, current_label1: list, label_number_2: int, current_label2: list
):
    # ラベルをインデックスで取得
    all_label1_list = labels[label_number_1 - 1].split(", ")
    all_label2_list = labels[label_number_2 - 1].split(", ")
    image1 = image_urls[label_number_1 - 1]
    image2 = image_urls[label_number_2 - 1]

    # 1.0すでにあるももの一番遠いやつを見つける.cur_label1 vs img1
    label_similarity_pairs_1 = []
    for label in current_label1:
        if label in similarity_cache[label_number_1 - 1]:
            label_similarity_pairs_1.append(
                (label, similarity_cache[label_number_1 - 1][label])
            )
    label_candidates, similarities = zip(*label_similarity_pairs_1)
    inverse_similarities = [1 / s for s in similarities]  # 逆数を取る
    probabilities = np.exp(inverse_similarities) / np.sum(
        np.exp(inverse_similarities)
    )  # softmaxを使用して確率分布を作成
    min_current_label1_image1 = np.random.choice(label_candidates, p=probabilities)

    # 2.0全ラベルの一番近いやつを見つける.all_label1 vs img1
    label1_image1_probs = similarity_cache[label_number_1 - 1]
    label_candidates = [
        label for label in label1_image1_probs if label not in current_label1
    ]
    similarities = [label1_image1_probs[label] for label in label_candidates]
    probabilities = np.exp(similarities) / np.sum(
        np.exp(similarities)
    )  # softmaxを使用して確率分布を作成
    max_label1_image1 = np.random.choice(label_candidates, p=probabilities)

    # 3.0 all_label1とimage2の一番遠いやつ見つける.all_label1 vs img2
    label1_image2_probs = calculate_similarity(all_label1_list, image2)
    label_candidates = [
        label for label in label1_image2_probs if label not in current_label1
    ]
    inverse_similarities = [
        1 / label1_image2_probs[label] for label in label_candidates
    ]  # 逆数を取る
    probabilities = np.exp(inverse_similarities) / np.sum(
        np.exp(inverse_similarities)
    )  # softmaxを使用して確率分布を作成
    min_label1_image2 = np.random.choice(label_candidates, p=probabilities)

    # 4.0すでにあるももの一番近いやつを見つける.cur_label1 vs img2
    label_candidates = [
        label for label in label1_image2_probs if label in current_label1
    ]
    label_candidates = [
        label
        for label in label1_image2_probs
        if label in current_label1 and label != min_current_label1_image1
    ]
    similarities = [label1_image2_probs[label] for label in label_candidates]
    probabilities = np.exp(similarities) / np.sum(
        np.exp(similarities)
    )  # softmaxを使用して確率分布を作成
    max_current_label1_image2 = np.random.choice(label_candidates, p=probabilities)

    # 5.0 new_label1を作成
    new_label1 = current_label1.copy()
    new_label1.remove(min_current_label1_image1)
    new_label1.append(max_label1_image1)
    new_label1.append(min_label1_image2)
    new_label1.remove(max_current_label1_image2)

    # label2に関しても同様の処理
    # cur_label2 vs img2
    label_similarity_pairs_2 = []
    for label in current_label2:
        if label in similarity_cache[label_number_2 - 1]:
            label_similarity_pairs_2.append(
                (label, similarity_cache[label_number_2 - 1][label])
            )
    label_candidates, similarities = zip(*label_similarity_pairs_2)
    inverse_similarities = [1 / s for s in similarities]  # 逆数を取る
    probabilities = np.exp(inverse_similarities) / np.sum(
        np.exp(inverse_similarities)
    )  # softmaxを使用して確率分布を作成
    min_current_label2_image2 = np.random.choice(label_candidates, p=probabilities)

    # all_label2 vs img2
    label2_image2_probs = similarity_cache[label_number_2 - 1]
    label_candidates = [
        label for label in label2_image2_probs if label not in current_label2
    ]
    similarities = [label2_image2_probs[label] for label in label_candidates]
    probabilities = np.exp(similarities) / np.sum(
        np.exp(similarities)
    )  # softmaxを使用して確率分布を作成
    max_label2_image2 = np.random.choice(label_candidates, p=probabilities)

    # all_label2 vs img1
    label2_image1_probs = calculate_similarity(all_label2_list, image1)
    label_candidates = [
        label for label in label2_image1_probs if label not in current_label2
    ]
    inverse_similarities = [
        1 / label2_image1_probs[label] for label in label_candidates
    ]  # 逆数を取る
    probabilities = np.exp(inverse_similarities) / np.sum(
        np.exp(inverse_similarities)
    )  # softmaxを使用して確率分布を作成
    min_label2_image1 = np.random.choice(label_candidates, p=probabilities)

    # cur_label2 vs img1
    label_candidates = [
        label
        for label in label2_image1_probs
        if label in current_label2 and label != min_current_label2_image2
    ]
    similarities = [label2_image1_probs[label] for label in label_candidates]
    probabilities = np.exp(similarities) / np.sum(
        np.exp(similarities)
    )  # softmaxを使用して確率分布を作成
    max_current_label2_image1 = np.random.choice(label_candidates, p=probabilities)

    # new_label2を作成
    new_label2 = current_label2.copy()
    new_label2.remove(min_current_label2_image2)
    new_label2.append(max_label2_image2)
    new_label2.append(min_label2_image1)
    new_label2.remove(max_current_label2_image1)

    # 重複を削除
    new_label1 = list(set(new_label1))
    new_label2 = list(set(new_label2))

    return new_label1, new_label2
