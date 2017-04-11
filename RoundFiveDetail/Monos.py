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

samplerate, dats = wavfile.read(monos[0])
samples = len(dats)

lefts = np.zeros((3, samples))
lefts[0,:] = dats
samplerate, lefts[1,:] = wavfile.read(monos[2])
samplerate, lefts[2,:] = wavfile.read(monos[4])

plt.figure()
ax1 = plt.subplot(311)
ax1.plot(lefts[0,:])
ax2 = plt.subplot(312)
ax2.plot(lefts[1,:])
ax3 = plt.subplot(313)
ax3.plot(lefts[2,:])

#plt.show()
avglefts = np.zeros((3,samples))

maxvals = np.zeros((3,1))

differences = np.zeros((3, samples))

variances = np.zeros((3,samples))

avgdiff = np.zeros((3,1))

leftavg = np.zeros((3,1))

freqdat = np.zeros((3,1))

for i in range(3):
    avglefts[i,:] = np.mean(lefts[i,:])
    differences[i,:] = np.add(lefts[i,:], -1*avglefts[i,:])
    avgdiff[i,0] = np.mean(differences[i,:])
    variances[i,:] = np.square(differences[i,:])
    variances[i,:] = np.sum(variances[i,:])
    maxvals[i,0] = np.max(lefts[i,:])
    leftavg[i,0] = avglefts[i,0]

print(leftavg)
end = time.time()
print("Time elapsed = ")
print(end - start)
