import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import time
import OffsetEliminator as off



start = time.time()

filenames = ["E1vert.wav", "E2vert.wav","E3vert.wav"]
monos = [0]*6

monos[0] = "E1right.wav"
monos[1] = "E1right.wav"
monos[2] =  "E2right.wav"
monos[3]= "E2right.wav"
monos[4] = "E3right.wav"
monos[5] = "E3right.wav"

samplerate, dats = wavfile.read(monos[0])
samples = len(dats)



bigrights = np.zeros((3, samples))
bigrights[0,:] = dats
samplerate,bigrights[1,:] = wavfile.read(monos[2])
samplerate, bigrights[2,:] = wavfile.read(monos[4])

rights = np.zeros((3, 1000))

beg = 10000
end = 10000+100000
rights = bigrights[:,beg:end]
samples = end - beg




plt.figure()
ax1 = plt.subplot(311)
#ax1.plot(rights[0,48000:50000-290])
ax2 = plt.subplot(312)
#ax2.plot(rights[1,59000-290:61000])
ax3 = plt.subplot(313)
#ax3.plot(rights[2,53000:55000])


array1 = rights[0, 48000:50000]
array2 = rights[1,59000:61000]
array3 = rights[2,:]

corr12, offset12 = off.CorrScan(array1, array2, 500, 1800, 0)
print(corr12, offset12)

array1, array2 = off.OffsetArray(array1, array2, offset12)


ax1.plot(array1)
ax2.plot(array2)
plt.show()


avgrights = np.zeros((3,samples))

maxvals = np.zeros((3,1))

differences = np.zeros((3, samples))

variances = np.zeros((3,samples))

avgdiff = np.zeros((3,1))

rightavg = np.zeros((3,1))

freqdat = np.zeros((3,1))

for i in range(3):
    avgrights[i,:] = np.mean(rights[i,:])
    differences[i,:] = np.add(rights[i,:], -1*avgrights[i,:])
    avgdiff[i,0] = np.mean(differences[i,:])
    variances[i,:] = np.square(differences[i,:])
    variances[i,:] = np.sum(variances[i,:])
    maxvals[i,0] = np.max(rights[i,:])
    rightavg[i,0] = avgrights[i,0]

end = time.time()
print("Time elapsed = ")
print(end - start)

