import numpy as np
import DataPrograms as DP
import Analysis as An
import namemaker as name
import PartitionAnalysis as PA

basicpath =  '/home/hunter/Documents/UCB/Irene/RoundFiveRecs/'
foldernames = ['RoundFive']
letternames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] 
numbers = ['1', '2', '3']
extension = 'vert.wav'

filenames = name.makefilenames(foldernames, letternames, numbers, basicpath, extension)[0]


An.HistoPlot(filenames, 'quadpart.png')

