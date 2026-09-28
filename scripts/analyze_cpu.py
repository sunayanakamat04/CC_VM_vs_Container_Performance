import pandas as pd
import matplotlib.pyplot as plt

# Read processed CPU results
df = pd.read_csv("results/processed/cpu_results.csv")

print("CPU Results:")
print(df)

# Calculate average performance for each environment and thread count
summary = (
    df.groupby(["environment", "threads"])["events_per_second"]
    .mean()
    .reset_index()
)

print("\nAverage CPU Performance:")
print(summary)

# Create graph
for environment in summary["environment"].unique():
    data = summary[summary["environment"] == environment]

    plt.plot(
        data["threads"],
        data["events_per_second"],
        marker="o",
        label=environment
    )

plt.title("CPU Performance: VM vs Container")
plt.xlabel("Number of Threads")
plt.ylabel("Events per Second")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save graph
plt.savefig(
    "results/figures/cpu_performance.png",
    dpi=300
)

print("\nGraph saved to results/figures/cpu_performance.png")
