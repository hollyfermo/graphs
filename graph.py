import matplotlib.pyplot as plt
import pandas as pd
plt.ion()

df = pd.read_csv("csv_data.csv")

places = ["Edward Boyle Library", "Hyde Park", "A58 (Road)", "The Edge gym", "Leeds Train Station"]

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(places, df["Temperature"], label="Temperature (Celsius)", color="red", linewidth=2)
ax1.set_ylabel("Temperature (Celsius)", color="red")
ax1.tick_params(axis="y", labelcolor="red")

ax2 = ax1.twinx()
ax2.plot(places, df["Humidity"], label="Humidity (%)", color="blue", linewidth=2)
ax2.set_ylabel("Humidity (%)", color="blue")
ax2.tick_params(axis="y", labelcolor="blue")

ax3 = ax1.twinx()
ax3.spines["right"].set_position(("outward", 60)) 
ax3.plot(places, df["eCO2Value"], label="CO2 Concentration (PPM)", color="green", linewidth=2)
ax3.set_ylabel("CO2 Concentration (PPM)", color="green")
ax3.tick_params(axis="y", labelcolor="green")

ax1.set_xlabel("Places")
plt.title("Temperature, Humidity, and CO2 Concentrations On/Off Campus")

plt.tight_layout()
plt.show()
input("Press enter to close.")