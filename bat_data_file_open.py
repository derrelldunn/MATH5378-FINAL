import matplotlib.pyplot as plt
import pandas as pd
import numpy as nd

import statsmodels.stats.api as sms
import scipy
import scikits.bootstrap as bootstrap



data = pd.read_csv('bat_data.csv')
data_input = pd.read_csv('bat_data.csv')
print(data.describe())

species_length = data[["Species", "FA(mm)"]]
species_len = data["FA(mm)"]

print(species_length.describe())
species_length.hist()
species_length.boxplot()
plt.show()
species_length.hist()
plt.show()

CIs = bootstrap.ci(data =species_len, statfunction=scipy.mean)

print ('Bootstrapped confidence intervals\nLow:', CIs[0], '\nHigh:', CIs[1])

#print('the confidence interval is:')
#print(sms.DescrStatsW(data).tconfint_mean())

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

subgrp_trap_location = data['Trap']

#plt.scatter(data['Band'], data['Wt(g)'], c=data['Sex'] == 'F')
#plt.show()

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

print(female_stats.describe())
print(female_late_stats_time.describe())
female_stats.boxplot()
plt.show()
female_late_stats_time.boxplot()
plt.show()

male_stats = data[m_combine_grp]
male_late_stats_time = data[m_combine_grp_time]

print(male_stats.describe())
print(male_late_stats_time.describe())
male_stats.boxplot()
plt.show()
male_late_stats_time.boxplot()
plt.show()



