import pandas as pd
import matplotlib.pyplot as plt

# Read memory results
df = pd.read_csv("results/processed/memory_results.csv")

print("Memory Results:")
print(df)

# Create graph
plt.bar(
    df["environment"],
    df["memory_speed_mib_per_sec"]
)

plt.title("Memory Performance: VM vs Container")
plt.xlabel("Environment")
plt.ylabel("Memory Speed (MiB/sec)")
plt.tight_layout()

# Save graph
plt.savefig(
    "results/figures/memory_performance.png",
    dpi=300
)

print("\nGraph saved to results/figures/memory_performance.png")
