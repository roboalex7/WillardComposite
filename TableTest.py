import pandas as pd
import numpy as np

#URLs that the table is grabbing from
kenpomURL = '.\WebSamples\Kenpom.html'
torvikLast10URL = '.\WebSamples\Torvik_Last10.html'
#For some reason relative paths wont pull the tables???? idk why
#torvikMainURL = '\WebSamples\Torvik_Main.html'
#torvikQuad1URL = '\WebSamples\Torvik_Quad1.html'
torvikMainURL = "file:///C:/Users/natha/Documents/Coding/WillardComposite/WebSamples/Torvik_Main.html#"
torvikQuad1URL = "file:///C:/Users/natha/Documents/Coding/WillardComposite/WebSamples/Torvik_Last10.html#"

#Grabbing the table from the webpage and assigning header row
kenpomTable = pd.read_html(kenpomURL, header=17)
torvikLast10Table = pd.read_html(torvikLast10URL, header=1)
torvikMainTable = pd.read_html(torvikMainURL, header=1)
torvikQuad1Table = pd.read_html(torvikQuad1URL,header=1)

#Convert dataframe from above to csv file and exporting
for i, df in enumerate(kenpomTable):
    df.to_csv('./CSVFiles/kenpomTable.csv'.format(i))

for i, df in enumerate(torvikLast10Table):
    df.to_csv('./CSVFiles/torvikLast10Table.csv'.format(i))

for i, df in enumerate(torvikMainTable):
    df.to_csv('./CSVFiles/torvikMainTable.csv'.format(i))

for i, df in enumerate(torvikQuad1Table):
    df.to_csv('./CSVFiles/torvikQuad1Table.csv'.format(i))


#Import csv file as dataframe
kenpomDF = pd.read_csv('./CSVFiles/kenpomTable.csv', index_col=0)
torvikLast10DF = pd.read_csv('./CSVFiles/torvikLast10Table.csv')
torvikMainDF = pd.read_csv('./CSVFiles/torvikMainTable.csv')
torvikQuad1DF = pd.read_csv('./CSVFiles/torvikQuad1Table.csv')

#Correcting for team name difference manually
torvikLast10DF.at[130, 'Team'] = "Charleston"
torvikMainDF.at[136, 'Team'] = "Charleston"
torvikQuad1DF.at[130, 'Team'] = "Charleston"
kenpomDF.at[199, 'Team'] =  "Fort Wayne"

#Dropping blank rows
kenpomDF.drop([40,41,82,83,124,125,166,167,208,209,250,251,292,293,334,335])
torvikLast10DF.drop([25,51,77,103,129,155,181,207,233,259,285,311,337,366])
torvikLast10DF.drop('Rec', axis=1)
torvikMainDF.drop([25,51,77,103,129,155,181,207,233,259,285,311,337,366])
torvikMainDF.drop('Rec', axis=1)
torvikQuad1DF.drop([25,51,77,103,129,155,181,207,233,259,285,311,337,366])
torvikQuad1DF.drop('Rec', axis=1)

#Sorta Dataframe by team alphabetically to align data sets
kenpomDF = kenpomDF.sort_values(by=['Team'])
torvikLast10DF = torvikLast10DF.sort_values(by=['Team'])
torvikMainDF = torvikMainDF.sort_values(by=['Team'])
torvikQuad1DF = torvikQuad1DF.sort_values(by=['Team'])

#Export sorted data to csv
kenpomDF.to_csv('./CSVFiles/kenpomTableSorted.csv')
torvikLast10DF.to_csv('./CSVFiles/torvikLast10TableSorted.csv')
torvikMainDF.to_csv('./CSVFiles/torvikMainTableSorted.csv')
torvikQuad1DF.to_csv('./CSVFiles/torvikQuad1TableSorted.csv')

#Convert dataframe to arrays
rawKenPom = kenpomDF.to_numpy()
rawTorvikLast10 = torvikLast10DF.to_numpy()
rawTorvikMain = torvikMainDF.to_numpy()
rawTorvikQuad1 = torvikQuad1DF.to_numpy()

#Printing testing of specific data
#Note some columns of data cannot be printed due to encoding error
x = 77
print(rawKenPom[x,1])
print(rawTorvikLast10[x,2])
print(rawTorvikMain[x,2])
print(rawTorvikQuad1[x,2])

#Start Willis Composite
rows = np.array([[0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1]])
compositeDF = pd.DataFrame({'Team':rows[:,0],'Seed':rows[:,1],'Region':rows[:,2],'Net':rows[:,3],'KenPom':rows[:,4],'AdjO':rows[:,5],'AdjD':rows[:,6],'Torvik':rows[:,7],'AEMLast10':rows[:,8],'Q1 W':rows[:,9],'Q2 L':rows[:,10],'WillisComposite':rows[:,11]})

#Export
print(compositeDF)
compositeDF.to_csv('.\CSVFiles\WillisComposite.csv')


input()