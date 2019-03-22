# -*- coding:utf-8 -*-

 

import os
import wave
import pyaudio
import pylab as pl
import numpy as np
from scipy.io import wavfile


class AudioProcess:

    def __init__(self):
        pass

 

# public function

# read wave file to buffer

    def readWav(self, filename):
        """PyAudio Example: Read a wave file to buffer."""
        with wave.open(file_path,'rb') as f:
            # 读取格式信息
            # (nchannels, sampwidth, framerate, nframes, comptype, compname)
            params = f.getparams()
            nchannels, sampwidth, framerate, nframes = params[:4]
            # 读取完整的帧数据到str_data中，这是一个string类型的数据
            str_data = f.readframes(nframes)
            #创建PyAudio对象
            p = pyaudio.PyAudio()
            stream = p.open(format=p.get_format_from_width(sampwidth),
                                    channels=nchannels,
                                    rate=framerate,
                                    output=True)
        
            wave_data = np.fromstring(str_data, dtype=np.short)
            if params[0] == 2:
                wave_data.shape = -1, 2
                wave_data = wave_data.T

            stream.stop_stream()
            stream.close()
            p.terminate()
            
            return wave_data

    def readWavLF(self, filename,filenameLF):
        """读取一个wav文件，并重新采集，过滤掉高频部分"""
        framerate, data = wavfile.read(filename)
        wavfile.write(filenameLF,framerate//5,data[::5])
 

# write buffer to file, only mono

    def writeWav(self, outfilename, writemode, data, framerate, samplewidth, nchannel):
        """PyAudio Example: Write buffer to a wave file."""
        with wave.open(outfilename, writemode) as wf:
            wf.setnchannels(nchannel)
            wf.setsampwidth(samplewidth)
            wf.setframerate(framerate)
            wf.writeframes(b''.join(data))
            wf.close()

 
    def recordWav(self, file_path):
        """PyAudio Example: Record a wave buffer from MIC."""
        RECORD_SECONDS = 10
        CHANNELS = 1            # 声道数1
        RATE = 11025              # 采样率
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
        self.writeWav(file_path, "wb", frames,
                     RATE, pa.get_sample_size(FORMAT), CHANNELS)
        
        stream.stop_stream()
        stream.close()
        pa.terminate()        

 
    def LFrecordWav(self, file_path):
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
        self.writeWav(file_path, "wb", frames,
                     RATE, pa.get_sample_size(FORMAT), CHANNELS)
        
        stream.stop_stream()
        stream.close()
        pa.terminate()


    def recordWav2(self, file_path1,file_path2):
        """录制声音的低频部分，通过降低采样率实现."""
        RECORD_SECONDS = 10
        CHANNELS = 1            # 声道数1
        RATE1 = 11025              # 采样率1
        RATE2 = 4000              # 采样率2
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
        self.writeWav(file_path1, "wb", frames1,
                     RATE1, pa.get_sample_size(FORMAT), CHANNELS)
        self.writeWav(file_path2, "wb", frames2,
                     RATE2, pa.get_sample_size(FORMAT), CHANNELS)
        
        stream1.stop_stream()
        stream1.close()
        stream2.stop_stream()
        stream2.close()
        pa.terminate()


    def playWav(self, file_path):
        """PyAudio Example: Play a wave file."""
        with wave.open(file_path,'rb') as f:
            # 读取格式信息
            # (nchannels, sampwidth, framerate, nframes, comptype, compname)
            params = f.getparams()
            nchannels, sampwidth, framerate, nframes = params[:4]
            # 读取完整的帧数据到str_data中，这是一个string类型的数据
            str_data = f.readframes(nframes)
            #创建PyAudio对象
            p = pyaudio.PyAudio()
            stream = p.open(format=p.get_format_from_width(sampwidth),
                                    channels=nchannels,
                                    rate=framerate,
                                    output=True)

            # play stream
            while len(str_data) > 0:
                stream.write(str_data)
                str_data = f.readframes(nframes)
    
            stream.stop_stream()
            stream.close()
            p.terminate()


# plot wav

    def plotWav(self, file_path):
        with wave.open(file_path,'rb') as f:
            # 读取格式信息
            # (nchannels, sampwidth, framerate, nframes, comptype, compname)
            params = f.getparams()
            nchannels, sampwidth, framerate, nframes = params[:4]
            # 读取完整的帧数据到str_data中，这是一个string类型的数据
            str_data = f.readframes(nframes)
            #创建PyAudio对象
            p = pyaudio.PyAudio()
            stream = p.open(format=p.get_format_from_width(sampwidth),
                                    channels=nchannels,
                                    rate=framerate,
                                    output=True)
            stream.stop_stream()
            stream.close()
            p.terminate()

        #将波形数据转换为数组
        # A new 1-D array initialized from raw binary or text data in a string.
        data = np.frombuffer(str_data, dtype=np.short)

        if 2 == nchannels:
            #将wave_data数组改为2列，行数自动匹配。在修改shape的属性时，需使得数组的总长度不变
            data.shape = -1, 2
            data = wave_data.T          #将数组转置
            length = len(data[0])
            time = np.arange(0, length) * (1.0 / framerate)
            pl.subplot(211)
            pl.plot(time, data[0])
            pl.subplot(212)
            pl.plot(time, data[1], c="g")
            pl.xlabel("time (seconds)")
            pl.show()
        else:
            length = len(data)
            time = np.arange(0, length) * (1.0 / framerate)
            pl.plot(time, data)
            pl.show()

        #显示频率分布图，频分图
        # 采样点数，修改采样点数和起始位置进行不同位置和长度的音频波形分析
        N=44100
        start=0 #开始采样位置
        df = framerate/(N-1) # 分辨率
        freq = [df*n for n in range(0,N)] #N个元素
        if 2 == nchannels:
            wave_data2=data[0][start:start+N]
        else:
            wave_data2=data[start:start+N]
        c=np.fft.fft(wave_data2)*2/N

        #常规显示采样频率一半的频谱
        d=int(len(c)/2)

        #仅显示频率在4000以下的频谱
        while freq[d]>4000:
            d-=10
        pl.plot(freq[:d-1],abs(c[:d-1]),'r')
        pl.show()

 

 

