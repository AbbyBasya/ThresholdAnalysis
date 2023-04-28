from datetime import datetime
from datetime import date
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import OrderedDict
import os
import random
import seaborn as sns
import matplotlib as mpl
import re
import csv
import pickle
import sys
#sys.path.insert(0,'D:/PhD/Behavior/Behavior_Analysis/batch_clean_selected')
from parse_data_v2_1 import Mouse_data
from parse_data_v2_1 import pickle_dict
from parse_data_v2_1 import load_pickleddata

# total = 0
# correct = 0
#
# path = '/Volumes/GoogleDrive/My Drive/behavior data/experiment_data_2022_3_cheat_go_no/parsed_dataframe_pickle'
# g= os.path.join(path,'GM2_further_stats.pickle')
# g = load_pickleddata(g)
#
# trials = g.df_trials
# iscorrect = g.df_trials_iscorrect
#
# count = 0
# for trial in trials:
#     if iscorrect:
#         total+=1
#         pcorrect=int((correct/total)*100)
#         pcorrect
#
# #plt.plot(trials, pcorrect)
# plot = sns.lineplot(data = g,x = trials,y = pcorrect)


var = pd.read_excel("/Volumes/GoogleDrive/My Drive/behavior data/figures/GM1_cumulative_15.xlsx")
print(var)

x = list(var['X values'])
iteration1 = list(var['29th'])
iteration2 = list(var['23rd'])

plot = sns.lineplot(x, iteration1, label = "29th")
sns.lineplot(x, iteration2, label = "23rd")
plot.set_ylabel("Cumulative Performance", fontsize=15)
plot.set_xlabel("Trials", fontsize=15)
#plot.xaxis.set_ticks(min(x), max(x)+1, 1.0)
#plot.xticks(np.arange(min(x), max(x)+1, 1.0))
#plot.axes.set_xticklabels(x, fontsize = 15)



plt.legend()
plt.show()








