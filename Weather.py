"""
Created on Tue Nov 6 2018
Python3 program to solve the weather challenge
@author: Kilian Geßele
"""

# important libraries
import pandas as pd

def read_table(filename):
    """Read the table data in a Pandas DataFrame"""
    return pd.read_csv(filename)

def analyse_table(table):
    """Find the day that has the smallest temperature variation"""
    
    #calculate the absolute temperature difference
    diff = abs(table['MxT'] - table['MnT'])
    
    #find the minimal value and  show the result
    print(table.loc[diff.idxmin()])

############### main program ###############
data = read_table('weather.csv')
analyse_table(data)
