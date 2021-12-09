import librosa
import numpy as np
import matplotlib.pyplot as plt
import pydub
from scipy.io import wavfile
from scipy import signal
import os
import com.arthenica.mobileffmpeg import FFmpeg

def return_max_amplitude_time(wav):
    # 경로 부분과 파일 이름 부분 잘라주는 것  그 뿐
    (file_dir, file_id) = os.path.split(wav)
    # sampling rate = sampling frequency 단위사긴(초)당 샘플링 횟수 ( Hz)
    sample_rate, data = wavfile.read(wav)

    time = np.linspace(0, len(data) / sample_rate, len(data))

    # 필터링 ( 주파수 기준 )
    b = signal.firwin(101, cutoff=(8000, 16500), fs=sample_rate, pass_zero='bandpass')
    data1 = signal.lfilter(b, [1, 0], data)
    data1 = list(data1)
    # 최고로 큰 소리가 난 시각을 리턴해준다
    return data1.index(max(data1)) / sample_rate

#main은 aac파일을 가져와서 10초 이하의 파일로 자르고 그것들을 양 스테레오로 나누어
# 두개의 wav파일을 저장하는 것 까지

target_path = '/storage/emulated/0/Android/data/com.example.audiorecord/files/Download'
target_file = 'myaudio.aac'
save_path = '/storage/emulated/0/Android/data/com.example.audiorecord/files/Download/result/'


stereo_audio = pydub.AudioSegment.from_file(
    target_path + '/' + target_file,
    format="aac")
print("success")


# Calling the split_to_mono method
# on the stereo audio file
mono_audios = stereo_audio.split_to_mono()

# Exporting/Saving the two mono
# audio files present at index 0(left)
# and index 1(right) of list returned
# by split_to_mono method



if len(mono_audios[0]) > 10000:
    mono_audios_left = mono_audios[0][-3500:-400]
    mono_audios_right = mono_audios[1][-3500:-400]
else:
    mono_audios_left = mono_audios[0]
    mono_audios_right = mono_audios[1]

# 저장한 경로+파일명 변수들
wav_left = save_path+target_file[:-4]+"mono_left.wav"
wav_right = save_path+target_file[:-4]+"mono_right.wav"

mono_left = mono_audios_left.export(
    wav_left,
    format="wav")
mono_right = mono_audios_right.export(
    wav_right,
    format="wav")


# 안드로이드와 연결할 때 바꿔야함
left = return_max_amplitude_time(wav_left)
right = return_max_amplitude_time(wav_right)


