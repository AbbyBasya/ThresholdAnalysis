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


#path = '/Volumes/GoogleDrive/My Drive/behavior data/experiment_data_2022_3_odor go_no-go_no_delay/parsed_dataframe_pickle'
path = 'H:/My Drive/behavior data/valence_task_2023_odor go_no-go_no_delay/parsed_dataframe_pickle'

#females = os.path.join(path,'combined_all_clean_G_females.pickle')
#males = os.path.join(path,'combined_all_clean_G_males.pickle')

g = os.path.join(path,'combined_all_clean_learning.pickle')


#f = load_pickleddata(females)
#m = load_pickleddata(males)
g = load_pickleddata(g)


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
g.index.duplicated()


y = 'is_Correct'
#y= 'rate_odor'
#y='rate_window'
#y = 'latency_to_odor'
#x = 'session'
x = 'odormix'

values = ['', 'day1', 'day2', 'day3', 'day4']

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
g = g[(g['trialtype'].isin(['no_go','go']))]
# cold_test = post_data[(post_data['dilution'].isin(['6']))]

#data_deg_cond =  data_deg_cond.groupby(['mouse_name','session','phase'])[y].mean().reset_index()
# data_pre =  data_pre.groupby(['mouse_name','dilution'])[y].mean().reset_index()
# data_post =  data_post.groupby(['mouse_name','dilution'])[y].mean().reset_index()
# social_pre=social_pre.groupby(['mouse_name','dilution'])[y].mean().reset_index()
# social_post=social_post.groupby(['mouse_name','dilution'])[y].mean().reset_index()
#f = f.groupby(['mouse_name','dilution'])[y].mean().reset_index()


#g = g.groupby(['mouse_name'])[y].mean().reset_index()

g = g.groupby(['mouse_name','session','odormix'])[y].mean().reset_index()


# cold_test= cold_test.groupby(['mouse_name'])[y].mean().reset_index()

#plot = sns.lineplot(data = data_pre,x = x,y = y, marker="o",ci='sd', err_style='bars')
#plot = sns.lineplot(data = data_post,x = x,y = y, marker="o",ci='sd', err_style='bars')
#plot = sns.lineplot(data = social_post,x = x,y = y, marker="o",ci='sd', err_style='bars')
#plot= sns.lineplot(data = social_pre,x = x,y = y, marker="o",ci='sd', err_style='bars')


#plot = sns.lineplot(data = data_pre,x = x,y = y, marker="o",hue="mouse_name",palette=['g','r','b'])
#plot = sns.lineplot(data = data_post,x = x,y = y, marker="o",hue="mouse_name",palette=['g','r'],linestyle='dashed')


#plot = sns.boxplot(data = data_pre, column= '5', x = 5,y = y)
#plt.scatter(x=5, y=y)

#print(data_post)
#data_post = data_post.reindex(columns=['Name', 'Gender', 'Age', 'City', 'Education'])

#leg = plot.legend()
#leg_lines = leg.get_lines()
#leg_lines[4].set_linestyle(":")

#plot = sns.lineplot(data = g,x = x,y = y, marker = "o", hue="odormix", ci=68, err_style='bars')
#plot = sns.barplot(data = g,x = x,y = y, marker = "o", hue="odormix#", ci=68, err_style='bars', hue_order = ('8:0 Go' ,'1:8 Go', '2:7 Go', '3:6 Go', '6:3 No', '7:2 No', '8:1 No', '8:0 No'))
#
# g['odormix'] = pd.Categorical(g['odormix'],
#                                     categories=['8:0 Go','1:8 Go', '2:7 Go', '3:6 Go', '4:5 Go', '5:4 No', '6:3 No', '7:2 No', '8:1 No', '8:0 No'],
#                                     ordered=True)

g['odormix'] = pd.Categorical(g['odormix'],
                                    categories=['0:8 Go','1:8 Go', '1:5 Go', '2:7 Go', '3:6 Go', '6:6 Go', '6:6 No', '6:3 No', '7:2 No','5:1 No', '8:1 No', '8:0 No'],
                                    ordered=True)

#plot = sns.lineplot(data = g,x = x,y = y, marker = "o", hue="odormix", ci=68, err_style='bars', legend = True)
plot = sns.lineplot(data = g,x = x,y = y, marker = "o", hue="session",  legend = True, palette=['g','r','g','r'])

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

plt.locator_params(axis="x", integer=True, tight=True)
#plot.yaxis.set_ticks(np.arange(0.4, 1, 0.05))


#sns.move_legend(plot, "upper left", bbox_to_anchor=(1, 1))

#plt.locator_params(axis="both", tight=True)

#plt.xticks(ticks = x ,labels = values, rotation = 'vertical')

mpl.rcParams['font.size']=30

#plt.gca().invert_xaxis()

plt.show()


