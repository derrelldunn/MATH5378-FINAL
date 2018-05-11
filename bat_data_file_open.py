import matplotlib.pyplot as plt
import pandas as pd
import scipy

import scikits.bootstrap as bootstrap

data = pd.read_csv('bat_data.csv')
data_input = pd.read_csv('bat_data.csv')
print('All Bats Species Statistical Summary')
print(data.describe())

print('All Bat Species correlation coefficient between FA(mm) and Wt(g)')
print(data['FA(mm)'].corr(data['Wt(g)']))
print('\n-------------------------------------')

species_length = data[["Species", "FA(mm)"]]
species_len = data["FA(mm)"]

species_length.hist()
species_length.boxplot()
plt.title("All Bat Species Bat Length N = 267")
plt.show()
species_length.hist()
plt.title("All Bat Species  Length-FA(mm) N = 267")
plt.show()

CIs = bootstrap.ci(data=species_len, statfunction=scipy.mean)
print('Confidence Interval FA(mm) All Species Bats Low {} High {}'.format(CIs[0], CIs[1]))
print('\n-------------------------------------')

bat_weight = data[["Species", "Wt(g)"]]
species_wt = data['Wt(g)']

CIwt = bootstrap.ci(data=species_wt, statfunction=scipy.mean)
print('Confidence Interval Wt(g) All Species Bats Low {} High {}'.format(CIwt[0], CIwt[1]))
print('\n-------------------------------------')

bat_weight.boxplot()
plt.title('All Bat Species Weight - Wt(g) N= 267')
plt.show()
bat_weight.hist()
plt.title('All Bat Species Histogram (Bat Weight in grams) N = 267')
plt.show()

subgrp_Mcriteria = data['Sex'] == 'M'
subgrp_Fcriteria = data['Sex'] == 'F'

overall_female = data[subgrp_Fcriteria]
overall_male = data[subgrp_Mcriteria]

print('All Species Female only correlation coefficient between FA(mm) and Wt(g)')
print(overall_female['FA(mm)'].corr(overall_female['Wt(g)']))
print('\n')
print('All Species Male only correlation coefficient between FA(mm) and Wt(g)')
print(overall_male['FA(mm)'].corr(overall_male['Wt(g)']))

print('\nAll Species Female Bat Summary Statistics')
print(overall_female.describe())
print('\nAll Species Male Bat Summary Statistics')
print(overall_male.describe())

CIwt = bootstrap.ci(data=overall_male['Wt(g)'], statfunction=scipy.mean)
print('Confidence Interval Male Wt(g) All Species Bats Low {} High {}'.format(CIwt[0], CIwt[1]))
print('\n-------------------------------------')

CIwt = bootstrap.ci(data=overall_female['Wt(g)'], statfunction=scipy.mean)
print('Confidence Interval Female Wt(g) All Bats Low {} High {}'.format(CIwt[0], CIwt[1]))
print('\n-------------------------------------')

CIwt = bootstrap.ci(data=overall_male['FA(mm)'], statfunction=scipy.mean)
print('Confidence Interval Male FA(mm) All Bats Low {} High {}'.format(CIwt[0], CIwt[1]))
print('\n-------------------------------------')

CIwt = bootstrap.ci(data=overall_female['FA(mm)'], statfunction=scipy.mean)
print('Confidence Interval Female FA(mm) All Bats Low {} High {}'.format(CIwt[0], CIwt[1]))
print('\n-------------------------------------')

overall_female.boxplot()
plt.title('Female only - All Species')
plt.show()
overall_male.boxplot()
plt.title('Male only - All Species')
plt.show()

subgrp_late_capture_time = data['Time'] == '21:00'
subgrp_early_capture_time = data['Time'] == '7:00'

subgrp_early_capture_time.boxplot()
plt.title('Early Capture - All Species')
plt.show()
subgrp_late_capture_time.boxplot()
plt.title('Late capture - All Species')
plt.show()

print('All Species Late Capture Time')
print(subgrp_late_capture_time.describe())

print('All Species Early Capture Time')
print(subgrp_early_capture_time.describe())

overall_male_early = data[subgrp_Mcriteria & subgrp_early_capture_time]
overall_male_late = data[subgrp_Mcriteria & subgrp_late_capture_time]

overall_male_early.boxplot()
plt.title('Male only Early - All Species')
plt.show()
overall_male_late.boxplot()
plt.title('Male only Late - All Species')
plt.show()

overall_female_early = data[subgrp_Fcriteria & subgrp_early_capture_time]
overall_female_late = data[subgrp_Fcriteria & subgrp_late_capture_time]

overall_female_early.boxplot()
plt.title('Female only Early - All Species')
plt.show()
overall_female_late.boxplot()
plt.title('Female only Late - All Species')
plt.show()

print('All Species Female Early Statistical Summary')
print(overall_female_early.describe())
print('All Species Female Late Statistical Summary')
print(overall_female_late.describe())

print('All Species Male Early Statistical Summary')
print(overall_male_early.describe())
print('All Species Male Late Statistical Summary')
print(overall_male_late.describe())

print('Male only Early Correlation Coefficient')
print(overall_male_early['FA(mm)'].corr(overall_male_early['Wt(g)']))

CIwt = bootstrap.ci(data=overall_male_early['FA(mm)'], statfunction=scipy.mean)
print('Confidence Interval Early Male FA(mm) All Species Bats Low {} High {}'.format(CIwt[0], CIwt[1]))
print('\n-------------------------------------')

print('Male Only Late All Species correlation coefficient')
print(overall_male_late['FA(mm)'].corr(overall_male_late['Wt(g)']))

CIwt = bootstrap.ci(data=overall_male_late['FA(mm)'], statfunction=scipy.mean)
print('Confidence Interval Late Male FA(mm) All Species Low {} High {}'.format(CIwt[0], CIwt[1]))
print('\n-------------------------------------')

print('All Species female Early correlation coefficient')
print(overall_female_early['FA(mm)'].corr(overall_female_early['Wt(g)']))

CIwt = bootstrap.ci(data=overall_female_early['FA(mm)'], statfunction=scipy.mean)
print('Confidence Interval All Species Early Female FA(mm) All Bats Low {} High {}'.format(CIwt[0], CIwt[1]))
print('\n-------------------------------------')

print('All Species female Late correlation coefficient')
print(overall_female_late['FA(mm)'].corr(overall_female_late['Wt(g)']))
print('\n-------------------------------------')

CIwt = bootstrap.ci(data=overall_female_late['FA(mm)'], statfunction=scipy.mean)
print('Confidence Interval All Species Late Female FA(mm) All Bats Low {} High {}'.format(CIwt[0], CIwt[1]))
print('\nEnd of All Species Analysis')

subgrp_trap_location = data['Trap']

# plt.scatter(data['Band'], data['Wt(g)'], c=data['Sex'] == 'F')
# plt.title('All Species Scatterplot N = 267, female in yellow')
# plt.show()

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


intermedia_female_stats = data[fm_combine_grp]
intermedia_female_late_stats_time = data[fm_combine_grp_time]
intermedia_female_early_stats_time = data[fm_combine_grp_time_early]

intermedia_female_late_stats_time_weight = intermedia_female_late_stats_time['Wt(g)']
intermedia_female_early_stats_time_weight = intermedia_female_early_stats_time['Wt(g)']
intermedia_female_stats_time_weight = intermedia_female_stats['Wt(g)']

intermedia_female_late_stats_time_size = intermedia_female_late_stats_time['FA(mm)']
intermedia_female_early_stats_time_size = intermedia_female_early_stats_time['FA(mm)']
intermedia_female_stats_time_size = intermedia_female_stats['FA(mm)']

print('Kerivoula intermedia Species Female Only Statistics')
print(intermedia_female_stats.describe())
print('Kerivoula intermedia Species Late Female Only Statistics')
print(intermedia_female_late_stats_time.describe())
print('Kerivoula intermedia Species Early Female Only Statistics')
print(intermedia_female_early_stats_time.describe())
print('\n')

CIs = bootstrap.ci(data=intermedia_female_stats_time_weight, statfunction=scipy.mean)
print ('Kerivoula intermedia Female Weight confidence intervals Low:{} High{}'.format(CIs[0], CIs[1]))
CIs = bootstrap.ci(data=intermedia_female_late_stats_time_weight, statfunction=scipy.mean)
print ('Kerivoula intermedia Late Weight Female confidence interval Low:{} High{}'.format(CIs[0], CIs[1]))
# CIs = bootstrap.ci(data =intermedia_female_early_stats_time_weight, statfunction=scipy.mean)
# print ('Kerivoula intermedia Early Weight Female confidence intervals Low:{} High{}'.format(CIs[0], CIs[1]))
CIs = bootstrap.ci(data=intermedia_female_stats_time_size, statfunction=scipy.mean)
print ('Kerivoula intermedia Female FA(mm) confidence interval Low:{} High{}'.format(CIs[0], CIs[1]))
CIs = bootstrap.ci(data=intermedia_female_late_stats_time_size, statfunction=scipy.mean)
print ('Kerivoula intermedia Late Female FA(mm) confidence interval Low:{} High{}'.format(CIs[0], CIs[1]))
CIs = bootstrap.ci(data=intermedia_female_early_stats_time_size, statfunction=scipy.mean)
print ('Kerivoula intermedia Early Female FA(mm) confidence interval Low:{} High{}'.format(CIs[0], CIs[1]))

intermedia_female_stats.boxplot()
plt.title('Kerivoula Female intermedia N = 11')
plt.show()
intermedia_female_late_stats_time.boxplot()
plt.title('Kerivoula intermedia Female Late Capture Time N = 6')
plt.show()
intermedia_female_early_stats_time.boxplot()
plt.title('Kerivoula intermedia Female Early Capture Time N = 5')
plt.show()

intermedia_male_stats = data[m_combine_grp]
intermedia_male_late_stats_time = data[m_combine_grp_time]
intermedia_male_early_stats_time = data[m_combine_grp_time_early]

intermedia_male_late_stats_time_weight = intermedia_male_late_stats_time['Wt(g)']
intermedia_male_early_stats_time_weight = intermedia_male_early_stats_time['Wt(g)']
intermedia_male_stats_time_weight = intermedia_male_stats['Wt(g)']

intermedia_male_late_stats_time_size = intermedia_male_late_stats_time['FA(mm)']
intermedia_male_early_stats_time_size = intermedia_male_early_stats_time['FA(mm)']
intermedia_male_stats_time_size = intermedia_male_stats['FA(mm)']

print('Kerivoula intermedia Male Summary Statistics')
print(intermedia_male_stats.describe())
print('Kerivoula intermedia Male Late Summary Statistics')
print(intermedia_male_late_stats_time.describe())
print('Kerivoula intermedia Male Early Summary Statistics')
print(intermedia_male_early_stats_time.describe())

CIs = bootstrap.ci(data=intermedia_male_stats_time_weight, statfunction=scipy.mean)
print ('Kerivoula intermedia Male Weight confidence interval Low:{} High{}'.format(CIs[0], CIs[1]))

CIs = bootstrap.ci(data=intermedia_male_late_stats_time_weight, statfunction=scipy.mean)
print ('Kerivoula intermedia Male Late Weight confidence interval Low:{} High{}'.format(CIs[0], CIs[1]))

CIs = bootstrap.ci(data=intermedia_male_early_stats_time_weight, statfunction=scipy.mean)
print ('Kerivoula intermedia Male Early Weight confidence interval Low:{} High{}'.format(CIs[0], CIs[1]))

CIs = bootstrap.ci(data=intermedia_male_stats_time_size, statfunction=scipy.mean)
print ('Kerivoula intermedia Male Size FA(mm) confidence interval Low:{} High{}'.format(CIs[0], CIs[1]))

CIs = bootstrap.ci(data=intermedia_male_late_stats_time_size, statfunction=scipy.mean)
print ('Kerivoula intermedia Male Late Size FA(mm) confidence interval Low:{} High{}'.format(CIs[0], CIs[1]))

CIs = bootstrap.ci(data=intermedia_male_early_stats_time_size, statfunction=scipy.mean)
print ('Kerivoula intermedia Male Early Size FA(mm) confidence interval Low:{} High{}'.format(CIs[0], CIs[1]))

intermedia_male_stats.boxplot()
plt.title('Kerivoula Male intermedia N = 54')
plt.show()

intermedia_male_late_stats_time.boxplot()
plt.title('Kerivoula intermedia Male Late Capture Time N = 45')
plt.show()

intermedia_male_early_stats_time.boxplot()
plt.title('Kerivoula intermedia Male Early Capture Time N = 09')
plt.show()
