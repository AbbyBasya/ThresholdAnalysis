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

path = 'G:/My Drive/behavior data/experiment_data_2022_3_cheat_go_no/parsed_dataframe_pickle'
filepath = os.path.join(path,'combined_all_clean_2022-08-30.pickle')
data = load_pickleddata(filepath)


data.index.duplicated()

y = 'is_Correct'
#y= 'rate_antici'
x = 'session'
#values = ['5*10^-2','5*10^-3','5*10^-4','5*10^-5']

data_deg_cond = data[(data['trialtype'].isin(['go','no_go']))]

data_deg_cond =  data_deg_cond.groupby(['mouse_name','session','phase'])[y].mean().reset_index()


#sns.lineplot(data = data_deg_cond,x = x,y = y,style = 'mouse_name')
sns.lineplot(data = data_deg_cond,x = x,y = y, marker="o",style="mouse_name")
#sns.lineplot(data = data_deg_cond,x = x,y = y, marker="o")
plt.locator_params(axis="both", integer=True, tight=True)
#plt.xticks(ticks = x ,labels = values, rotation = 'vertical')
plt.gca().invert_xaxis()

plt.show()


