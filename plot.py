import pandas as pd
import matplotlib.pyplot as plt
import os

filenames = ['0.5M_T1.csv', '0.5M_T2.csv', '0.5M_T3.csv', '1.0M_T1.csv', '1.0M_T2.csv', '1.0M_T3.csv', '2.0M_T1.csv', '2.0M_T2.csv', '2.0M_T3.csv']
g = 9.81  # m/s^2

results = []

for filename in filenames:
    df = pd.read_csv(filename)

    # --- Plot 1: total acceleration vs time ---
    plt.figure(figsize=(10, 5))
    plt.plot(df["time"], df["atotal"])
    plt.xlabel("Time (s)")
    plt.ylabel("Total Acceleration (m/s^2)")
    plt.title(f"Total Acceleration vs Time\n{os.path.basename(filename)}")
    plt.grid(True)

    print(f"\nSelect TWO points on the total acceleration plot for {filename}:")
    print("1. Release time")
    print("2. Impact time")
    points = plt.ginput(2, timeout=-1)  # click two points on the graph
    plt.show()

    release_time = points[0][0]
    impact_time = points[1][0]
    delta_t = impact_time - release_time
    impact_velocity = g * delta_t

    results.append({
        "height/trial": os.path.basename(filename),
        "release_time (s)": release_time,
        "impact_time (s)": impact_time,
        "free_fall_duration (s)": delta_t,
        "impact_velocity (m/s)": impact_velocity
    })

    # --- Plot 2: acceleration vs time for each axis ---
    plt.figure(figsize=(10, 6))
    plt.plot(df["time"], df["ax"], label="ax")
    plt.plot(df["time"], df["ay"], label="ay")
    plt.plot(df["time"], df["az"], label="az")
    plt.xlabel("Time (s)")
    plt.ylabel("Acceleration (m/s^2)")
    plt.title(f"Acceleration vs Time (x, y, z)\n{os.path.basename(filename)}")
    plt.legend()
    plt.grid(True)
    plt.show()

# --- Create results table ---
results_df = pd.DataFrame(results)

print("\nDrop Analysis Table:")
print(results_df)

# Optional: save table to CSV
results_df.to_csv("drop_analysis_results.csv", index=False)