# Advanced-Analytics-For-Security-Operations

The ping counter .py file uses the pingparsing library. The script creates a dictionary that maps website urls to an numeric identifier
this is necessary since NumPy arrays are not designed to hold strings, but rather only numbers. First, the script loops and performs ping operations against each website contained in the dictionary using the pingparsing library. Then, an empty list holds the resulting values from each website. Next, the [WEBSITE #, packetsTransmitted, packetsReceived, packetsLost, minRoundTrip, maxRoundTrip, avgRoundTrip] are appended. Finally, the list is converted to a numpy array.
