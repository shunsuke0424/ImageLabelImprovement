from datasets.datasets import image_urls, labels
from clip_distance import calculate_similarity
from distance_data import similarity_cache
import numpy as np


def enhance_label_discrimination(
    label_number_1: int, current_label1: list, label_number_2: int, current_label2: list
):
    # ラベルをインデックスで取得
    image1 = image_urls[label_number_1 - 1]
    image2 = image_urls[label_number_2 - 1]
    all_label1_list = labels[label_number_1 - 1].split(", ")
    all_label2_list = labels[label_number_2 - 1].split(", ")
    label1_image1_probs = similarity_cache[label_number_1 - 1]
    label1_image2_probs = calculate_similarity(all_label1_list, image2)
    label2_image2_probs = similarity_cache[label_number_2 - 1]
    label2_image1_probs = calculate_similarity(all_label2_list, image1)

    # 1.0すでにあるももの一番遠いやつを見つける.cur_label1 vs img1
    min_current_label1_image1 = cur_label1_vs_img1(label_number_1, current_label1)

    # 2.0全ラベルの一番近いやつを見つける.all_label1 vs img1
    max_label1_image1 = all_label1_vs_img1(
        label_number_1, current_label1, label1_image1_probs
    )

    # 3.0 all_label1とimage2の一番遠いやつ見つける.all_label1 vs img2
    min_label1_image2 = all_label1_vs_img2(
        current_label1, all_label1_list, label1_image1_probs, label1_image2_probs
    )

    # 4.0すでにあるももの一番近いやつを見つける.cur_label1 vs img2
    max_current_label1_image2 = cur_label1_vs_img2(
        current_label1,
        label1_image1_probs,
        label1_image2_probs,
        min_current_label1_image1,
    )

    # 5.0 new_label1を作成
    new_label1 = enhance_label1(
        current_label1,
        min_current_label1_image1,
        max_label1_image1,
        min_label1_image2,
        max_current_label1_image2,
    )

    # label2に関しても同様の処理
    # 1.0すでにあるももの一番遠いやつを見つける.cur_label2 vs img2
    min_current_label2_image2 = cur_label2_vs_img2(label_number_2, current_label2)

    # 2.0全ラベルの一番近いやつを見つける.all_label2 vs img2
    max_label2_image2 = all_label2_vs_img2(
        label_number_2, current_label2, label2_image2_probs
    )

    # 3.0 all_label2とimage1の一番遠いやつ見つける.all_label2 vs img1
    min_label2_image1 = all_label2_vs_img1(
        current_label2, all_label2_list, label2_image2_probs, label2_image1_probs
    )

    # 4.0すでにあるももの一番近いやつを見つける.cur_label2 vs img1
    max_current_label2_image1 = cur_label2_vs_img1(
        current_label2,
        label2_image2_probs,
        label2_image1_probs,
        min_current_label2_image2,
    )

    # 5.0 new_label2を作成
    new_label2 = enhance_label2(
        current_label2,
        min_current_label2_image2,
        max_label2_image2,
        min_label2_image1,
        max_current_label2_image1,
    )

    # 重複を削除
    new_label1 = list(set(new_label1))
    new_label2 = list(set(new_label2))

    return new_label1, new_label2


def cur_label1_vs_img1(label_number_1, current_label1):
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
    return min_current_label1_image1


def all_label1_vs_img1(label_number_1, current_label1, label1_image1_probs):
    label_candidates = [
        label for label in label1_image1_probs if label not in current_label1
    ]
    similarities = [label1_image1_probs[label] for label in label_candidates]
    probabilities = np.exp(similarities) / np.sum(
        np.exp(similarities)
    )  # softmaxを使用して確率分布を作成
    max_label1_image1 = np.random.choice(label_candidates, p=probabilities)
    return max_label1_image1


def cur_label1_vs_img2(
    current_label1, label1_image1_probs, label1_image2_probs, min_current_label1_image1
):
    current_label1_image2_probs = {
        label: label1_image2_probs[label]
        for label in current_label1
        if label in label1_image2_probs and label != min_current_label1_image1
    }
    current_label1_image1_probs = {
        label: label1_image1_probs[label]
        for label in current_label1
        if label in label1_image1_probs and label != min_current_label1_image1
    }
    # all_label1とimage1との類似度からall_label1とimage2を引いたものを計算
    differences_label1 = [
        current_label1_image1_probs[label] - current_label1_image2_probs[label]
        for label in current_label1
        if label != min_current_label1_image1
    ]
    # 差の逆数を取る
    inverse_differences = [1 / d for d in differences_label1 if d != 0]
    # 逆数を確率分布に変換
    probabilities = np.exp(inverse_differences)
    probabilities /= probabilities.sum()
    # 確率分布に基づいてラベルを選択
    max_current_label1_image2 = np.random.choice([label for label in current_label1 if label != min_current_label1_image1], p=probabilities)
    return max_current_label1_image2


def all_label1_vs_img2(
    current_label1, all_label1_list, label1_image1_probs, label1_image2_probs
):
    label1_candidates = [
        label for label in all_label1_list if label not in current_label1
    ]
    # current_label1に含まれるラベルの類似度を抽出
    current_label1_image2_probs = {
        label: label1_image2_probs[label]
        for label in all_label1_list
        if label in label1_candidates
    }
    current_label1_image1_probs = {
        label: label1_image1_probs[label]
        for label in all_label1_list
        if label in label1_candidates
    }
    # all_label1とimage1との類似度からall_label1とimage2を引いたものを計算
    differences_label1 = [
        current_label1_image1_probs[label] - current_label1_image2_probs[label]
        for label in label1_candidates
    ]
    # ソフトマックス関数を適用
    probabilities = np.exp(differences_label1)
    probabilities /= probabilities.sum()
    # 確率分布に基づいてラベルを選択
    min_label1_image2 = np.random.choice(label1_candidates, p=probabilities)
    return min_label1_image2


def enhance_label1(
    current_label1,
    min_current_label1_image1,
    max_label1_image1,
    min_label1_image2,
    max_current_label1_image2,
):
    new_label1 = current_label1.copy()
    new_label1.remove(min_current_label1_image1)
    new_label1.append(max_label1_image1)
    new_label1.append(min_label1_image2)
    new_label1.remove(max_current_label1_image2)
    return new_label1


# label2での処理
def cur_label2_vs_img2(label_number_2, current_label2):
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
    return min_current_label2_image2


def all_label2_vs_img2(label_number_2, current_label2, label2_image2_probs):
    label_candidates = [
        label for label in label2_image2_probs if label not in current_label2
    ]
    similarities = [label2_image2_probs[label] for label in label_candidates]
    probabilities = np.exp(similarities) / np.sum(
        np.exp(similarities)
    )  # softmaxを使用して確率分布を作成
    max_label2_image2 = np.random.choice(label_candidates, p=probabilities)
    return max_label2_image2


def all_label2_vs_img1(
    current_label2, all_label2_list, label2_image2_probs, label2_image1_probs
):
    label2_candidates = [
        label for label in all_label2_list if label not in current_label2
    ]
    # current_label2に含まれるラベルの類似度を抽出
    current_label2_image2_probs = {
        label: label2_image2_probs[label]
        for label in all_label2_list
        if label in label2_candidates
    }
    current_label2_image1_probs = {
        label: label2_image1_probs[label]
        for label in all_label2_list
        if label in label2_candidates
    }
    # all_label2とimage2との類似度からall_label2とimage1を引いたものを計算
    differences_label2 = [
        current_label2_image2_probs[label] - current_label2_image1_probs[label]
        for label in label2_candidates
    ]
    # ソフトマックス関数を適用
    probabilities = np.exp(differences_label2)
    probabilities /= probabilities.sum()
    # 確率分布に基づいてラベルを選択
    min_label2_image1 = np.random.choice(label2_candidates, p=probabilities)
    return min_label2_image1


def cur_label2_vs_img1(
    current_label2, label2_image2_probs, label2_image1_probs, min_current_label2_image2
):
    current_label2_image2_probs = {
        label: label2_image2_probs[label]
        for label in current_label2
        if label in label2_image2_probs and label != min_current_label2_image2
    }
    current_label2_image1_probs = {
        label: label2_image1_probs[label]
        for label in current_label2
        if label in label2_image1_probs and label != min_current_label2_image2
    }
    # all_label2とimage2との類似度からall_label2とimage1を引いたものを計算
    differences_label2 = [
        current_label2_image2_probs[label] - current_label2_image1_probs[label]
        for label in current_label2
        if label != min_current_label2_image2
    ]
    # 差の逆数を取る
    inverse_differences = [1 / d for d in differences_label2 if d != 0]
    # 逆数を確率分布に変換
    probabilities = np.exp(inverse_differences)
    probabilities /= probabilities.sum()
    # 確率分布に基づいてラベルを選択
    max_current_label2_image1 = np.random.choice(
        [label for label in current_label2 if label != min_current_label2_image2],
        p=probabilities,
    )
    return max_current_label2_image1


def enhance_label2(
    current_label2,
    min_current_label2_image2,
    max_label2_image2,
    min_label2_image1,
    max_current_label2_image1,
):
    new_label2 = current_label2.copy()
    new_label2.remove(min_current_label2_image2)
    new_label2.append(max_label2_image2)
    new_label2.append(min_label2_image1)
    new_label2.remove(max_current_label2_image1)
    return new_label2
