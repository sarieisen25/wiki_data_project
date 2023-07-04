import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Utilize read-made csv to replicate findings from paper

# with open('/Users/sarieisen/Downloads/Research/vital_articles_including_bot.csv', mode = 'r') as file:
#     data = csv.reader(file)
    
#for numbers in the 0-2 range, fit curves with that exponent
#pick out exponent with max R^2 value

# df = pd.read_csv('/Users/sarieisen/Downloads/Research/vital_articles_including_bot.csv')

# df_subset = df[df['n_user'] >= 10]
# df_subset = df_subset[df_subset['talk_page_size'] > 0]
# df_subset = df_subset[df_subset['n_revert'] > 0]
# df_subset = df_subset[df_subset['n_admin_activity'] > 0]
# print(len(df_subset))
# df_subset.to_csv('/Users/sarieisen/Downloads/Research/vital_articles_subset.csv')
#26014 pages left

df_subset = pd.read_csv('/Users/sarieisen/Downloads/Research/vital_articles_subset.csv')
def model_f(x,a,b):
    return a*(x**b)

def model_log(x,a,b):
    return (b*np.log(x))+a
    
def r_squared(ydata, xdata, param1, param2):
    residuals = ydata - model_log(xdata, param1, param2)
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((ydata-np.mean(ydata))**2)
    return 1-(ss_res/ss_tot)

contributors_talk_page, pcov1 = curve_fit(model_log, df_subset['n_user'], np.log(df_subset['talk_page_size']))
# print(contributors_talk_page)
# print(r_squared(df_subset['talk_page_size'], df_subset['n_user'], contributors_talk_page[0], contributors_talk_page[1]))
# plt.scatter(np.log(df_subset['n_user']), np.log(df_subset['talk_page_size']), s = 5)
# plt.plot(np.log(df_subset['n_user']), model_log(df_subset['n_user'], contributors_talk_page[0], contributors_talk_page[1]), c = 'orange')
# plt.plot(np.log(df_subset['n_user']), model_log(df_subset['n_user'], 0, 1), c = 'grey')
# plt.xlabel('# of contributors')
# plt.xscale('log')
# plt.ylabel('Talk page size (bytes)')
# plt.yscale('log')
# plt.text(8, 4, 'R^2 = 0.17')
# plt.text(3, 10, 'slope = '+str(np.round(contributors_talk_page[1], 2)))
# plt.show()

#change to log model
contributors_revert, pcov2 = curve_fit(model_log, df_subset['n_user'], np.log(df_subset['n_revert']))
# print(contributors_revert)
# print(r_squared(df_subset['n_revert'], df_subset['n_user'], contributors_revert[0], contributors_revert[1]))
# plt.plot(np.log(df_subset['n_user']), model_log(df_subset['n_user'], contributors_revert[0], contributors_revert[1]), c = 'orange')
# plt.plot(np.log(df_subset['n_user']), model_log(df_subset['n_user'], 0, 1), c = 'grey')
# plt.xlabel('log(# of contributors)')
# plt.xscale('log')
# plt.ylabel('log(# of reverts)')
# plt.yscale('log')
# plt.text(8, 4, 'R^2'+str(np.round(r_squared(df_subset['n_revert'], df_subset['n_user'], contributors_revert[0], contributors_revert[1]))))
# plt.text(3, 10, 'slope = '+str(np.round(contributors_revert[1], 2)))
# plt.show()

contributors_admin, pcov3 = curve_fit(model_log, df_subset['n_user'], np.log(df_subset['n_admin_activity']))
# print(contributors_admin)
print(r_squared(df_subset['n_admin_activity'], df_subset['n_user'], contributors_admin[0], contributors_admin[1]))
plt.plot(np.log(df_subset['n_user']), model_log(df_subset['n_user'], contributors_admin[0], contributors_admin[1]), c = 'orange')
plt.plot(np.log(df_subset['n_user']), model_log(df_subset['n_user'], 0, 1), c = 'grey')
plt.xlabel('log(# of contributors)')
# plt.xscale('log')
plt.ylabel('log(admin activity)')
# plt.yscale('log')
plt.text(8, 4, 'R^2'+str(np.round(r_squared(df_subset['n_admin_activity'], df_subset['n_user'], contributors_admin[0], contributors_admin[1]))))
plt.text(3, 10, 'slope = '+str(np.round(contributors_admin[1], 2)))
plt.show()

df_bot = df_subset[df_subset['n_bot_action']>0]
contributors_bot, pcov4 = curve_fit(model_log, df_bot['n_user'], np.log(df_bot['n_bot_action']))
# print(contributors_bot)
# print(r_squared(df_subset['n_bot_action'], df_subset['n_user'], contributors_bot[0], contributors_bot[1]))
# plt.plot(np.log(df_bot['n_user']), model_log(df_bot['n_user'], contributors_bot[0], contributors_bot[1]), c = 'orange')
# plt.plot(np.log(df_bot['n_user']), model_log(df_bot['n_user'], 0, 1), c = 'grey')
# plt.xlabel('log(# of contributors)')
# # plt.xscale('log')
# plt.ylabel('log(bot activity)')
# # plt.yscale('log')
# plt.text(8, 4, 'R^2'+str(np.round(r_squared(df_bot['n_bot_action'], df_bot['n_user'], contributors_bot[0], contributors_bot[1]))))
# plt.text(3, 8, 'slope = '+str(np.round(contributors_bot[1], 2)))
# plt.show()


#residuals
def resid(ydata, xdata, param1, param2):
    r = ydata / model_f(xdata, param1, param2)
    return np.log(r)

talk_page_resid = resid(df_subset['talk_page_size'], df_subset['n_user'], contributors_talk_page[0], contributors_talk_page[1])
df_subset['talk_page_resid'] = talk_page_resid

revert_resid = resid(df_subset['n_revert'], df_subset['n_user'], contributors_revert[0], contributors_revert[1])
df_subset['revert_resid'] = revert_resid

admin_resid = resid(df_subset['n_admin_activity'], df_subset['n_user'], contributors_admin[0], contributors_admin[1])
df_subset['admin_resid'] = admin_resid

bot_resid = resid(df_bot['n_bot_action'], df_bot['n_user'], contributors_bot[0], contributors_bot[1])
df_subset['bot_resid'] = bot_resid

# contributors_admin_num, pcov5 = curve_fit(model_log, df_subset['n_user'], np.log(df_subset['n_admin']))
# print(contributors_admin_num[1])

# contributors_bot_num, pcov6 = curve_fit(model_log, df_subset['n_user'], np.log(df_subset['n_bot']))
# print(contributors_bot_num[1])

# print(len(df_subset))
# df_subset.dropna()
# print(len(df_subset))
# print(df_subset.isnull().values.any().sum())
df_subset1 = df_subset.dropna()
# df_subset1.to_csv('/Users/sarieisen/Downloads/Research/vital_articels_subset_nona.csv')

# print(contributors_bot)
# print(r_squared(np.log(df_subset1['n_bot_action']), df_subset1['n_user'], contributors_bot[0], contributors_bot[1]))

# print(pcov4)
stdev = np.sqrt(pcov4[1][1])
# print(contributors_bot[1] + stdev)
# print(contributors_bot[1] - stdev)
print(str(contributors_bot[1])+': ['+str(contributors_bot[1]-stdev)+', '+str(contributors_bot[1]+stdev)+']')

print(df_subset[1:20])