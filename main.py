from zero_shot_classification import zero_shot_classification
from datasets.datasets import image_urls, labels
import random
from enhance_label_discrimination import enhance_label_discrimination
from evaluate import calculate_f1_scores, find_low_performance_labels
from logger import setup_logger
from datetime import datetime


logger = setup_logger("main")


def main():
    # 特徴量数の宣言
    word_count = 3
    avg_f1_scores_history = []
    # 改善したラベルの番号を保存するリストを初期化
    improved_labels_history = []
    # 初回のラベル選択
    current_labels = [
        [word.strip() for word in random.sample(label.split(","), word_count)]
        if len(label.split(",")) >= word_count
        else [word.strip() for word in label.split(",")]
        for label in labels
    ]
    counter = 0
    # 現在の日時を取得
    now = datetime.now()
    while counter < 100:
        logger.info(f"{counter}周目経過時のラベル群:{current_labels}")
        result_data = zero_shot_classification(image_urls, current_labels)
        # evaluate関数に結果を渡し、f値と改善すべきラベルを取得
        f1_scores = calculate_f1_scores(result_data)
        # F1スコアの算術平均を計算
        avg_f1_score = sum(f1_scores) / len(f1_scores)
        # 平均F1スコアをリストに追加
        avg_f1_scores_history.append(avg_f1_score)
        logger.warning("平均F1スコア: %s", avg_f1_score)

        # 平均F1スコアが基準を超えたらループを抜ける
        if avg_f1_score > 0.7:
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
        # 改善したラベルの番号をリストに追加
        improved_labels_history.append(
            (low_performance_label_number_1, low_performance_label_number_2)
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

        # 最新の4つのスコアが交互になっている場合、その直前に改善したラベルのペアを初期化
        if (
            len(avg_f1_scores_history) >= 4
            and len(set(avg_f1_scores_history[-4::2])) == 1
            and len(set(avg_f1_scores_history[-3::2])) == 1
        ):
            # 指定されたラベルだけを初期化
            current_labels[low_performance_label_number_1 - 1] = (
                [
                    word.strip()
                    for word in random.sample(
                        labels[low_performance_label_number_1 - 1].split(","),
                        word_count,
                    )
                ]
                if len(labels[low_performance_label_number_1 - 1].split(","))
                >= word_count
                else [
                    word.strip()
                    for word in labels[low_performance_label_number_1 - 1].split(",")
                ]
            )
            current_labels[low_performance_label_number_2 - 1] = (
                [
                    word.strip()
                    for word in random.sample(
                        labels[low_performance_label_number_2 - 1].split(","),
                        word_count,
                    )
                ]
                if len(labels[low_performance_label_number_2 - 1].split(","))
                >= word_count
                else [
                    word.strip()
                    for word in labels[low_performance_label_number_2 - 1].split(",")
                ]
            )
            logger.error(
                f"初期化し直したラベル番号:{current_labels[low_performance_label_number_1 - 1]}と{current_labels[low_performance_label_number_2 - 1]}"
            )
            # 初期化したペアの履歴とF1スコアの履歴をクリア
            improved_labels_history = []
            avg_f1_scores_history = []

        # 日時を文字列に変換
        timestamp_str = now.strftime("%Y%m%d_%H%M%S")

        # ファイル名にタイムスタンプを追加
        f1_scores_file = f"result_data/f1_scores_history/{timestamp_str}.txt"
        avg_f1_scores_file = f"result_data/avg_f1_scores_history/{timestamp_str}.txt"
        improved_labels_file = (
            f"result_data/improved_labels_history/{timestamp_str}.txt"
        )

        # F1スコアの推移を保存
        with open(f1_scores_file, "a") as f:
            f.write("%s\n" % f1_scores)
        # 平均F1スコアの推移を保存
        with open(avg_f1_scores_file, "a") as f:
            f.write("%s\n" % avg_f1_score)
        # 改善したラベルの番号の推移を保存
        with open(improved_labels_file, "a") as f:
            f.write(
                "%s\n"
                % str((low_performance_label_number_1, low_performance_label_number_2))
            )
        counter += 1
    logger.info(f"最終的なラベル群:{current_labels}")


if __name__ == "__main__":
    main()
