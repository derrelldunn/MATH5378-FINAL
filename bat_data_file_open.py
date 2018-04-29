import csv
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('bat_data.csv')
print(data.head(5))
print(data.describe())
trap_names = data["Trap"]
print(trap_names)
time_species = data[["Time", "Species"]]
print(time_species)
print(trap_names.describe())
print(time_species.describe())
bat_weight=data[["Species", "Wt(g)"]]
print(bat_weight)
print(bat_weight.describe())
bat_weight.boxplot()
plt.show()


