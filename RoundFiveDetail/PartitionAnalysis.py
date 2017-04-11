import numpy as np
from matplotlib import pyplot as plt 
from matplotlib import patches as mpatches

#this program should take in a text file of partition data
# I want this data as an array, with the ith row corresponding to the 
# values of the ith recordings partitions

Colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']


def GetData(filename):
	PartVals = np.loadtxt(filename)
	NumRecordings, NumParts = np.shape(PartVals)
	return PartVals, NumRecordings, NumParts

def MakeDomain(NumRecordings):
	return np.arange(1, NumRecordings+1, 1)

def Plotter(filename, title, xlabel, ylabel):
	PartVals, NumRecordings, NumParts = GetData(filename)
	domain = MakeDomain(NumRecordings)
	legendhandles = [0]*NumParts
	#for i in range(NumParts):
	for i in range(1):
		dats = PartVals[:,i]
		col = Colors[i]
		lab = "Partition Number " + str(i + 1)
		legendhandles[i] = mpatches.Patch(color = col,label = lab)
		plt.scatter(domain, dats, c=col)
	plt.legend(handles=legendhandles)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.title(title)
	plt.show()
	return

