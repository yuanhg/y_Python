#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "errrolyan"
# Date: 18-12-26
# Describe = "读取wav文件进行傅里叶变换获取频率值"

import wave as we
import numpy as np
import matplotlib.pyplot as plt
import sys

def wavread(path):
    wavfile = we.open(path, "rb")
    params = wavfile.getparams()
    nchannels, sampwidth, framesra, frameswav = params[:4]
    print("nchannels:%d" % nchannels)
    print("sampwidth:%d" % sampwidth)
    datawav = wavfile.readframes(frameswav)
    wavfile.close()
    datause = np.frombuffer(datawav, dtype=np.short)
    if nchannels == 2:
        datause.shape = -1, 2
    datause = datause.T
    time = np.arange(0, frameswav) * (1.0 / framesra)
    return datause, time, nchannels

def fft(path):
    wavdata, wavtime, nchannels = wavread(path)
    df = 1
    freq = [df * n for n in range(0, len(wavdata))]
    c = np.fft.fft(wavdata) * nchannels
    print(c)
    d = int(len(c) / 2)
    fig, ax = plt.subplots(2, 1)
    ax[0].plot(wavtime, wavdata, color='green')
    ax[0].set_xlabel('Time')
    ax[0].set_ylabel('Amplitude')
    ax[1].plot(freq, abs(c), color='red')
    ax[1].set_xlabel('Freq(HZ)')
    ax[1].set_ylabel('Y(freq)')
    plt.show()


#path = 'wav\\mic_record.wav'
path = 'wav\\mic_LF_record.wav'

#path = 'wav\\mic_0000.wav'
#path = 'wav\\mic_0000_enhanced.wav'
fft(path)

