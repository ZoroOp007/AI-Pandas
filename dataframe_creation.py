"""
general syntax of creating a dataframe 

        pandas.DataFrame(data, indexes, columns)

"""

## Empty DataFrame
import pandas as pd

df = pd.DataFrame()

print(df)

## from list
l = ["Badal" , "is", "the", "best"]

df = pd.DataFrame(l , columns=["String"])

print(df)

## Note for list of lists, each new list becomes a row of the dataframe.

ll = [["Arjun" ,"Shyam" ,"Karan" ,"Ramu"],["Policeman","Judge","NSG","Servant"]]

df = pd.DataFrame(ll)

print(df)

## from dictionary
dict1 = {"Name" : ["Ram","Shyam","Gopal","Ramu","Tinku"], "Age" : [23,15,34,23,43]}

df = pd.DataFrame(dict1)

print(df)



## using the zip function 
list1 = ["Apple" , "Oranges", "PineApple", ]

list2 = [40 , 60 , 20]

new_list = list(zip(list1,list2))

print( new_list)

## So we can overcome the problem faced in the above list by zipping the two separate list

