import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import time


start = time.time()

filenames = ["E1vert.wav", "E2vert.wav","E3vert.wav"]
monos = [0]*6

monos[0] = "E1left.wav"
monos[1] = "E1right.wav"
monos[2] =  "E2left.wav"
monos[3]= "E2right.wav"
monos[4] = "E3left.wav"
monos[5] = "E3right.wav"

samplerate, E1 = wavfile.read(filenames[0])
samples = np.size(E1)

data = np.zeros((3,samples))
data[0,:] = E1
samplerate, data[1,:] = wavfile.read(filenames[1])
samplerate, data[2,:] = wavfile.read(filenames[2])

def ArraySort(array1):
	SortingHat = np.zeros((2,len(array1)))
	SortingHat[0,:] = np.argsort(array1)
	SortingHat[1, :] = np.sort(array1)
	return SortingHat




avgdata = np.zeros((3,samples))

maxvals = np.zeros((3,1))

differences = np.zeros((3, samples))

variances = np.zeros((3,samples))

avgdiff = np.zeros((3,1))


freqdat = np.zeros((3,1))


leftrightcorr = np.zeros((3,1)


for i in range(3):
    avgdata[i,:] = np.mean(data[i,:])
    differences[i,:] = np.add(data[i,:], -1*avgdata[i,:])
    avgdiff[i,0] = np.mean(differences[i,:])
    variances[i,:] = np.square(differences[i,:])
    variances[i,:] = np.sum(variances[i,:])
    maxvals[i,0] = np.max(data[i,:])

avgs = avgdata[:,0]
avgdiff = np.zeros((3,1))
print(maxvals)
print(variances[:,0])

SortingHat0 = ArraySort(data[0,:])
SortingHat1 = ArraySort(data[1,:])
SortingHat2= ArraySort(data[2,:])

sorteddata = np.zeros(np.shape(data))
sorteddata[0,:] = SortingHat0[1,:]
sorteddata[1,:] = SortingHat1[1,:]
sorteddata[2,:] = SortingHat2[1,:]

plt.plot()
plt.show()
refavgdata = np.zeros((3,samples))
for i in range(3):
    refavgdata[i,:] = np.mean(sorteddata[i,1000:-1000])
refavgs = refavgdata[:,0]

print(refavgs)

'''
plt.figure()
ax1 = plt.subplot(411)
ax1.plot(SortingHat0[1,-100:])
ax2 = plt.subplot(412)
ax2.plot(SortingHat1[1,-100:])
ax3 = plt.subplot(413)
ax3.plot(SortingHat2[1,-100:])
ax4 = plt.subplot(414)
domain = np.arange(0,100, 1)
ax4.scatter(domain, SortingHat0[0, -100:], color = 'r', marker = '^')
ax4.scatter(domain, SortingHat1[0, -100:], color = 'b', marker = 's')
ax4.scatter(domain, SortingHat2[0, -100:], color = 'g', marker = '*')

plt.show()
'''

end = time.time()

print("Time elasped = ")
print(end-start)
