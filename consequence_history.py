# create list of trial types
# create list of lick/no lick (or reward/punish)
# bin the lists into chunks
# for every element in list, if it's a 6:3 for example, then determine if the elements n before it contained an airpuff
# then compare how many of the 6:3 that had vs  didn't have airpuff n before it resulted in licks
# start with just 1 before, iterate to 5 before, see  where strongest effect
# do for females vs males, light vs dark


pickled_data = os.path.join(path,'combined_all_clean_learning.pickle')
    pickled_data = load_pickleddata(pickled_data)
    pickled_data.index.duplicated()
    pickled_data = pickled_data[(pickled_data['trialtype'].isin(['no_go','go']))]
    pickled_data = pickled_data.groupby(['mouse_name','session','odormix'])[y].mean().reset_index()

# example of what it would look like
trial_type_list = [18, 72, 36, 18]
licked_list = [1, 1, 0, 1]
watered_list = [0, 1, 1, 0]
puffed_list = [1, 0, 0, 0]

one_eight_results = []
two_seven_results = []
# etc for the rest

#non-specific to odormix, but only for non easiest (1:8's)
def consequence_history(self, session):
    self.count_licked_airpuff = 0
self.count_no_lick_airpuff = 0
self.count_licked_nopuff = 0
self.count_no_lick_nopuff = 0
for i in trial_type_list:
    if trial_type_list[i]!= '18' or '81':
        if licked_list[i] == 1:
            if puffed_list[(i-3):[i-1]]== 1:
                self.count_licked_airpuff+1
            if puffed_list[(i-3):[i-1]]== 0:
                count_licked_nopuff+1
        if licked_list[i] == 0:
            if puffed_list[(i-3):[i-1]]== 1:
                count_no_lick_airpuff+1
            if puffed_list[(i-3):[i-1]]== 0:
                count_no_lick_nopuff+1
        print self.count_licked_airpuff
        print self.count_no_lick_airpuff
        print self.count_licked_nopuff
        print self.count_no_lick_nopuff

#specific to odormix 
for i in trial_type_list:
    if trial_type_list[i] == '18': 
