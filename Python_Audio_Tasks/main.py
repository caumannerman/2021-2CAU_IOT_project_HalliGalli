import librosa
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment

#main은 aac 혹은 wav 파일을 가져와서 4초 이하의 파일로 자르고 그것들을 2개의 mono 음원 파일로 나누어
# 그 두개의 wav파일을 지정된 경로에 저장하는 것 까지
# 두 개의 mono wav파일로 필터링 & 분석하는 Task는 fft_module.py에서 진행
# 이 두가지를 모두 합쳐, 양 쪽 두 명의 player가 Tap한 시간을 return해주는 것이 Split2Stereo&Filtering.py파일.


target_path = './image&audio'
target_file = '[6]침대이불위,윗쪽먼저침. 정확도 가장 떨어짐. 너무 강하게 치면 안됐음. 성공률 30%정도.wav'
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
    mono_audios_left = mono_audios[0][-3500:-400]
    mono_audios_right = mono_audios[1][-3500:-400]
else:
    mono_audios_left = mono_audios[0]
    mono_audios_right = mono_audios[1]

# 양 쪽으로 분리한 모노 음원을 save_path에 저장
mono_left = mono_audios_left.export(
    save_path+target_file[:-4]+"mono_left.wav",
    format="wav")
mono_right = mono_audios_right.export(
    save_path+target_file[:-4]+"mono_right.wav",
    format="wav")

print(len(mono_audios))
print(len(mono_audios[0]))
print(len(mono_audios[0][0]))


# 여기부터는 저장한 두 개의 mono 음원을 가져와서  time축에 대하여 amplitude를 plot


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



