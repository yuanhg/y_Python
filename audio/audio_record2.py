# -*- coding:utf-8 -*-

import os
import wave
import pyaudio
import pylab as pl
import numpy as np


# 打开WAV文档
file_path_w = 'wav\\mic_record.wav'
file_path_w_lf = 'wav\\mic_LF_record.wav'
file_path_r = 'wav\\Ring04.wav'


def writeWav(outfilename, writemode, data, framerate, samplewidth, nchannel):
        """PyAudio Example: Write buffer to a wave file."""
        with wave.open(outfilename, writemode) as wf:
            wf.setnchannels(nchannel)
            wf.setsampwidth(samplewidth)
            wf.setframerate(framerate)
            wf.writeframes(b''.join(data))
            wf.close()

def LFrecordWav(file_path1,file_path2):
        """录制声音的低频部分，通过降低采样率实现."""
        RECORD_SECONDS = 10
        CHANNELS = 1            # 声道数1
        RATE1 = 11025              # 采样率1
        RATE2 = 2000              # 采样率2
        FORMAT = pyaudio.paInt16
        CHUNK = 256

        pa = pyaudio.PyAudio()
        stream1 = pa.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE1,
                        input=True,
                        frames_per_buffer=CHUNK)
        stream2 = pa.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE2,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("*"*10, "开始录音10秒钟","*"*10)
        frames1 = []
        frames2 = []
        for i in range(0, int(RATE1 / CHUNK * RECORD_SECONDS)):
            data1 = stream1.read(CHUNK)
            frames1.append(data1)
        for i in range(0, int(RATE2 / CHUNK * RECORD_SECONDS)):
            data2 = stream2.read(CHUNK)
            frames2.append(data2)
        print("*"*10, "录音结束","*"*10)

        #wave_data = np.frombuffer(frames, dtype=np.short)
        writeWav(file_path1, "wb", frames1,
                     RATE1, pa.get_sample_size(FORMAT), CHANNELS)
        writeWav(file_path2, "wb", frames2,
                     RATE2, pa.get_sample_size(FORMAT), CHANNELS)
        
        stream1.stop_stream()
        stream1.close()
        stream2.stop_stream()
        stream2.close()
        pa.terminate()


LFrecordWav(file_path_w,file_path_w_lf)
