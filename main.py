# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np


# %%
data=pd.read_csv('data/heights.csv')
print(data.head())


# %%
# get array height by numpy
heights = np.array(data['height(cm)'])
print(heights)
print(heights.size)


# %%
print('Mean of heights= ', heights.mean())
print('Standard Deviation of height =', heights.std())
print('Minimum height =', heights.min())
print('Maximum height =', heights.max())


# %%
print("25th percentile =", np.percentile(heights, 25))
print("Median =", np.median(heights))
print("75th percentile =", np.percentile(heights, 75))


# %%
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


# %%
plt.hist(heights)
plt.title("Height Distribution of Presidents of USA")
plt.xlabel("height(cm)")
plt.ylabel("Number")
plt.show()


# %%


