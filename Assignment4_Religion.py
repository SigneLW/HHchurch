
# coding: utf-8

# # Assignment 4
#
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
#
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **religious events or traditions** (see below) for the region of **Hamburg, Hamburg, Germany**, or **Germany** more broadly.
#
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Hamburg, Hamburg, Germany** to Ann Arbor, USA. In that case at least one source file must be about **Hamburg, Hamburg, Germany**.
#
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
#
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
#
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
#
# Here are the assignment instructions:
#
#  * State the region and the domain category that your data sets are about (e.g., **Hamburg, Hamburg, Germany** and **religious events or traditions**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
#
# What do we mean by **religious events or traditions**?  For this category you might consider calendar events, demographic data about religion in the region and neighboring regions, participation in religious events, or how religious events relate to political events, social movements, or historical events.
#
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
#
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[147]:

import pandas as pd
from pylab import *

# Load data
HHdata = pd.read_csv('HHKirche.csv', encoding = "ISO-8859-1")
DEdata = pd.read_csv('DEKirche.csv', encoding = "ISO-8859-1")

# Transform data
df = pd.merge(left = HHdata, right = DEdata, on='Jahr', how='inner')
df.columns = ['Year','HH_Population','HH_Kath_abs','HH_Kath_rel','HH_Ev_abs','HH_Ev_rel','DE_Kath_rel','DE_Ev_rel','DE_christ_rel']
df_to_0 = pd.DataFrame()

# Make data readable and make data relative to first data point
for column in df:
    if (isinstance(df[column][0], str)):
        df[column] = df[column].replace({'%':'',',':'.',' ':''}, regex=True).str.strip()
        df[column] = pd.to_numeric(df[column])
        def rel_change(x, start_value):
            return (x-start_value)
        df_to_0[column] = df[column].apply(rel_change, args=(df[column][0],))

# Prepare for plotting
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

df_to_0 = df_to_0.drop(['HH_Population','HH_Kath_abs','HH_Ev_abs','DE_christ_rel'], 1)
df_to_0 = df_to_0.drop(15)
df = df.drop(15)
df_to_0['Year'] = df['Year']
print(df_to_0)
plt.style.use('seaborn-whitegrid')
matplotlib.rcParams.update({'font.size': 8})

# Create Plots
plt.figure();
plt.suptitle('Religious Affiliations in Hamburg and Germany');
#### PLOT 1 ####
ax1 = plt.subplot(2,2,1)
plt.plot(df['Year'],df['HH_Kath_rel'],'-',color='orange', linewidth=1)
plt.plot(df['Year'],df['DE_Kath_rel'],'--',color='orange', linewidth=1)
plt.plot(df['Year'],df['HH_Ev_rel'],'-',color='purple', linewidth=1)
plt.plot(df['Year'],df['DE_Ev_rel'],'--',color='purple', linewidth=1)
# Shrink current axis's height by 10% on the bottom
#box = ax1.get_position()
#ax1.set_position([box.x0, box.y0 + box.height * 0.2,
#                 box.width, box.height * 0.8])
ax1.set_ylim([0, 40])
ax1.set_xlim([2001,2015])
ax1.set_xticks([2002,2006,2010,2014])
plt.title('Total',fontsize=10)
plt.ylabel('% of population')

#### PLOT 2 ####
ax2 = plt.subplot(2,2, 2)
plt.plot(df['Year'],df_to_0['HH_Kath_rel'],'y-',color='orange', linewidth=1)
plt.plot(df['Year'],df_to_0['DE_Kath_rel'],'y--',color='orange', linewidth=1)
plt.plot(df['Year'],df_to_0['HH_Ev_rel'],'-',color='purple', linewidth=1)
plt.plot(df['Year'],df_to_0['DE_Ev_rel'],'--',color='purple', linewidth=1)
legendtext=['Catholics in Hamburg','Catholics in Germany','Protestants in Hamburg','Protestants in Germany']
plt.title('Relative to 2001',fontsize=10)
plt.ylabel('% change since 2001')

# Shrink current axis's height by 10% on the bottom
#box = ax2.get_position()
#ax2.set_position([box.x0, box.y0 + box.height * 0.2,
#                 box.width, box.height * 0.8])

# Put a legend below current axis
ax2.legend(legendtext,loc='upper center', bbox_to_anchor=(-0.15, -0.2),
          fancybox=True, shadow=True, ncol=2)
ax2.set_xlim([2001,2015])
ax2.set_xticks([2002,2006,2010,2014]);
#ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")
plt.show()
