import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from data_loader import load_data
import seaborn as sns

file_path = ('/Users/isiomailoh/Desktop/datasets/shopping_trends_project/data/shopping_trends_dataset.csv')
df = load_data(file_path)

colors = ["#89CFF0", "#FF69B4", "#FFD700", "#7B68EE", "#FF4500",
          "#9370DB", "#32CD32", "#8A2BE2", "#FF6347", "#20B2AA",
          "#FF69B4", "#00CED1", "#FF7F50", "#7FFF00", "#DA70D6"]
plt.figure(figsize=(20, 6))

counts = df["Gender"].value_counts()
explode = (0, 0.1)

counts.plot(kind='pie', fontsize=12, colors=colors, explode=explode, autopct='%1.1f%%')
plt.xlabel('Gender', weight="bold", color="#2F0F5D", fontsize=14, labelpad=20)
plt.axis('equal')
plt.legend(labels=counts.index, loc="best")
plt.show()
