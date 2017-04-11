from namemaker import makefilenames
import struct
import math as m
import wave
import matplotlib.pyplot as plt 
import math
import numpy as np
import scipy.io.wavfile as wavfile
import time
from scipy.optimize import root, fsolve, fmin
from scipy import stats

start = time.time()


foldernames = ['2mm']
letternames = ['A', 'B', 'C', 'D']
numbers = ['1', '2', '3']
basicpath = 'C:\\Users\\admin\\Documents\\UCB\\Irene\\RoundFourRecs\\'
extension = 'vert.wav'

filenames = makefilenames(foldernames, letternames, numbers,basicpath,extension)
filenames = filenames[0]

number = 4
dataset = np.zeros((number,2880000))

for i in range(number):
	samplerate, data = wavfile.read(filenames[i])
	#print(np.size(data))
	dataset[i,:] = data


def rms(x):
	return np.sqrt(np.sum(np.square(x)))


def ArraySort(array1):
	SortingHat = np.zeros((2,len(array1)))
	SortingHat[0,:] = np.argsort(array1)
	SortingHat[1, :] = np.sort(array1)
	return SortingHat

def Differences(SortingHat):
 	return np.add(SortingHat[:, 1:], -1*SortingHat[:,:-1])

def ArrayOffset(array1, array2, offset, leftpoint = 0, samplesize = 1000):
	#takes in two large arrays, a1 and a2
	#takes a given samplesize oriented at leftpoint that is a subset of the original arrays, and offsets them by "offset"
	array1 = array1[leftpoint:leftpoint + samplesize]
	array2 = array2[leftpoint:leftpoint + samplesize]
	if offset > 0:
		array1 = array1[:-offset]
		array2 = array2	[offset:]
	if offset < 0:
		array1 = array1[-offset:]
		array2 = array2[:offset]
	return array1, array2 

def Corrtest(array1, array2):
	double = np.add(array1, array2)
	return rms(double)

def MatchMaker(array1, array2, threshold):
	# function intended to be used on small sub arrays of the real big arrays that I care about
	Sort1 = ArraySort(array1)
	Sort2 = ArraySort(array2)
	Diff1 = Differences(Sort1)
	Diff2 = Differences(Sort2)
	i = -1
	j = 0
	corr = Corrtest(array1, array2)
	offset = 0
	while (	i < len(array1)-2) and (j < len(array1)-2):
		i += 1	
		if rms(Diff1[:,i] - Diff2[:, j]) < threshold:
			ind1 = Sort1[0,i]
			ind2 = Sort2[0,j]
			offset = ind2 - ind1
			offset = int(offset)
			b1, b2 = ArrayOffset(array1, array2, offset)
			newcorr = Corrtest(b1, b2)
			if newcorr > corr:
				corr = newcorr
		if i == len(array1) - 2:
			j += 1;
			i = 0;
	return offset, corr


def LifeMatchMaker(a1, a2, threshold, leftpoint = 0, samplesize = 100, initialoffset = 0):
	inc = 1 # indicator of increased corr on iteration
	b1, b2 = ArrayOffset(a1, a2, leftpoint, samplesize, initialoffset)
	originalcorr = Corrtest(b1, b2)
	print(originalcorr)
	counter = 0
	offset = initialoffset
	while inc ==1:
		print("Offset")
		print(offset)			
		b1, b2 = ArrayOffset(a1, a2, leftpoint, samplesize, offset) # calculate new offset samples
		tempoffset, corr = MatchMaker(b1, b2, threshold) # run matchmaker to see if a better corr can be obtained
		print("corr")
		print(corr)
		if corr < originalcorr:
			inc = 0 # couldn't find an offset that more highly correlated the samples
		else:
			originalcorr = corr # we did better!
			offset = tempoffset
			leftpoint = offset - samplesize // 2 # move samples over to center around the new offset, then repeat the algorithm
		counter += 1
	print("Iterations = ")
	print(counter)
	return offset, corr


array1 = dataset[0,:]
array2 = dataset[1,:]

offset, corr = LifeMatchMaker(array1, array2, .1, leftpoint = 0, samplesize = 100, initialoffset = -400)


end = time.time()

plt.plot(a1, color = 'g')
plt.plot(a2, color = 'b')
plt.plot(b1, color = 'c')
plt.plot(b2, color = 'r')
plt.show()

print("Time elapsed: ")
print(end-start)
#print(OffsetMinimizer(a1, a2))





#wavfile.write('C:\\Users\\admin\\Documents\\UCB\\Irene\\RoundFourRecs\\Experiment.wav', samplerate, dataset)
