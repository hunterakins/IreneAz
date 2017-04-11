import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import time
import warnings


start = time.time()

def Corr(array1, array2):
    return np.sqrt(np.sum(np.square(np.diff(array1, array2))))

def Compare(array1, array2, offset, size):
    return Corr(array1[:size], array2[offset:size+offset])

def CorrScan(array1, array2, offsetrange=5000, size=10000):
    N = len(array1)
    if offsetrange + size > N:
        print("Error, offsetrange and size are too large for the array samples")
        return
    offsets = np.arange(0, offsetrange, 1)
    print(offsets)
    for i in range(len(offsets)):
        tempoffset = offsets[i]
        tempcorr = Compare(array1, array2, tempoffset, size)
        if i == 0:
            corr = tempcorr
            optoffset =tempoffset
        if tempcorr < corr:
            corr = tempcorr
            optoffset = tempoffset
    return corr, offset
        

  







end = time.time()

print("total time elasped = ")
print(end-start)
