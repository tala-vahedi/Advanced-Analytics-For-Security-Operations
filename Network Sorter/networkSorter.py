'''
Tala Vahedi
August 23, 2021
Week Two Assignment - Display Panda DataFrame sorted by the highest number of observations
'''

'''
Script Purpose: Display Panda DataFrame sorted by the highest number of observations - Week 2 Assignment
Script Version: 1.0 September 3, 2021
Script Author:  Tala Vahedi, University of Arizona

Script Revision History:
Version 1.0 September 3, 2021, Python 3.x
'''

# Psuedo Constants
SCRIPT_NAME    = "Script: Display Panda DataFrame sorted by the highest number of observations"
SCRIPT_VERSION = "Version 1.0"
SCRIPT_AUTHOR  = "Author: Tala Vahedi"

# Import 3rd Party Modules
import pandas as pd # importing pandas as pd

if __name__ == '__main__':
   # Print Basic Script Information
   print()
   print(SCRIPT_NAME)
   print(SCRIPT_VERSION)
   print(SCRIPT_AUTHOR)
   print()

   pd.set_option('display.max_rows', None)
   pd.set_option('display.max_columns', None)   
   pd.set_option('display.width', 2000)

   jsonFile = 'CONNECTIONS-JSON.json'
   print("Reading '", jsonFile,  "' file, please wait...")

   # Creating a Panda DataFrame from the JSON File variable "jsonFile"
   connDF = pd.read_json(jsonFile, orient='index')

   print("Sorting results by highest number of observations, please wait...", "\n")
   # sorting values of "observed" in descending order
   connDF = connDF.sort_values(['Observed'], ascending=False)
   connDF.set_index(['Observed'], inplace=True)
   # removing column titled "record", per the screenshot provided in lecture
   del connDF['Record']
   print("Sorted Results:")
   # printing out the first 10 lines of the pandas DataFrame in terminal 
   print(connDF.head(10))
   # adding the full output into a text file in directory
   print(connDF, file=open("PandaDataFrame.txt", "a"))