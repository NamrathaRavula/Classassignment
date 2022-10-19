#Question 1
from numpy import random;
import numpy as np;
a=random.randint(20, size=(15))
b = a.reshape(3,5)
print(b)
new_a = np.where(b == [
   [i]
   for i in np.amax(b, axis = 1)
], 0 ,b)
print(new_a)



#Question 2
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:/Users/sruja/OneDrive/Desktop/python-codes/data.csv")
data.head()
data.describe()
data = data.fillna(data.mean())
print(data[['Maxpulse','Calories']].agg(['min','max','mean','count']))
print(data[(data.Calories < 1000) & (data.Calories > 500)]) 
print(data[ (data.Calories>500) & (data.Pulse < 100)])
df_modified = pd.DataFrame(data, columns = ['Duration', 'pulse', 'Calories'])
print (df_modified.head())
del data["Maxpulse"]
print(data.head)
data['Calories'] = data['Calories'].astype("int")
print(data['Calories'].dtypes)
print(data.plot.scatter(x ='Duration', y= 'Calories'))
plt.show()


#Question 3
import matplotlib.pyplot as plt
import numpy as np

y = np.array([22.2, 17.6, 8.8, 8, 7.7, 6.7])
mylabels = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
myexplode = [0.2, 0, 0, 0,0,0]
plt.pie(y,labels=mylabels, explode = myexplode,autopct='%1.1f%%')
plt.show()

