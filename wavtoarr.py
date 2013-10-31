import matplotlib.pyplot as plt
import wave
import numpy as np
from scikits.audiolab import Sndfile


a = wave.open('output.wav','r')
total_frames = a.getnframes()
f = Sndfile('output.wav','r')

fs = f.samplerate
nc = f.channels
enc = f.encoding
format_wave = f.format

data_float = f.read_frames(total_frames,dtype=np.float32)
data_after_ft = np.fft.fft2(data_float)


print fs,nc,enc,format_wave
print "\n \n"
print data_float
print data_float.size, data_float.shape
print "\n \n"
print data_after_ft

#plt.figure(1)
#plt.subplot(211)
#plt.plot(data_float,'k')

#plt.subplot(212)
#plt.plot(data_after_ft, 'r')
#plt.show()