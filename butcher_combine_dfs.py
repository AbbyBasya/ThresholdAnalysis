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

mouse_id = ['S3_patched_together','S2_patched_together']
mouse_dataframes = {}

for mouse_name in mouse_id:
    print(mouse_name)

    path = 'G:/My Drive/behavior data/experiment_data_2022_3_cheat_go_no/parsed_dataframe_pickle'
    filepath = os.path.join(path, '{}_stats.pickle'.format(mouse_name))
    data = load_pickleddata(filepath)
    counter = {'cheat_go_no': 0}
    training_types = data.training_type
    print(training_types)
    for index, key in enumerate(data.df_trials):

        data_trials = data.df_trials[key]
        data_trials_iscorrect = data.df_trials_iscorrect[key].drop(columns=['trialtype'], axis=1)
        data_trials_lick = data.df_trials_lick[key].drop(columns=['trialtype'], axis=1)
        step1 = pd.concat([data_trials, data_trials_iscorrect, data_trials_lick], axis=1, sort=False)

        training_type = training_types[index]
        step1['status'] = training_type
        #step1['group'] = mouse_group[mouse_name]
        counter[training_type] += 1
        step1['session'] = counter[training_type]
        step1['trialnumber'] = step1.index + 1
        #step1['is_imaging'] = len(re.findall('-', mouse_name))
        step1['mouse_name'] = mouse_name
        step1['phase'] = 1
        if index < 1:
            df_this_mouse = pd.DataFrame(step1)
        else:
            df_this_mouse = df_this_mouse.append(step1)
    mouse_dataframes[mouse_name] = df_this_mouse

# %%
from datetime import date

version = date.today()

df_list = []
for key, value in mouse_dataframes.items():
    df_list.append(value)
combined_df = pd.concat(df_list)

save_path = path
filename = 'combined_all_clean_{}'.format(version)
pickle_dict(combined_df, save_path, filename)

