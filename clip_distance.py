import torch
import clip
from PIL import Image
import requests
from io import BytesIO
from torchvision.transforms import Compose, Resize, CenterCrop, ToTensor, Normalize
from datasets.datasets import image_urls, labels


def calculate_similarity(labels: list, image_url: str):
    # 画像のダウンロード
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))

    # モデルのロード
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, preprocess = clip.load("ViT-B/32", device=device)

    # 画像の前処理
    preprocess = Compose(
        [
            Resize([224, 224]),
            CenterCrop(224),
            ToTensor(),
            Normalize(
                (0.48145466, 0.4578275, 0.40821073),
                (0.26862954, 0.26130258, 0.27577711),
            ),
        ]
    )
    image = preprocess(img).unsqueeze(0).to(device)

    # テキストの前処理
    texts = clip.tokenize(labels).to(device)

    # モデルを通じて特徴ベクトルを取得
    with torch.no_grad():
        logits_per_image, _ = model(image, texts)
        scores = logits_per_image.cpu().numpy()
    # ラベルとそのスコアを辞書に格納
    label_scores = {label: score for label, score in zip(labels, scores[0])}

    return label_scores
