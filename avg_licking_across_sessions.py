# -*- coding: utf-8 -*-

# %% import functions
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

sys.path.insert(0, '/Users/lechenqian/Dropbox (Uchida Lab)/Analyze_behavioral_data/functions')
from parse_data_v2_1 import Mouse_data
from parse_data_v2_1 import pickle_dict
from parse_data_v2_1 import load_pickleddata
from statannot import add_stat_annotation

# %% load combined dataframes
path = input('Where to load the concatenated df? >>>   ')
filename = 'df_of_concatenated_clean_2021-10-21.pickle'
data = load_pickleddata(os.path.join(path, filename))
savefig_path = '/Users/lechenqian/Dropbox (Uchida Lab)/Analyze_behavioral_data/figures/{}'.format(date.today())

# %%
# %% normalization
new_data_rate_antici = data[
    (data['status'] == 'cond') & (data['session'] <= 5) & (data['trialtype'].isin(['go', 'go_omit']))]
data1 = new_data_rate_antici.groupby(by=['mouse_name', 'session']).mean()
max_anti_lick = {}
data['norm_rate_antici'] = 0
for mouse_name in data['mouse_name'].unique():
    max_lick = data1.loc[pd.IndexSlice[mouse_name, :], 'rate_antici'].max()
    max_anti_lick[mouse_name] = max_lick
    new_array = data[data['mouse_name'] == mouse_name]['rate_antici'] / max_anti_lick[mouse_name]
    data.loc[data['mouse_name'] == mouse_name, 'norm_rate_antici'] = new_array

new_data_rate_after = data[(data['status'] == 'cond') & (data['session'] <= 5) & (data['trialtype'].isin(['go']))]
data2 = new_data_rate_antici.groupby(by=['mouse_name', 'session']).mean()
max_after_lick = {}
data['norm_rate_after'] = 0
for mouse_name in data['mouse_name'].unique():
    max_lick = data2.loc[pd.IndexSlice[mouse_name, :], 'rate_after'].max()
    max_after_lick[mouse_name] = max_lick
    new_array = data[data['mouse_name'] == mouse_name]['rate_after'] / max_after_lick[mouse_name]
    data.loc[data['mouse_name'] == mouse_name, 'norm_rate_after'] = new_array
# %% comparison bettween control and deg

x = 'session'
y = 'norm_rate_antici'
# y = 'anti_duration'
# y = 'latency_to_odor'
# y = 'latency_to_rew'
# y = 'norm_rate_after'
# %%
# data_deg_cond = data[(data['group'].isin(['control','deg']))&
#                      (data['trialtype'].isin(['go','go_omit']))]
data_deg_cond = data[(data['group'].isin(['control', 'deg'])) &
                     (data['trialtype'].isin(['go']))]  # for rate after

data_deg_cond = data_deg_cond.groupby(['mouse_name', 'session', 'group',
                                       'phase'])[y].mean().reset_index()

sns.set_context("talk", font_scale=0.9)
sns.color_palette("Set2")

fig, ax = plt.subplots(1, 1, figsize=(6, 5))
# palette = sns.color_palette("mako_r", 2)
sns.lineplot(data=data_deg_cond, x=x, y=y, hue='group', style='phase',
             ax=ax, markers=True, err_style="bars",
             ci=68, palette='Set2')
sns.scatterplot(data=data_deg_cond, x=x, y=y, hue='group',
                ax=ax, markers=True, alpha=0.3,
                ci=68, palette='Set2')
plt.legend(frameon=False, fontsize=12, bbox_to_anchor=(1.01, 1))
sns.despine()

plt.savefig(os.path.join(savefig_path, 'control_vs_deg_{}.pdf'.format(y)),
            bbox_inches="tight", dpi=400)
plt.savefig(os.path.join(savefig_path, 'control_vs_deg_{}.eps'.format(y)),
            bbox_inches="tight", dpi=400)
plt.savefig(os.path.join(savefig_path, 'control_vs_deg_{}.png'.format(y)),
            bbox_inches="tight", dpi=400)
# %%
from datetime import date

version = date.today()

# save concatenated dataframe
save_path = path
filename = 'df_of_concatenated_clean_{}'.format(version)
pickle_dict(data, save_path, filename)


