import matplotlib.pyplot as plt
import numpy as np

# Load data from the file
with open("result_data/avg_f1_scores_history/20240109_001800.txt", "r") as f:
    data = [float(line.strip()) for line in f]

# Plot the data
plt.plot(data)
plt.title("Progression of F1 Scores")
plt.xlabel("Epoch")
plt.ylabel("F1 Score")


# 0.1刻みで薄いグレーの線を描画
for y in np.arange(0, 1, 0.1):
    plt.axhline(y=y, color="lightgray", linestyle="-", linewidth=0.5)

plt.show()
