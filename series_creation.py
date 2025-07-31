import pandas as pd
import numpy as np


ser = pd.Series([1,4,2,6,4,2])

print(ser)

ser = pd.Series(np.linspace(1,20,12), index = [x for x in "abcdefghijkl"])

print(ser)

## From  dictionary 

dict1 = {"Name" : ["Badal" , "Monica" , " Surya"],
         "Age" : [23 , 19 , 45]
         }

ser = pd.Series(dict1)

print(ser)

print(ser.loc["Name"])

# Here I have cleared my confusion about loc and iloc 
# So Basically iloc is used to locate the integer valued index
# While the loc function is used to locate the non integer valued index

ser = pd.Series(np.arange(1,20,3), index = [x for x in "abcdefghijklmn"])

print(ser)