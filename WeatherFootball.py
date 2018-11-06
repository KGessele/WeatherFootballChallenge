"""
Created on Tue Nov  6 2018
Python3 program to solve the weather and football challenge
@author: Kilian Geßele
"""

# important libraries
import pandas as pd

def read_table(filename):
    """Read the table data in a Pandas DataFrame"""
    return pd.read_csv(filename)

def show_result(result,column_out):
    """Print the resulting value and the corresponding column name"""
    print(column_out + ': ' + str(result[column_out]))

def analyse_table(table, column_min, column_sub, column_out):
    """
    Find the table row that contains the minimal value of a column difference
    table -- table data [Pandas DataFrame]
    column_min -- column name of the minuends [string]
    column_sub -- column name of the subtrahends [string]
    column_out -- column name of the output value [string]
    """
    
    #calculate the absolute column difference
    diff = abs(table[column_min] - table[column_sub])
    
    #find the minimal value of the difference and  show the result
    show_result(table.loc[diff.idxmin()], column_out)


############### main program ###############
data = read_table('weather.csv')
analyse_table(data, 'MxT', 'MnT', 'Day')

data = read_table('football.csv')
analyse_table(data, 'Goals', 'Goals Allowed', 'Team')
