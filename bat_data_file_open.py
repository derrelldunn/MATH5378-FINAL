import matplotlib.pyplot as plt
import pandas as pd
import numpy as nd
import scipy

import scikits.bootstrap as bootstrap

data = pd.read_csv('bat_data.csv')
data_input = pd.read_csv('bat_data.csv')
print(data.describe())
print('All correlation coeff')
print(data['FA(mm)'].corr(data['Wt(g)']))

species_length = data[["Species", "FA(mm)"]]
species_len = data["FA(mm)"]

print(species_length.describe())
species_length.hist()
species_length.boxplot()
plt.title("Full DataSet Bat Length")
plt.show()
species_length.hist()
plt.title("Full DataSet Bat Length-FA(mm)")
plt.show()

CIs = bootstrap.ci(data =species_len, statfunction=scipy.mean)
print ('Bootstrapped confidence intervals\nLow:', CIs[0], '\nHigh:', CIs[1])

bat_weight = data[["Species", "Wt(g)"]]
#print(bat_weight)
print(bat_weight.describe())
bat_weight.boxplot()
plt.show()
bat_weight.hist()
plt.show()

subgrp_Mcriteria = data['Sex'] == 'M'
subgrp_Fcriteria = data['Sex'] == 'F'

overall_female = data[subgrp_Fcriteria]
overall_male = data[subgrp_Mcriteria]

print('only female correlation coeff')
print(overall_female['FA(mm)'].corr(overall_female['Wt(g)']))

print('only male correlation coeff')
print(overall_male['FA(mm)'].corr(overall_male['Wt(g)']))

print(overall_female.describe())
print(overall_male.describe())
overall_female.boxplot()
plt.show()
overall_male.boxplot()
plt.show()

subgrp_late_capture_time = data['Time'] == '21:00'
subgrp_early_capture_time = data['Time'] == '7:00'

overall_male_early = data[(subgrp_Mcriteria) & (subgrp_early_capture_time)]
overall_male_late = data[(subgrp_Mcriteria) & (subgrp_late_capture_time)]

overall_female_early = data[(subgrp_Fcriteria) & (subgrp_early_capture_time)]
overall_female_late = data[(subgrp_Fcriteria) & (subgrp_late_capture_time)]

print('only male early correlation coeff')
print(overall_male_early['FA(mm)'].corr(overall_male_early['Wt(g)']))

print('only male late correlation coeff')
print(overall_male_late['FA(mm)'].corr(overall_male_late['Wt(g)']))

print('only female early correlation coeff')
print(overall_female_early['FA(mm)'].corr(overall_female_early['Wt(g)']))

print('only female late correlation coeff')
print(overall_female_late['FA(mm)'].corr(overall_female_late['Wt(g)']))

subgrp_trap_location = data['Trap']

plt.scatter(data['Band'], data['Wt(g)'], c=data['Sex'] == 'F')
plt.show()

subgrp_len_gt = data["FA(mm)"] > [data["FA(mm)"].mean()]

subgrp_wt_gt = data["Wt(g)"] > [data["Wt(g)"].mean()]

subgrp1_type_intermedia = data['Species'] == 'Kerivoula intermedia'
subgrp1_type_papillosa = data['Species'] == 'Kerivoula papillosa'
subgrp1_type_pellucida = data['Species'] == 'Kerivoula pellucida'
subgrp1_general_kerivoula = data['Species'] == 'Kerivoula'

subgrp2_general_hipposideros = data['Species'] == 'Hipposideros'
subgrp2_type_cervinus = data['Species'] == 'Hipposideros cervinus'

subgrp3_general_rhinolophus = data['Species'] == 'Rhinolophus'
subgrp3_type_trifoliatus = data['Species'] == 'Rhinolophus trifoliatus'

# Female late capture
fm_combine_grp_time = subgrp1_type_intermedia & subgrp_Fcriteria & subgrp_late_capture_time
# Female intermedia group
fm_combine_grp = subgrp_Fcriteria & subgrp1_type_intermedia
# Female early capture
fm_combine_grp_time_early = subgrp1_type_intermedia & subgrp_Fcriteria & subgrp_early_capture_time

# Male late capture
m_combine_grp_time = subgrp1_type_intermedia & subgrp_Mcriteria & subgrp_late_capture_time
# Male group
m_combine_grp = subgrp_Mcriteria & subgrp1_type_intermedia
# Male early capture group
m_combine_grp_time_early = subgrp1_type_intermedia & subgrp_Mcriteria & subgrp_early_capture_time

female_stats = data[fm_combine_grp]
female_late_stats_time = data[fm_combine_grp_time]
female_early_stats_time = data[fm_combine_grp_time_early]

female_late_stats_time_weight = female_late_stats_time['Wt(g)']
female_early_stats_time_weight = female_early_stats_time['Wt(g)']
female_stats_time_weight = female_stats['Wt(g)']

female_late_stats_time_size = female_late_stats_time['FA(mm)']
female_stats_time_size = female_stats['FA(mm)']

print(female_stats.describe())
print(female_late_stats_time.describe())
CIs = bootstrap.ci(data =female_late_stats_time_weight, statfunction=scipy.mean)
print ('Female late weight Bootstrapped confidence intervals\nLow:', CIs[0], '\nHigh:', CIs[1])

CIs = bootstrap.ci(data =female_stats_time_weight, statfunction=scipy.mean)
print ('Female regular Bootstrapped confidence intervals\nLow:', CIs[0], '\nHigh:', CIs[1])

CIs = bootstrap.ci(data =female_early_stats_time_weight, statfunction=scipy.mean)
print ('Female early Bootstrapped confidence intervals\nLow:', CIs[0], '\nHigh:', CIs[1])

CIs = bootstrap.ci(data =female_late_stats_time_size, statfunction=scipy.mean)
print ('Female late size Bootstrapped confidence intervals\nLow:', CIs[0], '\nHigh:', CIs[1])

CIs = bootstrap.ci(data =female_stats_time_size, statfunction=scipy.mean)
print ('Female regular size Bootstrapped confidence intervals\nLow:', CIs[0], '\nHigh:', CIs[1])

female_stats.boxplot()
plt.show()
female_late_stats_time.boxplot()
plt.show()

male_stats = data[m_combine_grp]
male_late_stats_time = data[m_combine_grp_time]
male_late_stats_time_weight = male_late_stats_time['Wt(g)']
male_stats_time_weight = male_stats['Wt(g)']
male_late_stats_time_size = male_late_stats_time['FA(mm)']
male_stats_time_size = male_stats['FA(mm)']

print(male_stats.describe())
print(male_late_stats_time.describe())
CIs = bootstrap.ci(data =male_late_stats_time_weight, statfunction=scipy.mean)
print ('male late Bootstrapped confidence intervals\nLow:', CIs[0], '\nHigh:', CIs[1])
CIs = bootstrap.ci(data =male_stats_time_weight, statfunction=scipy.mean)
print ('male Bootstrapped confidence intervals\nLow:', CIs[0], '\nHigh:', CIs[1])
CIs = bootstrap.ci(data =male_late_stats_time_size, statfunction=scipy.mean)
print ('male late size Bootstrapped confidence intervals\nLow:', CIs[0], '\nHigh:', CIs[1])
CIs = bootstrap.ci(data =male_stats_time_size, statfunction=scipy.mean)
print ('male Bootstrapped size confidence intervals\nLow:', CIs[0], '\nHigh:', CIs[1])
male_stats.boxplot()
plt.show()
male_late_stats_time.boxplot()
plt.show()


