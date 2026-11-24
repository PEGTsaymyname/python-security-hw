import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

file_path = Path("events.json")

with open(file_path, encoding="utf-8") as f:
    raw_data = json.load(f)

df = pd.DataFrame(raw_data["events"])
signature_counts = df["signature"].value_counts()
print(signature_counts)

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="signature", order=signature_counts.index)
plt.title("Распределение типов событий безопасности")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()