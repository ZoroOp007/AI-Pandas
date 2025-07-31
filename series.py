import pandas as pd
import numpy as np

ser = pd.Series()

print(ser)

arr = np.array([1,"Hello",3,2,7,4])

ser = pd.Series(arr)
print(ser)

arr1 = np.array([1,3,2.1])

# Note : we can add any number to array given if the array is of type of Integer or float
print(arr1 + 1)

## Output : [2. ,4. ,3.1]
