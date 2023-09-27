import numpy as np
import sounddevice as sd
import scipy.signal as ss
from collections import deque


FS = 44100
BLOCK_SIZE = 1024
CHANNELS = 1
LOWCUT = 100 # Hz
PLOT_LENGTH = 10

rms_data = deque([0 for i in range(PLOT_LENGTH)], maxlen=PLOT_LENGTH)
x = np.arange(len(rms_data))

b, a = ss.butter(5, LOWCUT, fs=FS, btype='low')

def callback(indata, frames, time, status):
    filtered = ss.lfilter(b, a, indata)
    rms_data.append(np.sqrt(np.sum(filtered * filtered) / len(filtered)))

with sd.InputStream(callback=callback, channels=CHANNELS, samplerate=FS):
    print('lIskauhdasd')
    sd.sleep(10000)