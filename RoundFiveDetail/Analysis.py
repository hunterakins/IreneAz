import DataPrograms as DP
import scipy.io.wavfile as wavfile
import numpy as np
import matplotlib.pyplot as plt

#Ideally what I have here is a function that takes in a list of sublists of filenames. Each of the filenames corresponds to a Left-Right recording. 
# I also take in a list of partition numbers.
# For each partition number in the list, I compute the average value of the subsets resulting from the partition and save them all in a big array.
# I also would like to plot histograms of each of the data sets values, in sets of three, and compare them to one another.


def FetchData(filenames): #this program just returns an array of data, the row corresponding the ith file
	numfiles = len(filenames)
	samplerate, E1 = wavfile.read(filenames[0])
	samples = np.size(E1)
	data = np.zeros((numfiles,samples))
	data[0,:] = E1
	for i in range(1, numfiles):
		samplerate, data[i,:] = wavfile.read(filenames[i])
	return data


# this will give me the array of averages of each partition
def PartitionAnalysis(filenames, partnumber, partfilename): 
	data = FetchData(filenames)
	partvals = DP.PartitionTest(data, partnumber) 
	np.savetxt(partfilename,partvals)
	return partvals

#for this one, I want to produce a plot for each set of "groupnum", for some number of partitions
# that is, for each recording set of [groupnum], I will partition each recording in the set and plot a histogram of it
# I think the easiest way is just to make a figure for each datum, with subplots for each of the partitions' histograms
 
def HistoPlot(filenames, imagepath, groupnum=3, partnum=3, binnumber=100, binrange=.10):
	data = FetchData(filenames)
	numrecordings, numsamples = np.shape(data)
	partitionsize = numsamples / partnum
	for i in range(numrecordings): #for each recording		
		f, axarr = plt.subplots(partnum, sharex=True)
		histarray = np.zeros((partnum, binnumber))
		currdats = data[i,:]
		axarr[0].set_title("Histogram for " + str(partnum) + " Contiguous Partitions of Recording " + str(i+1))
		for j in range(partnum):
			histvals, binedges = np.histogram(currdats[j*partitionsize:(j+1)*partitionsize], bins=binnumber, range=(-1*binrange, binrange)) 	
			axarr[j].scatter(binedges[0:-1], histvals)
		figure = plt.gcf()
		figure.set_size_inches(8, 6)
		plt.savefig(str(i) + imagepath, bbox_inches='tight')
	return






