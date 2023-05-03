from datetime import datetime
from datetime import date
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import OrderedDict
import os
import random
import matplotlib as mpl
import re
import csv
import pickle
import sys
#sys.path.insert(0,'D:/PhD/Behavior/Behavior_Analysis/batch_clean_selected')
from parse_data_v2_1 import Mouse_data
from parse_data_v2_1 import pickle_dict
from parse_data_v2_1 import load_pickleddata

#mouse_id = ['K3_good','K2_good','K1_good']
#mouse_id = ['K3_day1', 'K2_day1', 'K1_day1']
mouse_id = ['test']
mouse_dataframes = {}

for mouse_name in mouse_id:
    print(mouse_name)

    path = 'H:/My Drive/behavior data/valence_task_2023_odor go_no-go_no_delay/parsed_dataframe_pickle'
    filepath = os.path.join(path, '{}_stats.pickle'.format(mouse_name))
    data = load_pickleddata(filepath)
    #counter = {'MixTypes2': 0, 'MixTypes4': 1}
    counter = {'MixTypes4': 0, 'MixTypes3': 1}   #need to count days for each or switch so just day based

    training_types = data.training_type
    print(training_types)
    for index, key in enumerate(data.df_trials):

        data_trials = data.df_trials[key]
        data_trials_iscorrect = data.df_trials_iscorrect[key].drop(columns=['odormix'], axis=1)
        data_trials_lick = data.df_trials_lick[key].drop(columns=['odormix'], axis=1)
        step1 = pd.concat([data_trials, data_trials_iscorrect, data_trials_lick], axis=1, sort=False)

        training_type = training_types[index]
        step1['status'] = training_type
        #step1['group'] = mouse_group[mouse_name]
        counter[training_type] += 1
        step1['session'] = counter[training_type]
        #step1['dilution'] = training_type

        step1['trialnumber'] = step1.index + 1
        #step1['is_imaging'] = len(re.findall('-', mouse_name))
        step1['mouse_name'] = mouse_name
        #step1['phase'] = 1
        #step1['phase'] = 'pre'
        if index < 1:
            df_this_mouse = pd.DataFrame(step1)
        else:
            df_this_mouse = df_this_mouse.append(step1)
    mouse_dataframes[mouse_name] = df_this_mouse

# %%
from datetime import date

#version = date.today()
#version = 'E_Threshold'
version = 'learning'

df_list = []
for key, value in mouse_dataframes.items():
    df_list.append(value)
combined_df = pd.concat(df_list)

save_path = path
filename = 'combined_all_clean_{}'.format(version)
pickle_dict(combined_df, save_path, filename)

