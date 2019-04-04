import pandas as pd
import numpy as np

#URLs that the table is grabbing from
kenpomURL = '.\WebSamples\Kenpom.html'
torvikLast10URL = '.\WebSamples\Torvik_Last10.html'
torvikMainURL = '.\WebSamples\Torvik_Main.html'
#quadURL = "https://herosports.com/ncaa-tournament/college-basketball-net-rankings-ahah"
quadURL = "http://warrennolan.com/basketball/2019/stats-records-most-q1-wins"
netRankingURL = './WebSamples/NCAA_NET.html'

#Grabbing the table from the webpage and assigning header row
kenpomTable = pd.read_html(kenpomURL, header=17)
torvikLast10Table = pd.read_html(torvikLast10URL, header=1)
torvikMainTable = pd.read_html(torvikMainURL, header=1)
quadTable = pd.read_html(quadURL)
netRankingTable = pd.read_html(netRankingURL)

#Convert dataframe from above to csv file and exporting
for i, df in enumerate(kenpomTable):
    df.to_csv('./CSVFiles/kenpomTable.csv'.format(i))
for i, df in enumerate(torvikLast10Table):
    df.to_csv('./CSVFiles/torvikLast10Table.csv'.format(i))
for i, df in enumerate(torvikMainTable):
    df.to_csv('./CSVFiles/torvikMainTable.csv'.format(i))
for i, df in enumerate(quadTable):
    df.to_csv('./CSVFiles/quadTable.csv'.format(i))
for i, df in enumerate(netRankingTable):
    df.to_csv('./CSVFiles/netRankingTable.csv'.format(i))


#Import csv file as dataframe
kenpomDF = pd.read_csv('./CSVFiles/kenpomTable.csv', index_col=0)
torvikLast10DF = pd.read_csv('./CSVFiles/torvikLast10Table.csv')
torvikMainDF = pd.read_csv('./CSVFiles/torvikMainTable.csv')
quadDF = pd.read_csv('./CSVFiles/quadTable.csv')
netRankingDF = pd.read_csv('./CSVFiles/netRankingTable.csv')


#Correcting for team name difference manually
torvikLast10DF.at[130, 'Team'] = "Charleston"
torvikMainDF.at[136, 'Team'] = "Charleston"
kenpomDF.at[199, 'Team'] =  "Fort Wayne"
netRankingDF.at[269,'School'] = "Texas A&M Corpus Chris"
quadDF.at[146, 'Most Quadrant 1 Wins.2'] = "Cal St. Fullerton"
quadDF.at[147,'Most Quadrant 1 Wins.2'] = "Cal St. Northridge"
quadDF.at[145, 'Most Quadrant 1 Wins.2'] = "Cal St. Bakersfield"
quadDF.at[149, 'Most Quadrant 1 Wins.2'] = "Cal Baptist"
quadDF.at[95, 'Most Quadrant 1 Wins.2'] = "Florida Atlantic"
quadDF.at[184, 'Most Quadrant 1 Wins.2'] = "Florida Gulf Coast"
quadDF.at[274, 'Most Quadrant 1 Wins.2'] = "Fort Wayne"
quadDF.at[191, 'Most Quadrant 1 Wins.2'] = "Grambling St."
quadDF.at[325, 'Most Quadrant 1 Wins.2'] = "Illinois Chicago"
quadDF.at[218, 'Most Quadrant 1 Wins.2'] = "LIU Brooklyn"
quadDF.at[326, 'Most Quadrant 1 Wins.2'] = "Louisiana Monroe"
quadDF.at[121, 'Most Quadrant 1 Wins.2'] = "Massachusetts"
quadDF.at[37, 'Most Quadrant 1 Wins.2'] = "Mississippi"
quadDF.at[266, 'Most Quadrant 1 Wins.2'] = "Nebraska Omaha"
quadDF.at[282, 'Most Quadrant 1 Wins.2'] = "St. Bonaventure"
quadDF.at[283, 'Most Quadrant 1 Wins.2'] = "St. Francis NY"
quadDF.at[284, 'Most Quadrant 1 Wins.2'] = "St. Francis PA"
quadDF.at[34, 'Most Quadrant 1 Wins.2'] = "St. John's"
quadDF.at[298, 'Most Quadrant 1 Wins.2'] = "USC Upstate"
quadDF.at[313, 'Most Quadrant 1 Wins.2'] = "Tennessee Martin"

#Dropping blank rows
quadDF = quadDF.drop([0])
kenpomDF = kenpomDF.drop([40,41,82,83,124,125,166,167,208,209,250,251,292,293,334,335])
torvikLast10DF = torvikLast10DF.drop([25,51,77,103,129,155,181,207,233,259,285,311,337,366])
torvikMainDF = torvikMainDF.drop([25,51,77,103,129,155,181,207,233,259,285,311,337,366])

#Sorta Dataframe by team alphabetically to align data sets
kenpomDF = kenpomDF.sort_values(by=['Team'])
torvikLast10DF = torvikLast10DF.sort_values(by=['Team'])
torvikMainDF = torvikMainDF.sort_values(by=['Team'])
quadDF = quadDF.sort_values(by=['Most Quadrant 1 Wins.2'])
netRankingDF = netRankingDF.sort_values(by=['School'])

#Export sorted data to csv
kenpomDF.to_csv('./CSVFiles/kenpomTableSorted.csv')
torvikLast10DF.to_csv('./CSVFiles/torvikLast10TableSorted.csv')
torvikMainDF.to_csv('./CSVFiles/torvikMainTableSorted.csv')
quadDF.to_csv('./CSVFiles/quadTableSorted.csv')
netRankingDF.to_csv('./CSVFiles/netRankingTableSorted.csv')

#Convert dataframe to arrays
kenPomArray = kenpomDF.to_numpy()
torvikLast10Array = torvikLast10DF.to_numpy()
torvikMainArray = torvikMainDF.to_numpy()
quadArray = quadDF.to_numpy()
netRankingArray = netRankingDF.to_numpy()

#Printing testing of specific data
#Note some columns of data cannot be printed due to encoding error
x = 120
print(kenPomArray[x,1])
print(torvikLast10Array[x,2])
print(torvikMainArray[x,2])
print(quadArray[x,3])
print(netRankingArray[x,3])

#Start Willis Composite [row,coloumn]
rows = np.array([[kenPomArray[0,1],0,0,0,kenPomArray[0,0],kenPomArray[0,6],kenPomArray[0,8],torvikMainArray[0,1],torvikLast10Array[0,1],0,0],
				[kenPomArray[1,1],1,1,1,kenPomArray[1,0],kenPomArray[1,6],kenPomArray[1,8],torvikMainArray[1,1],torvikLast10Array[1,1],1,1]])
compositeDF = pd.DataFrame({'Team':rows[:,0],'Seed':rows[:,1],'Region':rows[:,2],'Net':rows[:,3],'KenPom':rows[:,4],'AdjO':rows[:,5],'AdjD':rows[:,6],'Torvik':rows[:,7],'AEMLast10':rows[:,8],'Q1 W':rows[:,9],'WillisComposite':rows[:,10]})

#Export
print(compositeDF)
compositeDF.to_csv('.\CSVFiles\WillisComposite.csv')


input()