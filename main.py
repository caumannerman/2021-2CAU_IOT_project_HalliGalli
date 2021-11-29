import librosa
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

audio_file1 = 'train1.wav'
data1, samplerate1 = librosa.load(audio_file1)
times1 = np.arange(len(data1))/float(samplerate1)
#sd.play(data,samplerate)
plt.plot(times1, data1)
plt.xlim(times1[0], times1[-1])
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()