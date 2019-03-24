import pandas as pd
import numpy as np

kenpomURL = "https://kenpom.com/"
trankURL = "file:///C:/Users/natha/Documents/Coding/WillardComposite/WebSamples/Torvik_Last10.html#"

kenpomTable = pd.read_html(kenpomURL, header=17)
trankTable = pd.read_html(trankURL, header=1)

for i, df in enumerate(kenpomTable):
    df.to_csv('kenpomtable.csv'.format(i))

for i, df in enumerate(trankTable):
    df.to_csv('tranktable.csv'.format(i))

kenpomDF = pd.read_csv('kenpomtable.csv', index_col=0)
trankDF = pd.read_csv('tranktable.csv')

rawKenPom = kenpomDF.to_numpy()
rawtrank = trankDF.to_numpy()

array = rawKenPom[0,1] + ' ' + rawtrank[0,3]

print(rawKenPom[0,1])
print(rawtrank[0,3])
print(array)


input()