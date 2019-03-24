import pandas as pd
import numpy as np

#URLs that the table is grabbing from
kenpomURL = "https://kenpom.com/"
trankURL = "file:///C:/Users/natha/Documents/Coding/WillardComposite/WebSamples/Torvik_Last10.html#"

#Grabbing the table from the webpage and assigning header row
kenpomTable = pd.read_html(kenpomURL, header=17)
trankTable = pd.read_html(trankURL, header=1)

#Convert dataframe from above to csv file and exporting
for i, df in enumerate(kenpomTable):
    df.to_csv('kenpomtable.csv'.format(i))

for i, df in enumerate(trankTable):
    df.to_csv('tranktable.csv'.format(i))

#Import csv file as dataframe
kenpomDF = pd.read_csv('kenpomtable.csv', index_col=0)
trankDF = pd.read_csv('tranktable.csv')

#Convert dataframe to arrays
rawKenPom = kenpomDF.to_numpy()
rawtrank = trankDF.to_numpy()

#Testing array addition
array = rawKenPom[0,1] + ' ' + rawtrank[0,3]

#Printing specific data
#Note some columns of data cannot be printed due to encoding error
print(rawKenPom[0,1])
print(rawtrank[0,3])
print(array)


input()