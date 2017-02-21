import numpy as np
from matplotlib import pyplot as plt 

'''
Sample = np.loadtxt('avg5mm.txt', delimiter = ',')
SampleLeftChannel = Sample[:,0]
SampleRightChannel = Sample[:, 1]
SampleLatMix = Sample[:, 2]
SampleVertMix = Sample[:, 3]
'''


plt.figure(1)
plt.title("Plots of average and rms values of scan")
plt.xlabel('Recording Number')

i = 0

def SampleAnalysis(filename):
	Sample = np.loadtxt(filename, delimiter = ',')
	SampleLeftChannel = Sample[:,0]
	SampleRightChannel = Sample[:, 1]
	SampleLatMix = Sample[:, 2]
	SampleVertMix = Sample[:, 3]
	maxval = np.max(Sample)		
	numsamps, nummixes = np.shape(Sample)
	'''
	plt.subplot(4, 3, i+1)
	plt.plot(SampleLeftChannel, color = 'r')
	plt.plot(SampleVertMix, color = 'g')
	plt.plot(SampleLatMix, color = 'b')		
	plt.plot(SampleRightChannel, color = 'c')
	plt.title(filename[:-4] + " Values	")
	'''
	return Sample, SampleLeftChannel, SampleRightChannel, SampleLatMix, SampleVertMix


def GetAverages(sample, trialnum):
	#goal is to average the three vals corresponding to a single angular setting
	numsamps, nummixes = np.shape(sample)
	Averages = np.zeros(((numsamps // trialnum), nummixes)) 
	for i in range(numsamps // trialnum):
		temp = sample[i*trialnum:trialnum*(i+1) , :]
		Averages[(i, 0)] = np.sum(temp[:,0]) / trialnum
		Averages[(i, 1)] = np.sum(temp[:,1]) / trialnum
		Averages[(i, 2)] = np.sum(temp[:,2]) / trialnum
		Averages[(i, 3)] = np.sum(temp[:,3]) / trialnum
	return Averages	

Sample, SampleLeftChannel, SampleRightChannel, SampleLatMix, SampleVertMix = SampleAnalysis('avg5mm.txt')
#print(Sample)
print(Sample)
print(GetAverages(Sample, 3))



filenames = ['avg5mm.txt', 'avg4mm.txt', 'avg3mm.txt', 'avg2mm.txt','avg1mm.txt', 'rms5mm.txt', 'rms4mm.txt', 'rms3mm.txt', 'rms2mm.txt','rms1mm.txt']

for i in range(len(filenames)):
	Sample, SampleLeftChannel, SampleRightChannel, SampleLatMix, SampleVertMix = SampleAnalysis(filenames[i])
	Averages = GetAverages(Sample, 3)
	domain = np.linspace(1, 4, 4)
	np.savetxt('averages' + filenames[i], Averages, delimiter = ',', newline = '\n')
	for j in range(1):
		plt.plot(domain, Averages[:,j], color='b')
		plt.plot(domain, Averages[:, j + 1], color = 'g')
		plt.title(filenames[i])
		plt.xlabel('Recording number')
		plt.show()
