

"""
Calculates rms values of wav files and stores them in a numpy array.
First generates the filenames of original files.
Includes commented out code that converted the original files from 24-bit to 32-bit. 
Generates "newfilenames", the names of the 32-bit sound files.
Computes rms values of the 32-bit sound files with rmscalc and getdata.

Want to add in code to compare frame by 
"""

import struct
import math as m
import wave
import matplotlib.pyplot as plt 
import math
import numpy as np
import scipy.io.wavfile as wavfile
#import soundfile as sf 
import time

"""

Most of the commented out code pertained to processing a specific set of recordings, which had to be converted from 24 to 32 bit and had specific names...
filenames = [0]* 32
surnames = ['left', 'right', 'vert', 'lat'] #suffixes of filenames

for i in range(1,32):
	sublist = [0] * 4
	for j in range(4):
		sublist[j] = str(i) + surnames[j] + '.wav'
	filenames[i] = sublist
"""



""" 
del(filenames[26])
del(filenames[21])
del(filenames[17])
""" 
"""
def changebitdepth(filename):
	# changes bitdepth from 24 to 32
	data, samplerate = sf.read(filename)
	#length = np.shape(data)[0]
	#np.reshape(data, (length, 1))
	newfilename = 'new' + filename
	sf.write(newfilename, data, samplerate, subtype = 'FLOAT')
	return
"""

# this section of code creates a list of the file names of the converted 32 bit wav files
""" commenting out this part because my new files are already 32 bit 
newfilenames = [0]*len(filenames)
for i in range(1, len(filenames)):
	newfilenames[i] = [0]*4
	for j in range(4):
		newfilenames[i][j] = 'new' + filenames[i][j]
"""
# this section of code will call changebitdepth on all the wav files in filenames, thus creating the new 32-bit files referenced in newfilenames
# Since I ran the program once, I've created all the files and so I comment out this section of code
#for i in range(1, len(filenames)):
#	for j in range(4):
#		changebitdepth(filenames[i][j])

	

def getdata(filename):
	rate, data = wavfile.read(filename)
	return data


def rmscalc(data):
	squarevals = np.square(data)
	meansq = np.mean(squarevals);
	return m.sqrt(meansq)

def avgcalc(data):
    return np.mean(data);

start = time.time()

#take in list of lists of filenames (as 32 bit mono .wav files) and a filename for the outputted textfile of rms values 
# each element in the list of filenames is a list of four files, the left channel, right channel, vertical and lateral mix of a given stereo file
# the format of rmsvals is an n by 6 array, the first column is the rms value of the left channel, the second is that of the right,
# the third is that of the vertical mix, and the fourth is that of the lateral mix , the fifth is the ratio left/right, and the sixth is the ratio lat/vert 


def avgcalculator(filenames, textfilename): 
    numfiles = len(filenames);
    horz = len(filenames[0]);
    print("numfiles is ")
    print(numfiles)
    print("Number of subfiles is ")
    print(horz)
    avgvals = np.zeros((numfiles, horz))
    for i in range(numfiles):
        for j in range(horz):
            filename = filenames[i][j]
            data = getdata(filename)
            avgval = avgcalc(data)
            avgvals[(i-1,j)] = avgval 
    np.savetxt(textfilename, avgvals)
    return data, avgvals 


end = time.time()
print("Total time elapsed = ")
print(end-start)

