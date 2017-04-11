import numpy as np
import DataPrograms as DP
import Analysis as An
import namemaker as name
import PartitionAnalysis as PA
import matplotlib.pyplot as plt


basicpath =  '/home/hunter/Documents/UCB/Irene/RoundFiveRecs/'
foldernames = ['RoundFive']
letternames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] 
numbers = ['1', '2', '3']
extension = 'vert.wav'

filenames = name.makefilenames(foldernames, letternames, numbers, basicpath, extension)[0]


PartVals, NumRecordings, NumParts = PA.GetData('fulltest.txt')

domain = PA.MakeDomain(NumRecordings)

plt.scatter(domain, PartVals[:,0])

plt.show()
#An.HistoPlot(filenames, 'quinpart.png', partnum=5)

