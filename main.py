import librosa
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment

'''
audio_file1 = './audio/myaudio(0).aac'
data1, samplerate1 = librosa.load('./audio/my.m4a')
print(data1.shape, samplerate1)
times1 = np.arange(len(data1))/float(samplerate1)
#sd.play(data,samplerate)
plt.plot(times1, data1)
plt.xlim(times1[0], times1[-1])
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()
'''
"""
song = AudioSegment.from_('audio/myaudio (1).aac')
print(song)
"""
stereo_audio = AudioSegment.from_file(
    './audio/상단소음_상단먼저침.aac',
    format="aac")

# Calling the split_to_mono method
# on the stereo audio file
mono_audios = stereo_audio.split_to_mono()

# Exporting/Saving the two mono
# audio files present at index 0(left)
# and index 1(right) of list returned
# by split_to_mono method

mono_left = mono_audios[0].export(
    "./audio/mono_left.wav",
    format="wav")
mono_right = mono_audios[1].export(
    "./audio/mono_right.wav",
    format="wav")

print(len(mono_audios))
print(len(mono_audios[0]))
print(len(mono_audios[0][0]))



data1, samplerate1 = librosa.load('./audio/mono_left.wav')
print(data1.shape, samplerate1)
times1 = np.arange(len(data1))/float(samplerate1)
#sd.play(data,samplerate)
plt.plot(times1, data1)
plt.xlim(times1[0], times1[-1])
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()

D = librosa.stft(data1)
magnitude, phase = librosa.magphase(D)


data1, samplerate1 = librosa.load('./audio/mono_right.wav')
print(data1.shape, samplerate1)
times1 = np.arange(len(data1))/float(samplerate1)
#sd.play(data,samplerate)
plt.plot(times1, data1)
plt.xlim(times1[0], times1[-1])
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()



