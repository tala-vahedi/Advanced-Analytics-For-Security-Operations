# Advanced-Analytics-For-Security-Operations

- The ping counter .py file uses the pingparsing library. The script creates a dictionary that maps website urls to an numeric identifier
this is necessary since NumPy arrays are not designed to hold strings, but rather only numbers. First, the script loops and performs ping operations against each website contained in the dictionary using the pingparsing library. Then, an empty list holds the resulting values from each website. Next, the [WEBSITE #, packetsTransmitted, packetsReceived, packetsLost, minRoundTrip, maxRoundTrip, avgRoundTrip] are appended. Finally, the list is converted to a numpy array.

- The networkSorter folder contains a python script that reads a json file with an array of network connection data and creates a pandas dataframe to display and sort the number of network observations. The script appends the sorted results to a text file in current directory.

- The IP-Connections folder contains a python script that reads a csv file into a panda DataFrame, then using Panda methods the connections are filtered for rows that contain ipv6 addresses, next using Panda methods specific columns are extracted creating new two dimensional Data Frames pairing each data column (TOTAL thru HOSTILE) with the associated IP Connection. Finally, the script creates a horizonal bar chart for each of the paired DataFrames for a graphical view of the data.
