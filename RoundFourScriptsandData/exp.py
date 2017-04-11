from namemaker import makefilenames
import struct
import math as m
import wave
import matplotlib.pyplot as plt 
import math
import numpy as np
import scipy.io.wavfile as wavfile
import time

file = 'C:\\Users\\admin\\Documents\\UCB\\Irene\\RoundFour\\2mm.wav'


foldernames = ['2mm']
letternames = ['A', 'B', 'C', 'D']
numbers = ['1', '2', '3']
basicpath = 'C:\\Users\\admin\\Documents\\UCB\\Irene\\RoundFour\\'
extension = 'vert.wav'

filenames = makefilenames(foldernames, letternames, numbers,basicpath,extension)
print(filenames)