import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

df_subset = pd.read_csv('/Users/sarieisen/Downloads/Research/vital_articles_subset.csv')

def model_f(x,a,b):
    return a*(x**b)

categories = np.sort(df_subset.category_1.unique())
scaling_exp = pd.DataFrame()
talk_page = []
revert = []
admin = []
bot = []

print(df_subset[df_subset['category_1'] == 'Technology']['talk_page_size'])
for cat in categories:
    df_cat = df_subset[df_subset['category_1'] == cat]
    popt, pcov = curve_fit(model_f, df_cat['n_user'], df_cat['talk_page_size'])
    print(cat.replace('_', ' '), popt[1])
    talk_page.append(popt[1])

scaling_exp['talk page'] = talk_page
print(scaling_exp['talk page'])

# def model_linlog(x,a,b):
#     return (b*x)+a

# print('\n Talk page \n')
# for cat in categories:
#     df_cat = df_subset[df_subset['category_1'] == cat]
#     popt, pcov = curve_fit(model_linlog, np.log(df_cat['n_user']), np.log(df_cat['talk_page_size']))
#     print(cat.replace('_', ' '), round(popt[1], 3))

# print('\n \n Revert \n')
# for cat in categories:
#     df_cat = df_subset[df_subset['category_1'] == cat]
#     popt, pcov = curve_fit(model_linlog, np.log(df_cat['n_user']), np.log(df_cat['n_revert']))
#     print(cat.replace('_', ' '), round(popt[1], 3))

# print('\n \n Admin \n')
# for cat in categories:
#     df_cat = df_subset[df_subset['category_1'] == cat]
#     popt, pcov = curve_fit(model_linlog, np.log(df_cat['n_user']), np.log(df_cat['n_admin_activity']))
    # print(cat.replace('_', ' '), round(popt[1], 3))

#are there NA values in bots col?
#throws error 'array must not contain infs or NaNs'
# print('\n \n Bots \n')
# for cat in categories:
#     df_cat = df_subset[df_subset['category_1'] == cat]
#     df_cat.dropna()
#     popt, pcov = curve_fit(model_linlog, np.log(df_cat['n_user']), np.log(df_cat['n_bot_action']))
#     print(cat.replace('_', ' '), round(popt[1], 3))

# df_cat = df_subset.dropna()

# for cat in categories:
#     df_cat = df_subset[df_subset['category_1'] == cat]
#     popt, pcov = curve_fit(model_linlog, np.log(df_cat['n_user']), np.log(df_cat['n_bot_action']))
#     print(cat.replace('_', ' '), round(popt[1], 3))

#bar graph of avg number of editors by category of article
# mean_users = []
# for cat in categories:
#     mean = np.mean(df_subset[df_subset['category_1'] == cat]['n_user'])
#     mean_users.append(mean)

# print(mean_users)
# plt.bar(categories, mean_users)
# plt.show()