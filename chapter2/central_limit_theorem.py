# RCDS Introduction to Statistics and random sampling
# Jesus Urtasun Elizari - Imperial College London
# Chapter 2 - The central limit theorem


# Import libraries ............................................................
import numpy as np
import matplotlib.pyplot as plt


# The central limit theorem ...................................................

# Parameters
num_experiments = 1000

# Sample Size: 1 Roll
num_rolls_per_experiment = 1
averages_1 = []

for _ in range(num_experiments):
    rolls = np.random.randint(1, 7, num_rolls_per_experiment)
    average_roll = np.mean(rolls)
    averages_1.append(average_roll)

# Sample Size: 10 Rolls
num_rolls_per_experiment = 10
averages_10 = []

for _ in range(num_experiments):
    rolls = np.random.randint(1, 7, num_rolls_per_experiment)
    average_roll = np.mean(rolls)
    averages_10.append(average_roll)

# Sample Size: 100 Rolls
num_rolls_per_experiment = 100
averages_100 = []

for _ in range(num_experiments):
    rolls = np.random.randint(1, 7, num_rolls_per_experiment)
    average_roll = np.mean(rolls)
    averages_100.append(average_roll)

# Plotting the results
plt.figure(figsize=(18, 6))

# Histogram for 1 Roll
plt.subplot(1, 3, 1)
plt.hist(averages_1, bins = 30, density = True, alpha = 0.6, color = "lightblue")
plt.title('Distribution of Averages (1 Roll per Experiment)')
plt.xlabel('Average Roll Value')
plt.ylabel('Density')
plt.axvline(3.5, color = 'red', linestyle = 'dashed', linewidth = 2, label = 'Expected Mean (3.5)')
plt.legend()
# plt.grid()

# Histogram for 10 Rolls
plt.subplot(1, 3, 2)
plt.hist(averages_10, bins = 30, density = True, alpha = 0.6, color = "lightblue")
plt.title('Distribution of Averages (10 Rolls per Experiment)')
plt.xlabel('Average Roll Value')
plt.ylabel('Density')
plt.axvline(3.5, color = 'red', linestyle = 'dashed', linewidth = 2, label = 'Expected Mean (3.5)')
plt.legend()
# plt.grid()

# Histogram for 100 Rolls
plt.subplot(1, 3, 3)
plt.hist(averages_100, bins = 30, density = True, alpha = 0.6, color = "lightblue")
plt.title('Distribution of Averages (100 Rolls per Experiment)')
plt.xlabel('Average Roll Value')
plt.ylabel('Density')
plt.axvline(3.5, color = 'red', linestyle = 'dashed', linewidth = 2, label = 'Expected Mean (3.5)')
plt.legend()
# plt.grid()

# Show the plots
plt.tight_layout()
plt.show()
