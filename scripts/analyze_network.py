import pandas as pd
import matplotlib.pyplot as plt

# Read network results
df = pd.read_csv("results/processed/network_results.csv")

print("Network Results:")
print(df)

# Create graph
x = range(len(df))

plt.figure(figsize=(8, 5))

plt.bar(
    [i - 0.2 for i in x],
    df["sender_gbits"],
    width=0.4,
    label="Sender"
)

plt.bar(
    [i + 0.2 for i in x],
    df["receiver_gbits"],
    width=0.4,
    label="Receiver"
)

plt.xticks(list(x), df["environment"])
plt.xlabel("Environment")
plt.ylabel("Bandwidth (Gbits/sec)")
plt.title("Network Performance: VM vs Container")
plt.legend()
plt.tight_layout()

plt.savefig(
    "results/figures/network_performance.png",
    dpi=300
)

print("\nGraph saved to results/figures/network_performance.png")
