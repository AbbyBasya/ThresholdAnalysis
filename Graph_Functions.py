#Graph_Functions

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
#sys.path.insert(0,'D:/PhD/Behavior/Behavior_Analysis/batch_clean_selected')
from parse_data_v2_1 import Mouse_data
from parse_data_v2_1 import pickle_dict
from parse_data_v2_1 import load_pickleddata
from datamatrix import io
from statsmodels.stats.anova import AnovaRM



#path = '/Volumes/GoogleDrive/My Drive/behavior data/experiment_data_2022_3_odor go_no-go_no_delay/parsed_dataframe_pickle'
path = 'F:/My Drive/behavior data/valence_task_2023_odor go_no-go_no_delay/parsed_dataframe_pickle'
path_excels = 'F:/My Drive/behavior data/valence_task_2023_go_no_66/parsed_dataframe_spreadsheet'

def prism_output(pickled_data):
    y = 'licked'
    g = g.groupby(['mouse_name','session','odormix'])[y].mean().reset_index()
    for_prism=pd.DataFrame(pickled_data)
    for_prism.sort_values('odormix')
    saving = path + 'maletesting.csv'
    for_prism.to_csv(saving)
    print(for_prism)

def correct_graph(path):
    y='is_Correct'
    pickled_data = os.path.join(path,'combined_all_clean_learning.pickle')
    pickled_data = load_pickleddata(pickled_data)
    pickled_data.index.duplicated()
    pickled_data = pickled_data[(pickled_data['trialtype'].isin(['no_go','go']))]
    pickled_data = pickled_data.groupby(['mouse_name','session','odormix'])[y].mean().reset_index()
    pickled_data['odormix'] = pd.Categorical(pickled_data['odormix'],
                                    categories=['0:8 Go','1:8 Go', '1:5 Go', '2:7 Go', '3:6 Go', '4:5 Go', '6:6', '5:4 No', '6:3 No', '7:2 No','5:1 No', '8:1 No', '8:0 No'],
                                    ordered=True)
    x = 'odormix'
    plot = sns.lineplot(data = pickled_data,x = x,y = y, marker = "o", hue="session",  legend = True, palette = sns.color_palette('bright', as_cmap=True))
    plt.show()

def lick_graph (pickled_data):
    y = 'licked'
    x = 'odormix'
    pickled_data = os.path.join(path,'combined_all_clean_learning.pickle')
    pickled_data = load_pickleddata(pickled_data)
    pickled_data.index.duplicated()
    pickled_data = pickled_data[(pickled_data['trialtype'].isin(['no_go','go']))]
    pickled_data = pickled_data.groupby(['mouse_name','session','odormix'])[y].mean().reset_index()
    pickled_data['odormix'] = pd.Categorical(pickled_data['odormix'],
                                    categories=['0:8 Go','1:8 Go', '1:5 Go', '2:7 Go', '3:6 Go', '4:5 Go', '6:6', '5:4 No', '6:3 No', '7:2 No','5:1 No', '8:1 No', '8:0 No'],
                                    ordered=True)
    plot = sns.lineplot(data = pickled_data,x = x,y = y, marker = "o", hue="session",  legend = True, palette = ['g', 'r', 'g'])
    plot.set_ylabel(">1 Lick (%)", fontsize = 15)
    plot.yaxis.set_ticks(np.arange(0, 1.05, 0.1))
    mpl.rcParams['font.size']=30
    plt.show()

def rate_graph(pickled_data):
    #y = 'rate_odor'
    y='rate_window'
    x = 'odormix'
    pickled_data = os.path.join(path,'combined_all_clean_learning.pickle')
    pickled_data = load_pickleddata(pickled_data)
    pickled_data.index.duplicated()
    pickled_data = pickled_data[(pickled_data['trialtype'].isin(['no_go','go']))]
    pickled_data = pickled_data.groupby(['mouse_name','session','odormix'])[y].mean().reset_index()    
    pickled_data['odormix'] = pd.Categorical(pickled_data['odormix'],
                                    categories=['0:8 Go','1:8 Go', '1:5 Go', '2:7 Go', '3:6 Go', '4:5 Go', '6:6', '5:4 No', '6:3 No', '7:2 No','5:1 No', '8:1 No', '8:0 No'],
                                    ordered=True)
    plot = sns.lineplot(data = pickled_data,x = x,y = y, marker = "o", hue="session",  legend = True, palette = ['g', 'r', 'g'])
    plot.set_ylabel("lick/s", fontsize = 15)
    plot.yaxis.set_ticks(np.arange(0, 1.05, 0.1))
    mpl.rcParams['font.size']=30
    plt.show()

def latency_graph(pickled_data):
    y = 'latency_to_odor'
    x = 'odormix'
    pickled_data = os.path.join(path,'combined_all_clean_learning.pickle')
    pickled_data = load_pickleddata(pickled_data)
    pickled_data.index.duplicated()
    pickled_data = pickled_data[(pickled_data['trialtype'].isin(['no_go','go']))]
    g = g.groupby(['mouse_name','session','odormix'])[y].mean().reset_index()
    pickled_data['odormix'] = pd.Categorical(pickled_data['odormix'],
                                    categories=['0:8 Go','1:8 Go', '1:5 Go', '2:7 Go', '3:6 Go', '4:5 Go', '6:6', '5:4 No', '6:3 No', '7:2 No','5:1 No', '8:1 No', '8:0 No'],
                                    ordered=True)    
    plot = sns.lineplot(data = g,x = x,y = y, marker = "o", hue="session",  legend = True, palette = sns.color_palette('bright', as_cmap=True))
    plot.set_ylabel("latency (s)", fontsize = 15)
    plot.yaxis.set_ticks(np.arange(0, 3, 0.5))
    mpl.rcParams['font.size']=30
    plt.show()

#lick_graph(path)
#correct_graph(path)
rate_graph(path)