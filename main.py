from zero_shot_classification import zero_shot_classification
from datasets.datasets import image_urls, labels
import random
from enhance_label_discrimination import enhance_label_discrimination
from evaluate import calculate_f1_scores, find_low_performance_labels
from logger import setup_logger
from datetime import datetime


logger = setup_logger("main")


def main():
    # 単語数の宣言
    word_count = 9
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
        f1_scores_file = f"f1_scores_history_{timestamp_str}.txt"
        avg_f1_scores_file = f"avg_f1_scores_history_{timestamp_str}.txt"
        improved_labels_file = f"improved_labels_history_{timestamp_str}.txt"

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


[
    [
        "Wainscoting on lower walls",
        "Matching wood-framed pictures",
        "Patterned drapery",
        "Bathroom mirror with wood frame",
        "Wood-paneled doors",
        "Beige upholstered bench",
        "Dark wood furniture",
        "High baseboards",
        "Wood trim around windows",
    ],
    [
        "Chandelier with candle-style lights",
        "Bedside lamps with bell shades",
        "High-backed wooden chair",
        "French doors leading to balcony",
        "Wall-mounted light fixtures",
        "Arched doorways",
        "Outdoor lantern-style light fixture",
        "Exposed wooden beams",
        "Plush white carpet",
    ],
    [
        "Assorted decorative objects on dresser",
        "Ceramic canisters on counter",
        "Wood and metal staircase railing",
        "Kitchen sink with gooseneck faucet",
        "Abstract sculpture on kitchen counter",
        "White baseboards",
        "Distressed wood mirror frame",
        "Recessed lighting",
        "White trim and molding",
    ],
    [
        "Carved wood details on furniture",
        "Warm-toned wood finishes",
        "Decorative throw pillow",
        "Wrought iron bed frame",
        "Beaded table lamp",
        "White ceiling",
        "Traditional room decor",
        "Dark wood baseboards",
        "Framed floral artwork",
    ],
    [
        "Intricate carpet design",
        "Ceiling medallion",
        "Ornate picture frames",
        "Brass light switch plate",
        "Light blue tea set",
        "Antique wooden chair",
        "Decorative throw on the chair",
        "White ceiling",
        "Lace curtains",
    ],
    [
        "Striped wallpaper",
        "Minimalist decor style",
        "Neatly arranged bed",
        "Dark metal bed frame",
        "Paneled walls",
        "Beige wall paint above paneling",
        "Gray upholstered bed frame",
        "Decorative ceiling medallion",
        "Beige carpet in other room",
    ],
    [
        "Sheer window shades",
        "Purple bedspread",
        "Downlights in kitchen area",
        "Open shelving in the kitchen",
        "Stacked books on the kitchen counter",
        "Black ceiling fan",
        "Large window panes",
        "Multi-level living spaces",
        "Lush greenery outside the window",
    ],
    [
        "White radiator heater",
        "Flush mounted ceiling lights",
        "Natural light from window",
        "Neutral-toned bedding",
        "Minimalistic design",
        "White walls",
        "White ceiling",
        "Abstract graffiti wall art",
        "Recessed wall nooks",
    ],
    [
        "Patterned wallpaper accent wall",
        "Blended interior decor",
        "Black venetian blinds",
        "Minimalistic furniture design",
        "Architectural room features",
        "Sleek wardrobe handles",
        "Beige throw pillow",
        "Neutral room tones",
        "Natural light from window",
    ],
    [
        "Shadow play on walls",
        "Dark wood door",
        "Step leading down to bed area",
        "Neutral color palette",
        "Contemporary art",
        "Open space concept",
        "Discreet wall outlets",
        "White bedding",
        "elegant furniture style",
    ],
]
