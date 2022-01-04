# Script Purpose: Display Python Pandas and Matplot Libraries - Week 3 Assignment
# Script Version: 1.0 September 9, 2021
# Script Author:  Tala Vahedi

# Script Revision History:
# Version 1.0 September 9, 2021, Python 3.x

# psuedo Constants
SCRIPT_NAME    = "Script: Display Python Pandas and Matplot Libraries"
SCRIPT_VERSION = "Version 1.0"
SCRIPT_AUTHOR  = "Author: Tala Vahedi"

# import 3rd Party Modules
from IPython.display import display
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
   # print Basic Script Information
   print()
   print(SCRIPT_NAME)
   print(SCRIPT_VERSION)
   print(SCRIPT_AUTHOR)
   print()

   # setting no display limits and a large width
   pd.set_option('display.max_rows', None)
   pd.set_option('display.max_columns', None)   
   pd.set_option('display.width', 2000)

   # reading the csv file with pandas
   data = pd.read_csv("IP-CONNECT.csv")

   # filtering out ipV6 Rows
   df = data[data.ipV6 == 0]

   # defining the columns in each 2D df
   cols = df.columns
   
   # iterating through each column within csv and pairing each data column with 
   # the associated IP Connection (excluding first column "connections") 
   for col in cols[1:]:
      # using filter pandas method to make "copy" of new df for each new column
      df2D = df.filter([cols[0],col], axis=1)
      # displaying results for a tabular view of the data
      display(df2D)
      # defining the columns within each newly created df
      columns = df2D.columns
      # providing the x and y axis to the matplotlib horizontal bar chart
      plt.barh(df2D[columns[0]], df2D[columns[1]], color='blue')
      # making the title the "column name + OBERSERVATION"
      plt.title(str(col) + ' OBSERVATIONS', fontsize=7)
      # making the label the y axis column name
      plt.ylabel(str(cols[0]), fontsize=5)
      # making the label the x axis column name
      plt.xlabel(str(col), fontsize=5)
      # showing the graph for a graphical view of the data
      plt.show()   