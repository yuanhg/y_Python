# -*- coding:utf-8 -*-

import os
import wave
import pyaudio
import pylab as pl
import numpy as np


# 打开WAV文档
file_path_w = 'wav\\mic_LF_record.wav'
file_path_r = 'wav\\Ring04.wav'


def writeWav(outfilename, writemode, data, framerate, samplewidth, nchannel):
        """PyAudio Example: Write buffer to a wave file."""
        with wave.open(outfilename, writemode) as wf:
            wf.setnchannels(nchannel)
            wf.setsampwidth(samplewidth)
            wf.setframerate(framerate)
            wf.writeframes(b''.join(data))
            wf.close()

def LFrecordWav(file_path):
        """录制声音的低频部分，通过降低采样率实现."""
        RECORD_SECONDS = 10
        CHANNELS = 1            # 声道数1
        RATE = 2000              # 采样率
        FORMAT = pyaudio.paInt16
        CHUNK = 256

        pa = pyaudio.PyAudio()
        stream = pa.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("*"*10, "开始录音10秒钟","*"*10)
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("*"*10, "录音结束","*"*10)

        #wave_data = np.frombuffer(frames, dtype=np.short)
        writeWav(file_path, "wb", frames,
                     RATE, pa.get_sample_size(FORMAT), CHANNELS)
        
        stream.stop_stream()
        stream.close()
        pa.terminate()


LFrecordWav(file_path_w)
