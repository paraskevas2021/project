import csv
import pandas as pd
import matplotlib.pyplot as plt

#Diavazei to csv me onoma askisi1 apo to 1o erwtima
dataframe = pd.read_csv('askisi1.csv')

#Orizoume tis metavlites pou simmetexoun sto diagramma 
dataframe.plot(kind='scatter', x = 'Miles_Per_Galon', y = 'Miles')

#Emfanise to dataframe kai to diagramma 
print(dataframe.to_string)
plt.show()
