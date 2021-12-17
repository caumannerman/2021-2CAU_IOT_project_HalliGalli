import librosa
import numpy as np
import matplotlib.pyplot as plt
import pydub
from scipy.io import wavfile
from scipy import signal
import os
import sys
# sys.path.append('C:\Program Files\ffmpeg\ffmpeg-4.4.1-full_build\ffmpeg-4.4.1-full_build\bin\ffmpeg.exe')
#audio segment를 위해 로컬에 설치
sys.path.append('C:\\Program Files\\ffmpeg-4.4.1-essentials_build\\bin\\ffmpeg.exe')

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





def pythonRun(s):
    #main은 aac파일을 가져와서 10초 이하의 파일로 자르고 그것들을 양 스테레오로 나누어
    # 두개의 wav파일을 저장하는 것 까지

    target_path = '/storage/emulated/0/Android/data/com.example.audiorecord/files/Download'
    target_file = s                      # 'omRecorder.wav'
    save_path = '/storage/emulated/0/Android/data/com.example.audiorecord/files/Download/result/'
    pydub.AudioSegment.ffmpeg = r'C:\\Program Files\\ffmpeg-4.4.1-essentials_build\\bin\\ffmpeg.exe'
    pydub.AudioSegment.converter = r'C:\\Program Files\\ffmpeg-4.4.1-essentials_build\\bin\\ffmpeg.exe'
    pydub.AudioSegment.ffprobe = r'C:\\Program Files\\ffmpeg-4.4.1-essentials_build\\bin\\ffmpeg.exe'
    stereo_audio = pydub.AudioSegment.from_file(
        target_path + '/' + target_file,
        format="wav")


    # Calling the split_to_mono method
    # on the stereo audio file
    mono_audios = stereo_audio.split_to_mono()

    # Exporting/Saving the two mono
    # audio files present at index 0(left)
    # and index 1(right) of list returned
    # by split_to_mono method


# 4초 이상인 경우 자름
    if len(mono_audios[0]) > 4000:
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

# 나누어진 두 모노 파일에서 각 플레이어가 책상을 Tap한 시간을 return해줌 ( 안드로이드에서 실행 )
    left = return_max_amplitude_time(wav_left)
    right = return_max_amplitude_time(wav_right)


    return left, right

