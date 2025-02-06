import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file into a DataFrame
df = pd.read_csv('csv_data.csv')

# List of places
places = ["Edward Boyle Library", "Hyde Park", "A58 (Road)", "The Edge gym", "Leeds Train Station"]

# Extract the relevant columns for eco2, temperature, and humidity
eco2_values = df['eCO2Value']
temperature_values = df['Temperature']
humidity_values = df['Humidity']

# The number of places
n_places = len(places)

# Bar width
width = 0.2

# Create the x positions for the bars
x = range(n_places)  # Using range instead of places directly

# Create the bar chart
fig, ax = plt.subplots(figsize=(10, 6))

# Create bars for eco2, temperature, and humidity
bars1 = ax.bar([i - width for i in x], eco2_values, width, label='eco2', color='red')
bars2 = ax.bar(x, humidity_values, width, label='Humidity', color='blue')
bars3 = ax.bar([i + width for i in x], temperature_values, width, label='Temperature', color='green')

# Add labels, title, and legend
ax.set_xlabel('Places')
ax.set_ylabel('Values')
ax.set_title('Eco2, Temperature, and Humidity On/Off Campus')

# Set x-ticks to the position of places and label them
ax.set_xticks(x)
ax.set_xticklabels(places)

ax.set_yscale('log')

ax.legend()

# Display the plot
plt.tight_layout()
plt.show()
input("...")