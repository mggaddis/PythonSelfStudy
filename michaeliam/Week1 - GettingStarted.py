
# coding: utf-8

# # Getting Started
# 
# - Write code to be executed in the Code cell. To run code, use Cell -> Run or 'Shift+Enter'
# - The Markdown cell is a rich text format that may be used to capture the code description 
# - To illustrate mathematical operations in a Markdown cell, use the LaTex notation - '$...$' for inline mathematics or '$$..$$' for displayed mathematics.
# - Shortcut Keyboard keys:
#     1. Shift+Enter - executes the current cell and displays output, then jumps to the next cell below
#     2. Ctrl+Enter - runs cell in place, that is it executes the current cell, displays output but cursor remains in   that cell
#     3. Atl+Enter - executes current cell, displays output and inserts a cell between the current cell and the cell with the output   
# 

# # Import Data

# In[1]:

import numpy as np
import pandas as pd

df=pd.read_csv('C:\Users\mimclean\Desktop\Python Training Data\Airbnb_train.csv')
print(df.head())


# # Hello, World!
# 

# In[1]:

print "Hello, World!"


# In[7]:

import requests
import pandas as pd
import StringIO


# df1=pd.read_csv('C:\Users\mimclean\Desktop\Python Training Data\Consumer_Complaints.csv')
# print (df1.head())

# In[6]:

df1=pd.read_csv('C:\Users\mimclean\Desktop\Python Training Data\Consumer_Complaints.csv')
print (df1.head())


# In[ ]:



