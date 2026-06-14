import json
import pandas as pd
import matplotlib.pyplot as plt

with open("results/crypto_benchmark_mongo.json") as f:
    mongo = json.load(f)

dados = []

for tamanho in mongo["results"]:
    for teste in mongo["results"][tamanho]:
        dados.append({
            "size": tamanho,
            "test": teste["test"],
            "ops_per_sec": teste["ops_per_sec"]
        })

df = pd.DataFrame(dados)

for teste in df["test"].unique():
    subset = df[df["test"] == teste]

    plt.figure(figsize=(8,5))
    plt.plot(subset["size"], subset["ops_per_sec"], marker="o")
    plt.title(teste)
    plt.ylabel("Ops/sec")
    plt.xlabel("Payload")
    plt.grid()

    plt.savefig(f"results/{teste}.png")
    plt.close()