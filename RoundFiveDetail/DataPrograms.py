'''This script is designed to provide programs to enable the quick analysis of a particular data set.
The set consists of 3 wav files. Making it robust and capable of editing sets with more than 3 wav files wouldn't be too challenging. 
 These wav files will be read with scipy module, then stored as rows in an array.
I need a program to take in this data array and compute a histogram for each of these, with variable bin numbers.

Also, I want to split the data into smaller pieces and compare the different quantuitites such as rms value and averages to that of the whole data set.
'''
import numpy as np
import scipy.io.wavfile as wavfile
import time
import matplotlib.pyplot as plt


'''Note: bins is an integer, proportional to the resolution of the histo.
binrange is a tuple that limits the values that the bins are created from
Data is an array with col = 288000 and row equal to 3
'''



def HistoPlotter(data, bins, binrange, titletext):
    array1 = data[0,:]
    array2 = data[1,:]
    array3 = data[2,:]
    histarray = np.zeros((3,bins))
    binvals = np.zeros((3, bins+1))
    for i in range(3):
        histarray[i,:], binvals[i,:] = np.histogram(data[i,:], bins,range = binrange)
	plt.figure()
	print(np.shape(histarray))
    print(np.shape(binvals[:,:-1]))
    ax1 = plt.subplot(311)
    ax2 = plt.subplot(312)
    ax3 = plt.subplot(313)
    ax1.scatter(binvals[0,:-1], histarray[0,:])
    ax2.scatter(binvals[1,:-1], histarray[1,:])
    ax3.scatter(binvals[2,:-1], histarray[2,:])
    ax1.annotate(str(np.mean(array1)), xy = (binrange[0], 60000))
    ax2.annotate(str(np.mean(array2)), xy = (binrange[0], 60000))
    ax3.annotate(str(np.mean(array3)), xy = (binrange[0], 60000))
    plt.show()
    return histarray, binvals


def AvgVals(data):
	row, width = np.shape(data)
	avgvals = np.zeros((row, 1))
	for i in range(row): 
		avgvals[i,0] = np.mean(data[i,:])
	return avgvals

#this fn takes in an array of data and a number of partitions
# it returns an array, the ith row are the values for the ith recording, the jth element is the average of that partition

def PartitionTest(data, partnum):
	row, width = np.shape(data)
	print(width)
	partwidth = width / partnum
	print(partwidth)	
	partvals = np.zeros((row, partnum)) #array of average vals, the ijth element is the average of the jth part of the ith data row	
	for i in range(row):
		for j in range(partnum):
			jlb = j*partwidth
			jub = (j+1)*partwidth
			currpartition = data[i, jlb:jub]
			partvals[i,j] = np.mean(currpartition)
	return partvals


	
