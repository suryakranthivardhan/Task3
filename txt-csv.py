import pandas as pd
dataframe1 = pd.read_csv("C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\second year\\onlinefile.txt",delimiter = '.')
df = dataframe1.to_csv('C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\second year\\Filename.csv',index = None)
