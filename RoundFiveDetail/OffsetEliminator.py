import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import time
import warnings


start = time.time()

def Corr(array1, array2):
    return np.sqrt(np.sum(np.square(array1- array2)))

def Compare(array1, array2, offset, size, start):
    return Corr(array1[start:start+size], array2[start+offset:start+size+offset])

def CorrScan(array1, array2, offsetrange=5000, size=10000, start = 0):
    N = len(array1)    
    if offsetrange + size + start > N:
        print("Error, offsetrange and size are too large for the array samples")
        return
    if len(array1) != len(array2):
        print("Warning: arrays are of different size...")
    offsets = np.arange(0, offsetrange, 1)
    for i in range(len(offsets)):
        tempoffset = offsets[i]
        tempcorr = Compare(array1, array2, tempoffset, size, start)
        if i == 0:
            corr = tempcorr
            optoffset =tempoffset
        if tempcorr < corr:
            corr = tempcorr
            optoffset = tempoffset
    return corr, optoffset
        
def OffsetArray(array1, array2, offset):
    array1 = array1[:-offset]
    array2 = array2[offset:]
    return array1, array2



  







end = time.time()

print("total time elasped = ")
print(end-start)
