from zero_shot_classification import zero_shot_classification

# from show import show
from datasets.datasets import image_urls, labels
import random
from enhance_label_discrimination import enhance_label_discrimination
from evaluate import calculate_f1_scores, find_low_performance_labels
from logger import setup_logger

logger = setup_logger("main")


def main():
    # 単語数の宣言
    word_count = 9
    # 初回のラベル選択
    current_labels = [
        [word.strip() for word in random.sample(label.split(","), word_count)]
        if len(label.split(",")) >= word_count
        else [word.strip() for word in label.split(",")]
        for label in labels
    ]
    counter = 0
    while counter < 60:
        logger.info(f"{counter}周目経過時のラベル群:{current_labels}")
        result_data = zero_shot_classification(image_urls, current_labels)
        # evaluate関数に結果を渡し、f値と改善すべきラベルを取得
        f1_scores = calculate_f1_scores(result_data)
        # F1スコアの算術平均を計算
        avg_f1_score = sum(f1_scores) / len(f1_scores)
        logger.warning("平均F1スコア: %s", avg_f1_score)

        # 平均F1スコアが基準を超えたらループを抜ける
        if avg_f1_score > 0.8:
            break

        (
            low_performance_label_1,
            low_performance_label_2,
        ) = find_low_performance_labels(result_data)

        low_performance_label_number_1 = (
            current_labels.index(low_performance_label_1) + 1
        )
        low_performance_label_number_2 = (
            current_labels.index(low_performance_label_2) + 1
        )
        logger.info(
            f"改善したいラベル番号:{low_performance_label_number_1}と{low_performance_label_number_2}"
        )

        # enhance_label_discrimination関数を使用してラベルを改善
        result1, result2 = enhance_label_discrimination(
            low_performance_label_number_1,
            current_labels[low_performance_label_number_1 - 1],
            low_performance_label_number_2,
            current_labels[low_performance_label_number_2 - 1],
        )

        # リストを文字列に変換してrandom_labelsの特定のインデックスに代入
        current_labels[low_performance_label_number_1 - 1] = result1
        current_labels[low_performance_label_number_2 - 1] = result2
        counter += 1
    logger.info(f"最終的なラベル群:{current_labels}")


if __name__ == "__main__":
    main()
