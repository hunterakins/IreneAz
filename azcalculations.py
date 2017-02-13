from avgcalculator import avgcalculator, getdata
from getmonos import makemonos
import struct
import math as m
import wave
import matplotlib.pyplot as plt 
import math
import numpy as np
import scipy.io.wavfile as wavfile
import time
''' How to use this script:
Define azrecordings as a list of filenames that you want to analyze.
Define azfilename as the name of the textfile that  will contain all your data.

'''
start = time.time()


azrecordings = ["C:\Users\irene\Anaconda\AlignmentRecordings\RoundThree\\2mm.wav", "C:\Users\irene\Anaconda\AlignmentRecordings\RoundThree\\2p5mm.wav", "C:\Users\irene\Anaconda\AlignmentRecordings\RoundThree\\3mm.wav", "C:\Users\irene\Anaconda\AlignmentRecordings\RoundThree\\3p5mm.wav", "C:\Users\irene\Anaconda\AlignmentRecordings\RoundThree\\4mm.wav", "C:\Users\irene\Anaconda\AlignmentRecordings\RoundThree\\2mm.wav"];
azfilename = "azrmsvalsthree"

data = getdata("C:\Users\irene\Anaconda\AlignmentRecordings\RoundThree\\2mm.wav")

print(np.size(data))

plt.plot(data)
plt.show()

numsamples = len(azrecordings);

filenames = [0]*numsamples;

for i in range(numsamples):
    filenames[i] = makemonos(azrecordings[i])
    
data, avgvals = avgcalculator(filenames, azfilename)

latmixavg = [0]*5
for i in range(5):
    latmixavg[i] = avgvals[i][3];

print(latmixavg)



'''
def getratios(numpyarray):
    rows, cols = np.shape(numpyarray)
    ratios = np.zeros((rows, 2))
    for i in np.arange(rows):
        ratios[i,0] = numpyarray[i,1] / numpyarray[i,0] #right channel / left channel
        ratios[i,1] = numpyarray[i, 3] / numpyarray[i, 2] # vertical over lateral mix
    return ratios    


plt.figure(1)    
fig, ax = plt.subplots()


ratios = getratios(avgvals) 

barwidth = .1 #how much big are the bars (the ticks are a unit apart)   (I need to have enough space for each of the four recordings (left, right, vert, lat)
opacity = 0.8   

horz,vert = np.shape(ratios)
index = np.arange(numsamples) #one tick per recording...

ax.set_ylabel('Rms value (units?)')
ax.set_xlabel('Az Pos') 
ax.set_xticks(index + 2*barwidth)


colors = ['r','b','y','g','v']

for i in range(4):
    ax.bar(index + i*barwidth, avgvals[:, i], barwidth, color = colors[i])

plt.figure(2)
fig, axt = plt.subplots()
barwidth = .35
opacity = 0.8
axt.set_ylabel('Ratio')
axt.set_xlabel('Az pos')
axt.set_xticks(index + barwidth)
axt.set_xticklabels(('2mm', '2p5mm', '3mm', '3p5mm', '4mm'))


for i in range(2):
    axt.bar(index + i*barwidth, ratios[:, i], barwidth, color = colors[i])
    
end = time.time()

print("Total time elapsed = ")
print(end - start)
print(" seconds.")
plt.show()
'''