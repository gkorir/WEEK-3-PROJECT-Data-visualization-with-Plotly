# -*- coding: utf-8 -*-
"""Copy of Week 3 project-Data visualization with plotly-Geoffrey Korir.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xrZ2vnW-4PbSaumkFLSc287P2GiFaYb2

# Week 3 assignment On Data Visualisation with Plotly

1).**Defining the Question**

a) **Defining the data analytis question.**

Insights of the evolution of the mobile network across Africa

b) **Defining the Metric for Success.**

1.What is a high-level diagnosis of the sector you’re studying?

2.What are the key facts people need to know about this sector?

Trend of mobile network vs services being offered across Africa.

3.What are key trends that are worth noting?

How fixed broadband subscriptions has grown over the years.

How Mobile cellular subscrptions has grown over the years.

Interdependence on growth between fixed broadband and cellular subsciption.

C.**Recommendation** .

The sector should invest more on fixed broadband technology since its growing faster yoy as compaired to mobile celular subscription which is on a steady decline.

d) **Understanding the context.**

Mobile network as technology has grown over the years in terms of the service offered by the telco company.

e) **Recording the Experimental Designs.**

1).Obtain a Data.
2).Prepare the Data.
a. Get acquainted with all the columns on your data set.
b. Pay close attention to the units of measure used.
c. Imagine how these metrics would work together to help you make your business recommendation.

3).**Analyze the Data**.
4).Create a visualization using Plotly.
a. Use whichever graphs you think will be the most prudent in visualizing the answers to the project’s questions.
b. Label the axes and data points sparingly and correctly.
c. Upload the visualization to Chart Studio.

5).**Report the Data.**
a. In a 500 to 800 words article, answer the research question.
b. Upload the article to Medium and include all relevant visualizations in your article (at least 3).
c. Your article needs to be a balanced and objective account, with insights mostly coming from your datasets.

# Pre-requisite libraries
"""

# Import pandas for data manipulation
import pandas as pd

# Import numpy for scientific computations
import numpy as np

# Import plotly library for data visualisation
# ---
# `plotly.express` contains plotly.py's core functionality
# ----
#
import plotly.express as px
#install.packages(dplyr)

"""# Obtaining data set"""

# obtaining data set for mobile evolution
mobile_evolution_df = pd.read_csv('https://bit.ly/MobileDataset')
mobile_evolution_df.head()

"""# Get acquainted with all the columns on your data set"""

#getting to know the data types of the clumns of our data set
mobile_evolution_df.dtypes

# Checking the shapeof our data set.
mobile_evolution_df.shape

"""# Data preparation"""

#dispalying the columns names

mobile_evolution_df.columns = mobile_evolution_df.columns.str.lower().str.strip().str.replace(" ", "_").str.replace("(", "").str.replace(")", "")
mobile_evolution_df.columns = ['series_name', 'series_code', 'country_name', 'country_code', '1995', '1996', '1997', '1998','1999' ,'2000',' 2001',' 2002',' 2003',' 2004',' 2005',' 2006',' 2007 ','2008 ','2009 ','2010 ','2011 ','2012 ','2013',' 2014','2015', '2016']
mobile_evolution_df.columns = mobile_evolution_df.columns.str.strip()
mobile_evolution_df.columns

"""# Data Cleaning"""

# Check missing values
mobile_evolution_df.isnull().sum()

"""No missing values found"""

#Checking duplicates

mobile_evolution_df.duplicated().sum()

"""No duplicate values found"""

# Examining our cleaned data set

mobile_evolution_df.sample(2)

# we then round off our values to 2dp
mobile_check = mobile_evolution_df.round(decimals= 2)
mobile_check.head()

# converting columns to int

year_columns = mobile_evolution_df.columns[4:]
mobile_evolution_df[year_columns] = mobile_evolution_df[year_columns].apply(lambda x: x.replace('..', '0')).astype(float).astype('int')
year_columns

# we then drop column '2016' since it has all zeros values
mobile_evolution_df.drop(columns=['2016'], inplace=True)
mobile_evolution_df.sample(5)

#getting unique values using column 'series_name'

mobile_evolution_df['series_name'].unique()
mobile_evolution_df.head()

#getting columns with statistical values 

stats_columns = list(mobile_evolution_df.columns[1:])
mobile_stats_df = mobile_evolution_df.groupby('series_name', as_index=False).sum()
mobile_stats_df.head()

# getting transposed values

mobile_stats_df = mobile_stats_df.transpose().reset_index()
mobile_stats_df

new_columns = mobile_stats_df.iloc[0]
new_columns

mobile_stats_df.columns = new_columns
mobile_stats_df.drop(index=0, inplace=True)
mobile_stats_df

new_column = mobile_stats_df.columns[1:]
mobile_stats_df = pd.melt(mobile_stats_df, id_vars=['series_name'], value_vars=new_column)
mobile_stats_df

"""# Demonstrating solution and Plotly visualization"""

#Ploting a line graph

fig = px.line(
    mobile_stats_df,
    x = "series_name",
    y = "value",
    color = 0
)
fig.update_layout(
    title = {
        'text': "Major Trends Of mobile evolution Over the Years",
        'x': 0.5,
        'font_size' : 15,
        'xanchor': "center",
        'yanchor': "auto"
    },
xaxis_title_text = "Years",
yaxis_title_text = "Users",
)

#Plot display

fig.show()

yearly_columns = list(mobile_evolution_df.columns[2:])
country_trend_df = pd.melt(mobile_evolution_df, id_vars=['series_name', 'country_name'], value_vars=yearly_columns)
cellular_df = country_trend_df[country_trend_df['series_name']=='Fixed broadband subscriptions']

fig2 = px.line(
    cellular_df,
    x = "variable",
    y = "value",
    color = "country_name"
)


# Tweak and Label
fig2.update_layout(
    title = {
        'text': "Fixed Broadband Per Country Over the Years",
        'x': 0.5,
        'font_size' : 15,
        'xanchor': "auto",
        'yanchor': "auto"
    },
    xaxis_title_text = "Years",
    yaxis_title_text = "Fixed Broadband Users",
)

# Display

fig2.show()

mobile_cell_df = country_trend_df[country_trend_df['series_name']=='Mobile cellular subscriptions']
fig3 = px.line(
    mobile_cell_df,
    x = "variable",
    y = "value",
    color = "country_name"
)

# Tweak and Label

fig3.update_layout(
    title = {
        'text': "Cellular Subscriptions per Country Over Years ",
        'x': 0.5,
        'font_size' : 15,
        'xanchor': "center",
        'yanchor': "top"
    },
    xaxis_title_text = "Years",
    yaxis_title_text = "No of Cellular Subscrioptions",
)

# Display

fig3.show()

"""# Chart Studio for exporting to Medium"""

# install chart studio

!pip install chart_studio

# import chart studio

import chart_studio

username = 'gkorir' # your username
api_key = 'QUzcXeu3FIL0HEGBmN44' # your api key - go to profile > settings > regenerate key
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

import chart_studio.plotly as py
py.plot(fig, filename = 'My Visusalisation', auto_open=True)

"""'https://plotly.com/~gkorir/1/'"""

py.plot(fig2, filename = 'My Visusalisation2', auto_open=True)

"""'https://plotly.com/~gkorir/5/'"""

py.plot(fig3, filename = 'My Visusalisation3', auto_open=True)

"""https://plotly.com/~gkorir/9/"""