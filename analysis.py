import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("solar_data.csv")

print("Solar Energy Dataset:")
print(data)

print("\nStatistics:")
print(data.describe())

# Calculate average production
average = data["energy_production"].mean()

print("\nAverage Energy Production:", average)

# Find max production
maximum = data["energy_production"].max()

print("Maximum Production:", maximum)

# Rolling average (makes project more professional)
data["rolling_avg"] = data["energy_production"].rolling(3).mean()

# Plot graph
plt.figure(figsize=(8,5))

plt.plot(
    data["day"],
    data["energy_production"],
    marker="o",
    label="Production"
)

plt.plot(
    data["day"],
    data["rolling_avg"],
    label="3 Day Average"
)

plt.title("Solar Energy Production Analysis")

plt.xlabel("Day")

plt.ylabel("Energy Production (kWh)")

plt.legend()

plt.grid(True)

plt.show()