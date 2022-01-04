'''
CYBV-474
December 2020
Professor Hosmer

Panda Simple Dataframe Example
WK-2
Importing JSON

'''

# Standard Library Imports
    
# 3rd Party Library Imports
print("\nImporting a JSON")
print("Please wait, importing libraries")
import pandas as pd        # import Pandas 3rd party library

# Main Script Starts Here
if __name__ == '__main__':

    '''
    Example 2 - Creating a Panda Dataframe from a JSON File
    '''
    
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)   
    pd.set_option('display.width', 2000)
    
    
    print('\n')
    print('='*80)
    testDF = pd.read_json (r'IP-EX.json')
    print(testDF)
    
    print('\n')
    print('='*80)
    testDF = pd.read_json (r'MAC-EX.json')
    print(testDF.transpose())    
    

