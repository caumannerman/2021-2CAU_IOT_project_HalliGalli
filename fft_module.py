import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal
import os

wav = "./audio/mono_left.wav"
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

plt.figure(figsize=(20,10))
plt.plot(left_f, left_spectrum)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.title("Power spectrum")
plt.show()



b = signal.firwin(101, cutoff=(100,5000), fs=sample_rate, pass_zero='bandstop')
data1 = signal.lfilter(b,[1,0],data)

fft = np.fft.fft(data1)
magnitude = np.abs(fft)

f = np.linspace(0,sample_rate, len(magnitude))
left_spectrum = magnitude[:int(len(magnitude)/2)]
left_f = f[:int(len(magnitude)/2)]

plt.figure(figsize=(20,10))
plt.plot(left_f, left_spectrum)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.title("Power spectrum")
plt.show()

time = np.linspace(0,len(data1)/sample_rate, len(data1))
plt.figure(figsize=(20,10))
plt.plot(time,data1)
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.title("Amplitude - Time")
plt.show()

