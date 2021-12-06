import librosa
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment

#main은 aac파일을 가져와서 10초 이하의 파일로 자르고 그것들을 양 스테레오로 나누어
# 두개의 wav파일을 저장하는 것 까지
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
target_path = './audio'
target_file = '상단소음_상단먼저침.aac'
save_path = './result/'

stereo_audio = AudioSegment.from_file(
    target_path + '/' + target_file,
    format="aac")

# Calling the split_to_mono method
# on the stereo audio file
mono_audios = stereo_audio.split_to_mono()

# Exporting/Saving the two mono
# audio files present at index 0(left)
# and index 1(right) of list returned
# by split_to_mono method

print(type(mono_audios))
print(len(mono_audios))
print(len(mono_audios[0]))
print("----------------------------")

if len(mono_audios[0]) > 10000:
    mono_audios_left = mono_audios[0][-10000:]
    mono_audios_right = mono_audios[1][-10000:]
else:
    mono_audios_left = mono_audios[0]
    mono_audios_right = mono_audios[1]


mono_left = mono_audios_left.export(
    save_path+target_file[:-4]+"mono_left.wav",
    format="wav")
mono_right = mono_audios_right.export(
    save_path+target_file[:-4]+"mono_right.wav",
    format="wav")

print(len(mono_audios))
print(len(mono_audios[0]))
print(len(mono_audios[0][0]))


# 여기부터는 안해도 됨


data1, samplerate1 = librosa.load(save_path+target_file[:-4]+"mono_left.wav")
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


data1, samplerate1 = librosa.load(save_path+target_file[:-4]+"mono_right.wav")
print(data1.shape, samplerate1)
times1 = np.arange(len(data1))/float(samplerate1)
#sd.play(data,samplerate)
plt.plot(times1, data1)
plt.xlim(times1[0], times1[-1])
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()



