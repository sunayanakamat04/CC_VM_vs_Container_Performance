import pandas as pd
import matplotlib.pyplot as plt

# Read disk results
df = pd.read_csv("results/processed/disk_results.csv")

print("Disk Results:")
print(df)

# Separate READ and WRITE results
read_data = df[df["operation"] == "READ"]
write_data = df[df["operation"] == "WRITE"]

# Create comparison graph
x = range(len(read_data))

plt.figure(figsize=(8, 5))

plt.bar(
    [i - 0.2 for i in x],
    read_data["bandwidth_kib_per_sec"],
    width=0.4,
    label="READ"
)

plt.bar(
    [i + 0.2 for i in x],
    write_data["bandwidth_kib_per_sec"],
    width=0.4,
    label="WRITE"
)

plt.xticks(list(x), read_data["environment"])
plt.xlabel("Environment")
plt.ylabel("Bandwidth (KiB/s)")
plt.title("Disk Performance: VM vs Container")
plt.legend()
plt.tight_layout()

# Save graph
plt.savefig(
    "results/figures/disk_performance.png",
    dpi=300
)

print("\nGraph saved to results/figures/disk_performance.png")
