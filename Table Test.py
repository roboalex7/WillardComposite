import pandas as pd
import numpy as np

#URLs that the table is grabbing from
kenpomURL = "file:///C:/Users/natha/Documents/Coding/WillardComposite/WebSamples/Kenpom.html#"
trankURL = "file:///C:/Users/natha/Documents/Coding/WillardComposite/WebSamples/Torvik_Last10.html#"

#Grabbing the table from the webpage and assigning header row
kenpomTable = pd.read_html(kenpomURL, header=17)
trankTable = pd.read_html(trankURL, header=1)

#Convert dataframe from above to csv file and exporting
for i, df in enumerate(kenpomTable):
    df.to_csv('kenpomTable.csv'.format(i))

for i, df in enumerate(trankTable):
    df.to_csv('trankTable.csv'.format(i))

#Import csv file as dataframe
kenpomDF = pd.read_csv('kenpomtable.csv', index_col=0)
trankDF = pd.read_csv('tranktable.csv')

kenpomDF = kenpomDF.drop([40,41,82,83,124,125,166,167,208,209,250,251,292,293,334,335])
trankDF = trankDF.drop([25,51,77,103,129,155,181,207,233,259,285,311,337,366])

#Sorta Dataframe by team alphabetically to align data sets
kenpomDF = kenpomDF.sort_values(by=['Team'])
trankDF = trankDF.sort_values(by=['Team'])

kenpomDF.to_csv('kenpomTableSorted.csv')
trankDF.to_csv('trankTableSorted.csv')

#Convert dataframe to arrays
rawKenPom = kenpomDF.to_numpy()
rawtrank = trankDF.to_numpy()

#Printing specific data
#Note some columns of data cannot be printed due to encoding error
x = 48
print(rawKenPom[x,1])
print(rawtrank[x,2])


input()