import numpy as np
import matplotlib.pyplot as plt
from namemaker import makefilenames
import scipy.io.wavfile as wavfile


foldernames = ['RoundFive']
letternames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
numbers = ['1', '2', '3']
basicpath = 'C:\\Users\\admin\\Documents\\UCB\\Irene\\RoundFiveRecs\\'
extension = 'vert.wav'


filenames = makefilenames(foldernames, letternames, numbers,basicpath,extension)[0]

numfiles = len(filenames)
samplerate, data = wavfile.read(filenames[0])
data = np.zeros((numfiles, np.size(data)))
avgdata = np.zeros((numfiles, 1))


for i in range(numfiles):
    samplerate, data[i,:] = wavfile.read(filenames[i])
    avgdata[i,0] = np.mean(data[i,:])

avgdata = avgdata.reshape(10,3)

domain = np.arange(1,11, 1)

for i in range(3):
    plt.scatter(domain, avgdata[:, i])

plt.show()
