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
#path = 'F:/My Drive/behavior data/valence_task_2023_odor go_no-go_no_delay/parsed_dataframe_pickle'
path='F:/My Drive/behavior data/valence_task_2023_go_no_66/parsed_dataframe_pickle'
path_excels = 'F:/My Drive/behavior data/valence_task_2023_go_no_66/parsed_dataframe_spreadsheet'

#females = os.path.join(path,'combined_all_clean_G_females.pickle')
#males = os.path.join(path,'combined_all_clean_G_males.pickle')




#f = load_pickleddata(females)
#m = load_pickleddata(males)




# event plot with trials and iscorerct data

# assign two df


# filepath1 = os.path.join(path,'combined_all_clean_iso_pre.pickle')
# pre_data = load_pickleddata(filepath1)
#
# filepath2=os.path.join(path,'combined_all_clean_iso_post.pickle')
# post_data = load_pickleddata(filepath2)
#
# filepath3 = os.path.join(path,'combined_all_clean_social_pre.pickle')
# social_pre=load_pickleddata(filepath3)
#
# filepath4 = os.path.join(path,'combined_all_clean_social_post.pickle')
# social_post=load_pickleddata(filepath4)

# pre_data.index.duplicated()
# post_data.index.duplicated()
# social_post.index.duplicated()
# social_pre.index.duplicated()
#f.index.duplicated()
#m.index.duplicated()




#values= ['','baseline','after_2_weeks']
#values = ['5*10^-2','5*10^-3','5*10^-4','5*10^-5','5*10^-6']
#values_water = ['pipet vs non-pipet','pipet vs non-pipet','pipet vs pipet','pipet vs non-pipet']
#values = ['5*10^-1','5*10^-2','5*10^-4','5*10^-5']

# data_pre = pre_data[(pre_data['trialtype'].isin(['go','no_go']))]
# data_post = post_data[(post_data['trialtype'].isin(['go','no_go']))]
# social_pre = social_pre[(social_pre['trialtype'].isin(['go','no_go']))]
# social_post = social_post[(social_post['trialtype'].isin(['go','no_go']))]
#f = f[(f['trialtype'].isin(['go','no_go']))]
#m = m[(m['trialtype'].isin(['go','no_go']))]
# cold_test = post_data[(post_data['dilution'].isin(['6']))]

#data_deg_cond =  data_deg_cond.groupby(['mouse_name','session','phase'])[y].mean().reset_index()
# data_pre =  data_pre.groupby(['mouse_name','dilution'])[y].mean().reset_index()
# data_post =  data_post.groupby(['mouse_name','dilution'])[y].mean().reset_index()
# social_pre=social_pre.groupby(['mouse_name','dilution'])[y].mean().reset_index()
# social_post=social_post.groupby(['mouse_name','dilution'])[y].mean().reset_index()
#f = f.groupby(['mouse_name','dilution'])[y].mean().reset_index()


#g = g.groupby(['mouse_name'])[y].mean().reset_index()

#g[g[:, 2].argsort()]


#print(np.shape(g))

#for_prism = pd.DataFrame(g['mouse_name'],g['session'],g['odormix'])
#for_prism.sort_values(by=['mouse_name'])
#for_prism.sort_values(by=['mouse_name','session','odormix'])

#print(for_prism)
#g = g.groupby(['mouse_name','session'])[y].mean().reset_index()


# cold_test= cold_test.groupby(['mouse_name'])[y].mean().reset_index()

#plot = sns.lineplot(data = data_pre,x = x,y = y, marker="o",ci='sd', err_style='bars')
#plot = sns.lineplot(data = data_post,x = x,y = y, marker="o",ci='sd', err_style='bars')
#plot = sns.lineplot(data = social_post,x = x,y = y, marker="o",ci='sd', err_style='bars')
#plot= sns.lineplot(data = social_pre,x = x,y = y, marker="o",ci='sd', err_style='bars')


#plot = sns.lineplot(data = data_pre,x = x,y = y, marker="o",hue="mouse_name",palette=['g','r','b'])
#plot = sns.lineplot(data = data_post,x = x,y = y, marker="o",hue="mouse_name",palette=['g','r'],linestyle='dashed')


#plot = sns.boxplot(data = data_pre, column= '5', x = 5,y = y)
#plt.scatter(x=5, y=y)


#leg = plot.legend()
#leg_lines = leg.get_lines()
#leg_lines[4].set_linestyle(":")

#plot = sns.lineplot(data = g,x = x,y = y, marker = "o", hue="odormix", ci=68, err_style='bars')
#plot = sns.barplot(data = g,x = x,y = y, marker = "o", hue="odormix#", ci=68, err_style='bars', hue_order = ('8:0 Go' ,'1:8 Go', '2:7 Go', '3:6 Go', '6:3 No', '7:2 No', '8:1 No', '8:0 No'))
#
# g['odormix'] = pd.Categorical(g['odormix'],
#                                     categories=['8:0 Go','1:8 Go', '2:7 Go', '3:6 Go', '4:5 Go', '5:4 No', '6:3 No', '7:2 No', '8:1 No', '8:0 No'],
#                                     ordered=True)



# g['odormix'] = pd.Categorical(g['odormix'],
#                                     categories=['1:8 Go', '2:7 Go', '3:6 Go', '6:6', '6:3 No', '7:2 No','8:1 No'],
#                                     ordered=True)


#plot = sns.lineplot(data = g,x = x,y = y, marker = "o", hue="odormix", ci=68, err_style='bars', legend = True)

#color = (sns.set_palette("bright")

#plot = sns.lineplot(data = g,x = x,y = y, marker = "o", hue="session",  legend = True, palette = sns.color_palette('bright', as_cmap=True))
#plot = sns.lineplot(data = g,x = x,y = y, marker = "o", hue="session",  legend = True, palette = ['g', 'g', 'purple','purple','r','r'])
#plot = sns.lineplot(data = g,x = x,y = y, marker = "o", hue="mouse_name", err_style='bars', errorbar="se", legend = True, palette = ['magenta','orange','purple','b','r'])
#plot = sns.scatterplot(data = g,x = x,y = y, hue="mouse_name")


#dm=io.readpickle(os.path.join(path,'combined_all_clean_learning.pickle'))

# females = os.path.join(path_excels,'females_pre_dark_lick_stat.xlsx')
# dataframe_fe=pd.read_excel(females)

# males = os.path.join(path_excels,'males_pre_dark_lick_stat.xlsx')
# dataframe_male = pd.read_excel(males)


#plot.set_ylabel(">1 Lick (%)", fontsize = 15)
#plot.set_ylabel("lick/s", fontsize = 15)
#plot.set_ylabel("latency (s)", fontsize = 15)


#plot.yaxis.set_ticks(np.arange(0, 1.05, 0.1))
#plot.yaxis.set_ticks(np.arange(0, 7, 1))
#plot.yaxis.set_ticks(np.arange(0, 3, 0.5))


def prism_output(path):
    #y = 'rate_window'
    #y= 'licked'
    y = 'latency_to_odor'
    pickled_data = os.path.join(path,'combined_all_clean_learning.pickle')
    pickled_data = load_pickleddata(pickled_data)
    pickled_data.index.duplicated()
    pickled_data = pickled_data[(pickled_data['trialtype'].isin(['no_go','go']))]
    pickled_data = pickled_data.groupby(['mouse_name','session','odormix'])[y].mean().reset_index()
    for_prism=pd.DataFrame(pickled_data)
    for_prism.sort_values('odormix')
    saving = path + 'latency.csv'
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
    plot = sns.lineplot(data = pickled_data,x = x,y = y, marker = "o", hue="session",  legend = True, palette = ['g', 'r', 'g','b'])
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
    plot = sns.lineplot(data = pickled_data,x = x,y = y, marker = "o", hue="mouse_name",  legend = True, palette = ['g', 'r', 'b'])
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
    plot = sns.lineplot(data = pickled_data,x = x,y = y, marker = "o", hue="mouse_name",  legend = True, palette = ['g', 'r', 'g'])
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
    pickled_data = pickled_data.groupby(['mouse_name','session','odormix'])[y].mean().reset_index()
    #pickled_data['odormix'] = pd.Categorical(pickled_data['odormix'],
                                    #categories=['0:8 Go','1:8 Go', '1:5 Go', '2:7 Go', '3:6 Go', '4:5 Go', '6:6', '5:4 No', '6:3 No', '7:2 No','5:1 No', '8:1 No', '8:0 No'],
                                    #ordered=True)    
    plot = sns.lineplot(data = pickled_data,x = x,y = y, marker = "o", hue="mouse_name",  legend = True, palette = sns.color_palette('bright', as_cmap=True))
    plot.set_ylabel("latency (s)", fontsize = 15)
    plot.yaxis.set_ticks(np.arange(0, 3, 0.5))
    mpl.rcParams['font.size']=30
    plt.show()


#lick_graph(path)
#correct_graph(path)
#rate_graph(path)
#latency_graph(path)
prism_output(path)









#plot.yaxis.set_ticks(np.arange(0.25, 1.05, 0.05))


#plot = sns.lineplot(data = g,x = x,y = y, marker = "o")



#plot = sns.lineplot(data = g,x = x,y = y, marker = "o")
#plot = sns.lineplot(data = g,x = x,y = y, palette=['r'])

#plot=sns.boxplot(data = g,x = x,y = y)


#plot = sns.lineplot(data = m,x = x,y = y, palette=['g'])
#plot = sns.lineplot(data = g,x = x,y = y, palette=['r'])
#plot = sns.lineplot(data = g,x = x,y = y, hue="mouse_name")


# my_dict = dict(x=x, y=y)
# data = pd.DataFrame(my_dict)
# fig, ax= plt.subplots()
# ax =  sns.lineplot(data = m,x = x,y = y, palette=['g'])
# ax1 = sns.lineplot(data = m,x = x,y = y, palette=['r'])

#plot=sns.boxplot(data = cold,x = x,y = y, position=(0,1))


#plot = sns.lineplot(data = social_post,x = x,y = y, marker="o",hue="mouse_name", palette=['g'])
#plot = sns.lineplot(data = social_pre,x = x,y = y, marker="o",hue="mouse_name")

#plot = sns.lineplot(data = data_deg_cond,x = x,y = y, marker="o",hue="phase")
#plot.set_xlabel("Concentration", fontsize = 10)
#plot.set_xlabel("Training Day", fontsize = 15)

#plot.set_ylabel("anticipatory lick rate", fontsize = 15)

#plot.set_ylabel("Refrain from licking No_Go", fontsize = 10)
#plot.set_ylabel("Latency to Rewarded Odor (s)", fontsize = 10)


#plot.axes.set_xticklabels(labels = "odormix", fontsize = 15)
#plot.axes.set_yticklabels(fontsize = 15)


#for i, j in zip(x, y):
 #   plot.annotate(str(j),xy=(i,j))


#plot.set_ylim (0.4,1)


# label = "{:.2f}".format(y)
# plt.annotate(label, # this is the text
#                  (x,y), # these are the coordinates to position the label
#                  textcoords="offset points", # how to position the text
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center


#sns.lineplot(data = data_deg_cond,x = x,y = y, marker="o")


#plt.locator_params(axis="x", integer=True, tight=True)



#sns.move_legend(plot, "upper left", bbox_to_anchor=(1, 1))

#plt.locator_params(axis="both", tight=True)

#plt.xticks(ticks = x ,labels = values, rotation = 'vertical')



#plt.gca().invert_xaxis()

#plt.show()


