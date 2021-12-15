'''
Script Purpose: Recording ping results from CyberApolis websites
Script Version: 2.0 August 25, 2021
Script Author:  Tala Vahedi

Script Revision History:
Version 1.0 August 23, 2021, Python 3.x
Version 2.0 August 25, Updates and Simplification
'''

# Import 3rd Party Modules
import pingparsing  # import the pingparsing library
import numpy as np     # import numpy 3rd party library

# Psuedo Constants
SCRIPT_NAME    = "Script: Create a Numpy Array of Ping Results"
SCRIPT_VERSION = "Version 2.0"
SCRIPT_AUTHOR  = "Author: Tala Vahedi"


if __name__ == '__main__':
   # Print Basic Script Information
   print()
   print(SCRIPT_NAME)
   print(SCRIPT_VERSION)
   print(SCRIPT_AUTHOR)
   print()

   # create a parser object
   pingParser = pingparsing.PingParsing()    
   # create a transmitter object
   txObj = pingparsing.PingTransmitter()     

   # dict of websites to ping
   WEBSITES = {
      'capost.com'    : 1, 
      'cageneral.com' : 2,
      'cadepot.com'   : 3
      }

   # step 4.1 create a loop to perform ping operations against WEBSITES
   npList = [] # empty list to hold values of all wesbites ping results
   for url, id in WEBSITES.items(): # iterating through each websites in WEBSITES
      txObj.destination = url # identifying website
      print("Processing:\t" + url)
      pingResults = txObj.ping()  #pinging each website
      pingResultDict = pingParser.parse(pingResults).as_dict()  # storing ping results in dict  
      
      # Step 4.2 Create an empty list to hold the resulting values from each WEBSITE
      emptyList = [] # empty list to hold values of each individual wesbites ping results
      emptyList.append(id) # adding the WEBSITE # of each website
      for key, value in pingResultDict.items(): # iterating through each value in dict
         # Step 4.3 appending [WEBSITE #, packetsTransmitted, packetsReceived, packetsLost, minRoundTrip, maxRoundTrip, avgRoundTrip]
         if key == "packet_transmit" or key == "packet_receive" or key == "packet_loss_count"\
         or key == "rtt_min" or key == "rtt_max" or key == "rtt_avg":
               emptyList.append(value) 
      print(emptyList)
      # Appending each websites list into master list with all website ping results
      npList.append(emptyList)

   # step 4 convert the list to a numpy array
   npArray = np.array(npList)
   # Step 5 print out (display) the resulting numpy array
   print("Numpy Array: \n", npArray)
   # output results into txt file
   print(npArray, file=open("numpyResults.txt", "a"))