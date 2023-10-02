# create list of trial types
# create list of lick/no lick (or reward/punish)
# bin the lists into chunks
# for every element in list, if it's a 6:3 for example, then determine if the elements n before it contained an airpuff
# then compare how many of the 6:3 that had vs  didn't have airpuff n before it resulted in licks
# start with just 1 before, iterate to 5 before, see  where strongest effect
# do for females vs males, light vs dark

from datetime import datetime
from datetime import date
import numpy as np
import pandas as pd
import matplotlib as mpl
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
from datamatrix import io
from statsmodels.stats.anova import AnovaRM
from parse_odormix import Mouse_data
from parse_odormix import pickle_dict
from parse_odormix import load_pickleddata

path='F:/My Drive/behavior data/valence_task_2023_go_no_66/parsed_dataframe_pickle'

pickled_data = os.path.join(path,'combined_all_clean_learning.pickle')
pickled_data = load_pickleddata(pickled_data)
pickled_data.index.duplicated()
#pickled_data = pickled_data.groupby(['mouse_name','session','odormix'])

one_eight_results = []
two_seven_results = []
# etc for the rest

#non-specific to odormix, but only for non easiest (1:8's)

# how iterate through "sessions" in each folder

#for session in pickled_data['session']:



def consequence_history(session):
    count_licked_airpuff = 0
    count_no_lick_airpuff = 0
    count_licked_nopuff = 0
    count_no_lick_nopuff = 0
    h = 3
    #for i, val in enumerate(pickled_data['odormix']) if i>3:


    
    for i in range(3,len(pickled_data['odormix'])):
        #for i in pickled_data['puffed']:
        if pickled_data['odormix'][i]== '0.5' or '0.77' or '0.66':
        #if pickled_data['odormix'][i]== '0.5':
            if pickled_data['licked'][i] == 1:
                if (any(pickled_data['puffed'][(i-h):(i-1)]== 1)) is True:
                    count_licked_airpuff+=1
                else:
                    count_licked_nopuff+=1
            if pickled_data['licked'][i] == 0:
                if any(pickled_data['puffed'][(i-h):(i-1)]== 1) is True:
                    count_no_lick_airpuff+=1
                else:
                    count_no_lick_nopuff+=1
        

    print (count_licked_airpuff/(count_licked_airpuff+count_licked_nopuff))
    print (count_no_lick_airpuff)
    print (count_licked_nopuff/(count_licked_airpuff+count_licked_nopuff))
    print (count_no_lick_nopuff)
# need to change to fraction of when airpuff before they lick vs no lick


# try same structure from butcher_combine?
# mouse_id = ['test']
# mouse_dataframes = {}

# for mouse_name in mouse_id:
#     print(mouse_name)
#     path='F:/My Drive/behavior data/valence_task_2023_go_no_66/parsed_dataframe_pickle'
#     filepath = os.path.join(path, '{}_stats.pickle'.format(mouse_name))
#     data = load_pickleddata(filepath)
#     counter = {'MixTypes1' :0, 'MixTypes2': 0, 'MixTypes4': 1, 'MixTypes3': 1, 'MixTypes5': 1}
#     training_types = data.training_type 
#     print(training_types)

#     for index, key in enumerate(data.df_trials):



#create df where for each mouse saving these in diff columns


consequence_history(pickled_data)

# do for no_gos specifically