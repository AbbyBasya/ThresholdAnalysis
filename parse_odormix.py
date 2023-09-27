# -*- coding: utf-8 -*-
"""

"""
from datetime import datetime
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
import xlsxwriter

# %%
class Mouse_data:
    def __init__(self, mouse_id, filedir):
        self.mouse_id = mouse_id
        self.filedir = filedir
        self.filename = ''
        self.selected_filename = ''
        self.all_days = []

        self.training_type = []
        self.df_trials = {}
        self.trialtypes = []
        self.odormix = []
        self.df_trials_iscorrect = {}
        self.df_trials_lick = {}
        self.df_eventcode = {}
        self.p_hit = {}
        self.p_correj = {}
        self.licking_actionwindow = {}
        self.licking_latency = {}
        self.licking_baselicking = {}
        self.stats = {}
        self.event_data = ''
        self.odor_bef = 3.2
        self.odor_on = 1.5
        self.delay = 1
        self.rew_after = 2

    def read_filename(self):
        filedir = self.filedir + '/{}'.format(self.mouse_id)
        filename = []
        for dirpath, dirnames, files in os.walk(filedir):  # can walk through all levels down
            #     print(f'Found directory: {dirpath}')
            for f_name in files:
                if f_name.endswith('.xlsx'):
                    filename.append(dirpath + '/' + f_name)
                    print(f_name)
        print('---------------------------------------------')
        print('The files have been loaded from the following paths')
        print(filename[-45:])
        self.filename = filename

    def select_dates(self):
        pass

    def delete_date(self, dates):
        for date in dates:
            self.all_days.remove(date)

        return self.all_days

    def create_eventcode(self, original=True):  # {'date':df of eventcode} format from original CSV
        date_list = []
        df = {}
        training_type = []

        for file in self.filename:
            date = re.search(r"(\d{4}-\d{1,2}-\d{1,2}-\d{1,2}-\d{1,2})", file).group(
                0)  # extract date: must be like format 2020-02-10
            date_list.append(date)  # create a list of emperiment date

            train_type = os.path.split(file)[-1][16:-5]


            training_type.append(train_type)  ###

            data = pd.read_excel(file, header=0 if original else None)  # read orginal csv data
            data.columns = ['Time', 'Event', 'Type', 'Mix']  # rename columns

            df.update({date: data})  # create the dict of key: date and value: data dataframe
        self.df_eventcode = df  # individual mouse event code data
        date_format = '%Y-%m-%d-%h-%s'
        index = np.argsort(date_list)
        self.all_days = [date_list[i] for i in index]
        self.training_type = [training_type[i] for i in index]

        print('---------------------------------------------')
        print('{0} has data from these days: {1}'.format(self.mouse_id, zip(self.all_days, self.training_type)))

    def create_trials(self):  # {'date: df of trials}
        for index, date in enumerate(self.all_days):
            value = self.df_eventcode[date]

            new_df = self.generate_trials_dataframe(index, value)
            self.df_trials[date] = new_df
            print('{} done!'.format(date))

    def generate_trials_dataframe(self, index, ori_df):

        lick, trialtype, odormix, go_odor, nogo_odor, control_odor, water_on, water_off, airpuff_on, airpuff_off, trial_end = self.seperate_events(
            index,
            ori_df)
        d = {'trialtype' : trialtype, 'odormix': odormix, 'go_odor': go_odor, 'nogo_odor': nogo_odor,
             'control_odor': control_odor,
             'water_on': water_on, 'water_off': water_off, 'airpuff_on':airpuff_on , 'airpuff_off': airpuff_off ,'licking': lick,
             'trial_end': trial_end}
        df_trial = pd.DataFrame(data=d)
        return df_trial

    def seperate_events(self, index_day, df):

        start_trials = 0
        lick = []
        trialtype = []
        odormix = []
        go_odor = []
        nogo_odor = []
        control_odor = []
        water_on = []
        water_off = []
        airpuff_on = []
        airpuff_off = []
        trial_end = []
        print(index_day)

        for index, row in df.iterrows():
            if row['Event'] == 101:  # trial start
                start_trials = row['Time']
                temp_licks = []
                temp_go_odor_on = np.nan
                temp_go_odor_off = np.nan
                temp_nogo_odor_on = np.nan
                temp_nogo_odor_off = np.nan
                temp_control_odor_on = np.nan
                temp_control_odor_off = np.nan

                temp_water_on = np.nan
                temp_water_off = np.nan

                temp_airpuff_on = np.nan
                temp_airpuff_off = np.nan
                temp_trial_end = np.nan

                if row['Type'] == 'trial1':
                    trialtype.append('no_go')
                    if row['Mix'] == 'punish_mix81':
                        odormix.append('8:1 No')
                    elif row['Mix'] == 'punish_mix80':
                        odormix.append('8:0 No')
                    elif row['Mix'] == 'punish_mix63':
                        odormix.append('6:3 No')
                    elif row['Mix'] == 'punish_mix72':
                        odormix.append('7:2 No')
                    elif row['Mix'] == 'mix80':
                        odormix.append('8:0 No')
                    elif row['Mix'] == 'mix81':
                        odormix.append('0.88')
                    elif row['Mix'] == 'mix63':
                        odormix.append('0.66')
                    elif row['Mix'] == 'mix72':
                        odormix.append('0.77')
                    elif row['Mix'] == 'mix54':
                        odormix.append('5:4 No')
                    elif row['Mix'] == 'mix51':
                        odormix.append('0.83')
                    elif row['Mix'] == 'mix66':
                        odormix.append('0.5')

                
                elif row['Type'] == 'trial0':
                    trialtype.append('go')
                    if row['Mix'] == 'reward_mix81':
                        odormix.append('1:8 Go')
                    elif row['Mix'] == 'reward_mix80':
                        odormix.append('0:8 Go')
                    elif row['Mix'] == 'reward_mix63':
                        odormix.append('3:6 Go')
                    elif row['Mix'] == 'reward_mix72':
                        odormix.append('2:7 Go')
                    elif row['Mix'] == 'mix80':
                        odormix.append('0:8 Go')
                    elif row['Mix'] == 'mix81':
                        odormix.append('0.11')
                    elif row['Mix'] == 'mix63':
                        odormix.append('0.33')
                    elif row['Mix'] == 'mix72':
                        odormix.append('0.22')
                    elif row['Mix'] == 'mix54':
                        odormix.append('4:5 Go')
                    elif row['Mix'] == 'mix51':
                        odormix.append('0.166')
                    elif row['Mix'] == 'mix66':
                        odormix.append('0.5')
                    elif row['Mix'] == 'mix54':
                        odormix.append('4:5 Go')

                elif row['Type'] == 'trial2':
                    trialtype.append('go')
                    odormix.append('0.5')
                elif row['Type'] == 'trial3':
                    trialtype.append('go')
                    odormix.append('0.5')





            elif row['Event'] == 11:
                lick_time = row['Time'] - start_trials
                temp_licks.append(lick_time)

            elif row['Event'] == 131:  # go odor on
                temp_go_odor_on = row['Time'] - start_trials

            elif row['Event'] == 130:
                temp_go_odor_off = row['Time'] - start_trials

            elif row['Event'] == 141:  # no go odor on
                temp_nogo_odor_on = row['Time'] - start_trials

            elif row['Event'] == 140:
                temp_nogo_odor_off = row['Time'] - start_trials
            elif row['Event'] == 161:  # no go odor on
                temp_control_odor_on = row['Time'] - start_trials

            elif row['Event'] == 160:
                temp_control_odor_off = row['Time'] - start_trials

            elif row['Event'] == 51:  # water on
                temp_water_on = row['Time'] - start_trials

            elif row['Event'] == 50:
                temp_water_off = row['Time'] - start_trials

            elif row['Event'] ==666:  # airpuff on
                temp_water_on = row['Time'] - start_trials

            elif row['Event'] == 667:   #airpuff off
                temp_water_off = row['Time'] - start_trials

            elif row['Event'] == 100:  # trial end
                temp_trial_end = row['Time'] - start_trials

                lick.append(temp_licks)
                go_odor.append([temp_go_odor_on, temp_go_odor_off])

                nogo_odor.append([temp_nogo_odor_on, temp_nogo_odor_off])
                control_odor.append([temp_control_odor_on, temp_control_odor_off])
                water_on.append(temp_water_on)
                water_off.append(temp_water_off)
                airpuff_on.append(temp_airpuff_on)
                airpuff_off.append(temp_airpuff_off)
                trial_end.append(temp_trial_end)

        return lick, trialtype, odormix, go_odor, nogo_odor, control_odor, water_on, water_off, airpuff_on, airpuff_off, trial_end

    def create_trial_iscorrect(
            self):  # create dataframe with trial number, correct or rewarded or not only for conditioning period
        for index, date in enumerate(self.all_days):
            value = self.df_trials[date]
            new_df = self.eval_trials_correct(value)
            #new_df.insert(0, 'trialtype', value['trialtype'])
            new_df.insert(0, 'odormix', value['odormix'])
            #new_df.insert(0, 'trialtype', value['trialtype'])#
            self.df_trials_iscorrect[date] = new_df
            print('create_trial_iscorrect done!')

    def eval_trials_correct(self, df):

        is_correct = []
        is_rewarded = []
        licked = []
        watered = []
        puffed = []

        for index, row in df.iterrows():
            if row['trialtype'] == 'go':
                is_rewarded.append(1)
                puffed.append(0)
                # if any(x > row['go_odor'][0] and x < row['go_odor'][1] + self.delay for x in row['licking']):
                if any((x > row['go_odor'][1] and x < (row['go_odor'][1]+ self.delay)) for x in row['licking']):
                #if any(row['go_odor'][1]<x< (row['go_odor'][1]+ self.delay))
                    is_correct.append(1)
                    licked.append(1)
                    watered.append(1)
                elif any((x > row['nogo_odor'][1] and x < (row['nogo_odor'][1]+ self.delay)) for x in row['licking']):
                #if any(row['go_odor'][1]<x< (row['go_odor'][1]+ self.delay))
                    is_correct.append(1)
                    licked.append(1)
                    watered.append(1)
                else:
                    is_correct.append(0)
                    licked.append(0)
                    watered.append(0)
                    
            
            
            elif row['trialtype'] == 'no_go':
                is_rewarded.append(0)
                watered.append(0)
                # if any(x > row['nogo_odor'][0] and x < row['nogo_odor'][1] + self.delay for x in row['licking']):
                if any((x > row['nogo_odor'][1] and x < (row['nogo_odor'][1]+ self.delay)) for x in row['licking']):
                    is_correct.append(0)
                    licked.append(1)
                    puffed.append(1)
                elif any((x > row['go_odor'][1] and x < (row['go_odor'][1]+ self.delay)) for x in row['licking']):
                #if any(row['go_odor'][1]<x< (row['go_odor'][1]+ self.delay))
                    is_correct.append(0)
                    licked.append(1)
                    puffed.append(1)
                else:
                    is_correct.append(1)
                    licked.append(0)
                    puffed.append(0)


        # for index, row in df.iterrows():
            # if row['odormix'] == '1:8 Go'or '2:7 Go' or '3:6 Go':
            #     is_rewarded.append(1)
            #     # if any(x > row['go_odor'][0] and x < row['go_odor'][1] + self.delay for x in row['licking']):
            #     if any(x > row['go_odor'][1] and x < row['go_odor'][1] + self.delay for x in row['licking']):
            #         is_correct.append(1)
            #     else:
            #         is_correct.append(0)
            #
            # elif row['odormix'] == '8:1 No' or '7:2 No' or '6:3 No':
            #     is_rewarded.append(0)
            #     # if any(x > row['nogo_odor'][0] and x < row['nogo_odor'][1] + self.delay for x in row['licking']):
            #     if any(x > row['nogo_odor'][1] and x < row['nogo_odor'][1] + self.delay for x in row['licking']):
            #         is_correct.append(0)
            #     else:
            #         is_correct.append(1)

            elif row['trialtype'] == 'go_blank_cheat':
                is_rewarded.append(1)
                # if any(x > row['nogo_odor'][0] and x < row['nogo_odor'][1] + self.delay for x in row['licking']):
                if any(x > row['go_odor'][1] and x < row['go_odor'][1] + self.delay for x in row['licking']):
                    is_correct.append(1)
                else:
                    is_correct.append(0)

            elif row['trialtype'] == 'c_reward':
                is_rewarded.append(1)
                if any(x > row['control_odor'][0] and x < row['water_on'] for x in row['licking']):
                    is_correct.append(1)
                else:
                    is_correct.append(0)
            elif row['trialtype'] == 'c_omit':
                is_rewarded.append(0)
                if any(x > row['control_odor'][0] and x < row['control_odor'][1] + 2 * self.delay for x in
                       row['licking']):
                    is_correct.append(1)
                else:
                    is_correct.append(0)

            elif row['trialtype'] == 'background':
                is_rewarded.append(0)
                if any(x > 0 and x < row['trial_end'] for x in row['licking']):
                    is_correct.append(0)
                else:
                    is_correct.append(1)

            elif row['trialtype'] == 'go_omit':
                is_rewarded.append(0)
                if any(x > row['go_odor'][0] and x < row['go_odor'][1] + self.delay for x in row['licking']):
                    is_correct.append(1)
                else:
                    is_correct.append(0)
            elif row['trialtype'] in ['unpred_water', 'close_unpred_water', 'far_unpred_water']:
                is_rewarded.append(1)
                is_correct.append(np.nan)
        d = {'is_Correct': is_correct, 'is_Rewarded': is_rewarded, 'licked' : licked, 'watered' : watered, 'puffed' : puffed}
        new_df = pd.DataFrame(d)
        return new_df

    def create_trial_lick(self):
        for index, date in enumerate(self.all_days):
            value = self.df_trials[date]
            new_df = self.lick_stats(value)
            #new_df.insert(0, 'trialtype', value['trialtype'])
            new_df.insert(0, 'odormix', value['odormix'])

            self.df_trials_lick[date] = new_df
            print('lick stats done!')

    def lick_stats(self, df):

        lick_num = []
        lick_rate = []
        lick_latent_odor = []
        lick_latent_rew = []
        lick_duration = []
        lick_rate_window = []
        lick_rate_odor = []
        lick_rate_aftr = []
        # proportion_correct = []
        tol_interval = self.odor_on + self.delay + self.rew_after
        anti_window = self.odor_on + self.delay
        lick_window_list = []
        lick_odor_list = []
        lick_aftr_list = []

        for index, row in df.iterrows():
            if row['trialtype'] in ['go']:

                #lick_valid = [x for x in row['licking'] if x > row['go_odor'][0] and x < row['go_odor'][
                #    1] + self.delay]
                lick_valid = [x for x in row['licking'] if x > row['go_odor'][0] and x < row['go_odor'][
                    1] + tol_interval]  # valid licking: after odor on and 5.5 s after odor off
                # lickingrate for anticipitory period and after water period 3.5 respectively
                during_odor = [i for i in row['licking'] if
                        i > row['go_odor'][0] and i < row['go_odor'][1]]  
                during_window = [i for i in row['licking'] if
                        i > row['go_odor'][1] and i < (row['go_odor'][1] + self.delay)]  
                aftr = [i for i in row['licking'] if
                        i > row['water_on'] and i < row['water_off'] + self.rew_after]  # after water
                rate_odor = len(during_odor) / self.odor_on
                rate_window = len(during_window) / self.delay
                # num of licking
                num = len(lick_valid)
                if num != 0:
                    latency_odor = min(lick_valid) - row['go_odor'][0]  # first licking after odor delivery on
                else:
                    latency_odor = np.nan

                if row['trialtype'] in ['go']:
                    if len(aftr) != 0:
                        latency_rew = min(aftr) - row['water_on']  # first licking after odor delivery on
                    else:
                        latency_rew = self.rew_after
                else:
                    latency_rew = np.nan
                try:
                    duration = max(during_window) - min(during_window)  # anticipitory licking duration after odor presentation
                except:
                    duration = np.nan

            elif row['trialtype'] in ['no_go']:
                #lick_valid = [x for x in row['licking'] if x > row['go_odor'][0] and x < row['go_odor'][
                #    1] + self.delay]
                lick_valid = [x for x in row['licking'] if x > row['nogo_odor'][0] and x < row['nogo_odor'][
                    1] + tol_interval]  # valid licking: after odor on and 5.5 s after odor off
                # inter-licking interval for anticipitory period and after water period
                during_odor = [i for i in row['licking'] if
                        i > row['nogo_odor'][0] and i < row['nogo_odor'][1]]  
                during_window = [i for i in row['licking'] if
                        i > row['nogo_odor'][1] and i < row['nogo_odor'][1] + self.delay]  
                rate_odor = len(during_odor) / self.odor_on
                rate_window = len(during_window) / self.delay
                aftr = [i for i in row['licking'] if
                        i > row['water_on'] and i < row['water_off'] + self.rew_after]  # after water# num of licking
                num = len(lick_valid)
                if num != 0:
                    latency_odor = min(lick_valid) - row['nogo_odor'][0]  # first licking after odor delivery on
                else:
                    # latency_odor = tol_interval
                    latency_odor = np.nan
                latency_rew = np.nan
                try:
                    duration = max(during_window) - min(during_window)  # anticipitory licking duration after odor presentation
                except:
                    duration = np.nan



            lick_num.append(num)
            lick_rate.append(num / tol_interval)
            lick_latent_odor.append(latency_odor)
            lick_latent_rew.append(latency_rew)
            lick_duration.append(duration)
            lick_rate_window.append(rate_window)
            lick_rate_aftr.append(lick_rate_aftr)
            lick_rate_odor.append(rate_odor)
            lick_window_list.append(during_window)
            lick_odor_list.append(during_odor)
            lick_aftr_list.append(aftr)

        d = {'lick_num_whole_trial': lick_num,
             'lick_rate_whole_trial': lick_rate,
             'latency_to_odor': lick_latent_odor,
             'latency_to_rew': lick_latent_rew,
             'anti_duration': lick_duration,
             'rate_window': lick_rate_window,
             'rate_odor' : lick_rate_odor,
             'rate_after': lick_rate_aftr,
             'window_lick': lick_window_list,
             'odor_lick': lick_odor_list
             }
        new_df = pd.DataFrame(d)
        return new_df


def save_to_excel(dict_df, path, filename):
    try:
        os.makedirs(path)  # create the path first
    except FileExistsError:
        print('the path exist.')
    filename = path + '/{}.xlsx'.format(filename)

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')

    # Write each dataframe to a different worksheet. you could write different string like above if you want
    for key, value in dict_df.items():
        value.to_excel(writer, sheet_name=key)

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
    print('save to excel done!')


def pickle_dict(df, path, filename):
    try:
        os.makedirs(path)  # create the path first
    except FileExistsError:
        print('the path exist.')
    filename = path + '/{}.pickle'.format(filename)
    with open(filename, 'wb') as handle:
        pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print('save to pickle done!')


def load_pickleddata(filename):
    with open(filename, 'rb') as handle:
        df = pickle.load(handle)
    return df


# def sort_list(list1, list2):
#
#    zipped_pairs = zip(list2, list1)
#    zipped = list(zipped_pairs)
#
#    # Printing zipped list
#    print("Initial zipped list - ", str(zipped))
#
#    date_format = '%Y-%m-%d'
#    z = sorted(zipped,key=lambda date: datetime.strptime(date[1], date_format)) #
#
#    # printing result
#    print("final list - ", str(res))
#
#    return z


# %%
# %% main code
if __name__ == '__main__':

    is_save = True
    is_original = True  # when use clean data, change it to False

    # ********************
    load_path = 'F:/My Drive/behavior data/valence_task_2023_go_no_66'

    #mouse_names = ['males_last_51', 'males_pre_dark']
    #mouse_names =['ns_66_dark', 'females_last_51','females_last_54']
    mouse_names = ['females_pre_dark','males_pre_dark','females_pre_light', 'males_pre_light']
    #mouse_names = ['males_pre_dark','females_pre_dark']



    for mouse_name in mouse_names:
        cute = Mouse_data(mouse_name, filedir=load_path)
        cute.read_filename()
        # parse data
        cute.create_eventcode(original=is_original)
        cute.create_trials()
        cute.create_trial_iscorrect()
        cute.create_trial_lick()

        if is_save:
            # save data by pickle
            # ****************
            save_path = load_path + '/parsed_dataframe_pickle'

            filename = '{}_stats'.format(cute.mouse_id)
            pickle_dict(cute, save_path, filename)

            # save data to excel for just visualization (it'l all turn into string, so cannot be used later.)
            # ****************
            save_path_excel = load_path + '/parsed_dataframe_spreadsheet'

            save_to_excel(cute.df_trials_iscorrect, save_path_excel, '{}_trial_iscorrect'.format(cute.mouse_id))
            # save_to_excel(cute.df_trials_, save_path_excel, '{}_trial_lick_latency'.format(cute.mouse_id))
            save_to_excel(cute.df_trials_lick, save_path_excel, '{}_lick_stat'.format(cute.mouse_id))
            save_to_excel(cute.df_trials, save_path_excel, '{}_trials'.format(cute.mouse_id))
            save_to_excel(cute.df_eventcode, save_path_excel, '{}_eventcode'.format(cute.mouse_id))
        # %% main code




































