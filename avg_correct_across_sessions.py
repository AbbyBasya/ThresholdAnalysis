# -*- coding: utf-8 -*-

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

#sys.path.insert(0, '/Users/lechenqian/Dropbox (Uchida Lab)/Analyze_behavioral_data/functions')
from parse_data_v2_1 import Mouse_data
from parse_data_v2_1 import pickle_dict
from parse_data_v2_1 import load_pickleddata
from statannot import add_stat_annotation

# %% load combined dataframes
path = input('Where to load the concatenated df? >>>   ')
filename = 'df_of_concatenated_clean_2021-10-21.pickle'
data = load_pickleddata(os.path.join(path, filename))
savefig_path = '/Users/lechenqian/Dropbox (Uchida Lab)/Analyze_behavioral_data/figures/{}'.format(date.today())

# %% comparison bettween control and deg

x = 'session'
# y = 'norm_rate_antici'
# y = 'anti_duration'
# y = 'latency_to_odor'
# y = 'latency_to_rew'
y = 'is_Correct'
# %%
# data_deg_cond = data[(data['group'].isin(['control','deg']))&
#                      (data['trialtype'].isin(['go','go_omit']))]
data_deg_cond = data[(data['group'].isin(['control', 'deg'])) &
                     (data['trialtype'].isin(['go', 'go_omit']))]  # for rate after

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

# %% plot the ratio between go odor licking and background licking rate
data_deg_cond_go = data[(data['group'].isin(['control', 'deg'])) &
                        (data['trialtype'].isin(['go', 'go_omit']))]  # for rate after

data_deg_cond_bg = data[(data['group'].isin(['control', 'deg'])) &
                        (data['trialtype'].isin(['background']))]
data_deg_cond_go = data_deg_cond_go.groupby(['mouse_name', 'session', 'group',
                                             'phase'])['rate_antici'].mean().reset_index()
data_deg_cond_bg = data_deg_cond_bg.groupby(['mouse_name', 'session', 'group',
                                             'phase'])['lick_rate_whole_trial'].mean().reset_index()

df_groupby_ratio = data_deg_cond_go.copy()

df_groupby_ratio['bg_lick_rate'] = data_deg_cond_bg['lick_rate_whole_trial']
# because background licking has more 0
# when 0/0, pandas will put nan there instead of inf
df_groupby_ratio['bg/go_lick_rate'] = df_groupby_ratio['bg_lick_rate'] / df_groupby_ratio['rate_antici']

sns.set_context("talk", font_scale=0.9)
sns.color_palette("Set2")

fig, ax = plt.subplots(1, 1, figsize=(6, 5))
# palette = sns.color_palette("mako_r", 2)
sns.lineplot(data=df_groupby_ratio, x=x, y='bg/go_lick_rate', hue='group', style='phase',
             ax=ax, markers=True, err_style="bars",
             ci=68, palette='Set2')
sns.scatterplot(data=df_groupby_ratio, x=x, y='bg/go_lick_rate', hue='group',
                ax=ax, markers=True, alpha=0.3,
                ci=68, palette='Set2')
plt.legend(frameon=False, fontsize=12, bbox_to_anchor=(1.01, 1))
sns.despine()

plt.savefig(os.path.join(savefig_path, 'control_vs_deg_{}.pdf'.format('bgvsgo_lick_rate')),
            bbox_inches="tight", dpi=400)
plt.savefig(os.path.join(savefig_path, 'control_vs_deg_{}.eps'.format('bgvsgo_lick_rate')),
            bbox_inches="tight", dpi=400)
plt.savefig(os.path.join(savefig_path, 'control_vs_deg_{}.png'.format('bgvsgo_lick_rate')),
            bbox_inches="tight", dpi=400)















