from zero_shot_classification import zero_shot_classification

# from show import show
from datasets.datasets import image_urls, labels
import random
from filter_labels import filter_labels
from evaluate import evaluate


def main():
    # 単語数の宣言
    word_count = 9
    # 初回のラベル選択
    random_labels = [
        [word.strip() for word in random.sample(label.split(","), word_count)]
        if len(label.split(",")) >= word_count
        else [word.strip() for word in label.split(",")]
        for label in labels
    ]

    for _ in range(10):
        print("途中経過のラベル群: ")
        print(random_labels)
        result_data = zero_shot_classification(image_urls, random_labels)
        # evaluate関数に結果を渡し、f値と改善すべきラベルを取得
        dangerous_label_index1, dangerous_label_index2 = evaluate(result_data)
        print("改善したいラベル番号は")
        print(dangerous_label_index1, dangerous_label_index2)

        # filter_labels関数を使用してラベルを改善
        # TODO インデックスの扱いわかりにくい、統一しろ
        result1, result2 = filter_labels(
            dangerous_label_index1,
            random_labels[dangerous_label_index1 - 1],
            dangerous_label_index2,
            random_labels[dangerous_label_index2 - 1],
        )

        # リストを文字列に変換してrandom_labelsの特定のインデックスに代入
        random_labels[dangerous_label_index1 - 1] = result1
        random_labels[dangerous_label_index2 - 1] = result2
    print("最終的なラベル群: ")
    print(random_labels)


if __name__ == "__main__":
    main()
