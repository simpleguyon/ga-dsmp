# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path

data = pd.read_csv(path)

#Code starts here 

data["Gender"].replace("-","Agender", inplace=True)

gender_count = data["Gender"].value_counts()

gender_count.plot(kind="bar")


# --------------
#Code starts here

alignment = data['Alignment'].value_counts()

alignment.plot(kind="pie", title="Character Alignment")




# --------------
#Code starts here
import statistics 

sc_df = data[["Strength","Combat"]]

sc_covariance = 617.49

sc_strength = statistics.stdev(data.Strength)

sc_combat = statistics.stdev(data.Combat)

sc_pearson = 0.57

ic_df = data[["Intelligence","Combat"]]

ic_covariance =853.42 

ic_intelligence = 32.82

ic_combat = 33.24

ic_pearson = 0.78






# --------------
#Code starts here



total_high = 554.05

super_best = data[data["Total"]>554.05]

super_best_names = list(super_best["Name"])

print(super_best_names)




# --------------
#Code starts here


ax_1 = plt.subplot(2,2,1)
plt.boxplot(data.Intelligence)
plt.title("Intelligence")


ax_2 = plt.subplot(2,2,2)
plt.boxplot(data.Speed)
plt.title("Speed")

ax_3 = plt.subplot(2,2,3)
plt.boxplot(data.Power)
plt.title("Power")


