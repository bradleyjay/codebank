from pandas import *  
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import *
%matplotlib inline

# import data
np.seterr(divide='ignore', invalid='ignore')      # numpy error handling
mydata = np.genfromtxt('temperatureThermocouples.csv', delimiter=',') # import

## Columns: 
#1: Iteration
#2: Broil Burner
#3: Bake Burner	
#4: Surface Temp	
#5: Electronics
#6: Door

i = mydata[:,1]
broil = mydata[:,2]
bake = mydatap[:,3]
surface = mydata[:,4]
elec = mydata[:,5]
door = mydata[:,6]

# Run/Configure params = rcParams
plt.rcParams["figure.figsize"] = (12,8)     # set figure size
plt.rcParams["font.size"]=20                # set font size

df = pd.DataFrame(data = mydata, columns = ['Iteration', 'Broil', 'Bake', 
'Surface', 'Electronics', 'Door'])
df