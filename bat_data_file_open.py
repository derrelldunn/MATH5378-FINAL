import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('bat_data.csv')
print(data.head(5))
print(data.describe())
trap_names = data["Trap"]
print(trap_names)
time_species = data[["Time", "Species"]]
species_time = data[[ "Species", "Time"]]
print(time_species)
print(trap_names.describe())
print(time_species.describe())
bat_weight=data[["Species", "Wt(g)"]]
print(bat_weight)
print(bat_weight.describe())
bat_weight.boxplot()
bat_weight.hist()
#species_time.hist()
plt.show()
#add new code here


