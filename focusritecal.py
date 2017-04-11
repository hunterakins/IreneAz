from getmonos import makemonos
from rmscalc import rmscalculator
import struct
import math as m
import wave
import matplotlib.pyplot as plt 
import math
import numpy as np
import scipy.io.wavfile as wavfile
import time 

start = time.time()
filenames = ["C:\Users\irene\Anaconda\AlignmentRecordings\GainTuning\usegaintest0F.wav", "C:\Users\irene\Anaconda\AlignmentRecordings\GainTuning\usegaintest1F.wav"]
monofilenames = [0]*len(filenames);
for i in range(len(filenames)):
    monofilenames[i] = makemonos(filenames[i])
    
    
data, rmsvals = rmscalculator(monofilenames, "fcalvals") 

print(rmsvals)

print(monofilenames)

end = time.time()

print("Time elapsed = ")

print(end - start)  