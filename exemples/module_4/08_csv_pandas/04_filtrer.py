import pandas as pd
df = pd.read_csv("basket.csv")
subset = df[(df["position"] == "SG") & (df["ppg"].between(15, 25))]
print(subset[["Player","Team","position","ppg"]].head(5))
pays = df[df["country"].isin(["Canada","France","Serbia"])] #country match list
print(pays[["Player","country"]].head(5))
