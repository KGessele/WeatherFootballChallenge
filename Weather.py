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

############### main program ###############
data = read_table('weather.csv')
