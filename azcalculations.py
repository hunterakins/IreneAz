from avgcalculator import avgcalculator, getdata, AnalyzeData
from namemaker import makefilenames
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
Call the 
'''
start = time.time()


foldernames = ['5mm', '4mm', '3mm', '2mm', '1mm']
letternames = ['A', 'B', 'C', 'D']
numbers = ['1', '2', '3']
basicpath = 'C:\\Users\\admin\\Documents\\UCB\\Irene\\RoundFour\\'
extension = '.wav'

filenames = makefilenames(foldernames, letternames, numbers,basicpath,extension)

for i in range(len(filenames)):
	azrecordings = filenames[i];
	azfilename = foldernames[i] + '.txt'
	avgvals, rmsvals = AnalyzeData(azrecordings, azfilename)
	print("For ")
	print(foldernames[i])
	print(", the filenames are ")
	print(filenames[i])
	print(" and ")
	print("avgvals are ")
	print(avgvals)
	print(" and rmsvals are ")
	print(rmsvals)


end = time.time() 

print('Total time elapsed: ')
print(end - start)

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