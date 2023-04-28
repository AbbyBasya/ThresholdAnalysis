import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv ('/Users/murthylabmac/Downloads/behavioral_data/behavioral_data.csv')

stim = np.array(df['stimulus_evidence'])
response = np.array(df['response'])

x = np.unique(df['stimulus_evidence'])

proportion = []
for unique in x:
    indices = np.where(stim == unique)
    proportion.append(sum(response[indices])/np.shape(indices)[1])

plt.plot(x, proportion)
plt.xlabel("stimulus_evidence")
plt.ylabel("proportion_rightward")
plt.show()
