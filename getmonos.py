""" Takes in a single stereo wave file and creates four mono tracks: 
Say the original file is called sample.wav ;
It creates sampleleft.wav, sampleright.wav, samplevert.wav, samplelat.wav in the folder of the original file ;
"""

#from rmscalc import changebitdepth 
import struct
import math as m
import wave
import matplotlib.pyplot as plt 
import math
import numpy as np
import scipy.io.wavfile as wavfile
import time

def createfilenames(filename):
    filename = filename[0:-4]
    filenames = [filename + "left.wav", filename + "right.wav", filename + "vert.wav", filename + "lat.wav"]
    return filenames
    
    
def vertmix(leftchannel, rightchannel):
	return np.subtract(leftchannel, rightchannel)

def latmix(leftchannel, rightchannel):
	return np.add(leftchanel, rightchannel);


def makemonos(filename):
    samplerate, data = wavfile.read(filename)
    filenames = createfilenames(filename);
    wavfile.write(filenames[0], samplerate, data[:, 0]) #write left channel to new file
    wavfile.write(filenames[1], samplerate, data[:, 1]) #write right channel
    wavfile.write(filenames[2], samplerate, np.subtract(data[:, 0], data[:, 1])) #lateral mix
    wavfile.write(filenames[3], samplerate, np.add(data[:, 0], data[:, 1])) #vertical mix   
    return filenames
"""
azrecordings = ["2mm.wav", "2point5mm.wav", "3mm.wav", "3point5.wav", "4mm.wav"];

now = time.time()
for i in range(len(azrecordings)):
    makemonos(azrecordings[i])
    
later = time.time()

print("It took ")
print(later - now)
print(" seconds")
    """