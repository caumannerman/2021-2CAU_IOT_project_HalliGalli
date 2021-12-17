import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal
import os
# fft_module은 원본 audio ,필터링 후 audio, fft후 주파수 대역 plot 총 4가지를 plot해줌 (현재는 fft관련 plot은 주석처리)
# 단순히 filter를 설계하는 과정에서 쓰인 코드
# 안드로이드에는 fft없이 필터링 하는 코드만 들어간다.

wav = "./result/[6]침대이불위,윗쪽먼저침. 정확도 가장 떨어짐. 너무 강하게 치면 안됐음. 성공률 30%정도mono_right.wav"

#경로 부분과 파일 이름 부분 잘라주는 것  그 뿐
(file_dir, file_id) = os.path.split(wav)

print("Path : ", file_dir)
print("Name : ", file_id)

# sampling rate = sampling frequency 단위사긴(초)당 샘플링 횟수 ( Hz)
sample_rate, data = wavfile.read(wav)
print("Sample rate : {0}, data size : {1}, duartion : {2} seconds".format(sample_rate, data.shape, len(data)/sample_rate))

time = np.linspace(0, len(data)/sample_rate, len(data))

plt.figure(figsize=(20,10))
plt.plot(time,data)
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.title("Amplitude - Time")
plt.show()


fft = np.fft.fft(data)
magnitude = np.abs(fft)

f = np.linspace(0,sample_rate, len(magnitude))
left_spectrum = magnitude[:int(len(magnitude)/2)]
left_f = f[:int(len(magnitude)/2)]
'''
plt.figure(figsize=(20,10))
plt.plot(left_f, left_spectrum)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.title("Power spectrum")
plt.show()
'''


b = signal.firwin(101, cutoff=(7000,16500), fs=sample_rate, pass_zero='bandpass')
data1 = signal.lfilter(b,[1,0],data)

fft = np.fft.fft(data1)
magnitude = np.abs(fft)

f = np.linspace(0,sample_rate, len(magnitude))
left_spectrum = magnitude[:int(len(magnitude)/2)]
left_f = f[:int(len(magnitude)/2)]

'''
plt.figure(figsize=(20,10))
plt.plot(left_f, left_spectrum)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.title("Power spectrum")
plt.show()
'''

time = np.linspace(0,len(data1)/sample_rate, len(data1))
plt.figure(figsize=(20,10))
plt.plot(time,data1)
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.title("Amplitude - Time")
plt.show()

data1 = list(data1)


print(len(data1))

print(data1.index(max(data1)) / sample_rate)