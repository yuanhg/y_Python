# -*- coding:utf-8 -*-

import wave
import pyaudio
import pylab as pl
import matplotlib.pyplot as plt 
import numpy as np
import time

from scipy import signal
from scipy.io import wavfile



class AudioProcess:

    def __init__(self):
        pass

 

# public function

    def readWav(self, file_path):
        """把wav文件读到变量."""
        with wave.open(file_path,'rb') as f:
            # 读取格式信息，返回tuple，数据对应如下
            # (nchannels, sampwidth, framerate, nframes, comptype, compname)
            params = f.getparams()
            print("nchannels:%d , sampwidth:%d , framerate:%d , nframes:%d "
                  %(params[0],params[1],params[2],params[3]),
                  "\ncomptype:%s,compname:%s"%(params[4],params[5]))
            
            # 读取完整的帧数据到str_data中，这是一个string类型的数据
            str_data = f.readframes(params[3])
                        
        #将波形数据转换为数组
        # A new 1-D array initialized from raw binary or text data in a string.
        wav_data = np.frombuffer(str_data, dtype=np.short)
        
        if params[0] == 2:
            wav_data.shape = -1, 2
            wav_data = wav_data.T
        else:
            #把单声道数据复制到双声道
            wav_data = np.concatenate((wav_data,wav_data))
            wav_data.shape = 2,-1            
                
        time = np.arange(0, params[3]) * (1.0 / params[2])
        
        #str_data是字符串, wav_data是二维数组, time是一维数组, params是参数元组
        return str_data, wav_data, time, params


    def writeWav(self, file_path, writemode, frames, framerate, samplewidth, nchannel):
        """PyAudio Example: Write buffer to a wave file."""
        with wave.open(file_path, writemode) as f:
            f.setnchannels(nchannel)
            f.setsampwidth(samplewidth)
            f.setframerate(framerate)
            f.writeframes(b''.join(frames))

 
    def recordWav(self):
        """
        PyAudio Example: Record a wave buffer from MIC.
        44100HZ 16bit stereo:
            每秒钟有 44100 次采样,采样数据用 16 位(2字节)记录, 双声道(立体声);
        11025HZ 8bit  mono:
            每秒钟有 11025 次采样,采样数据用 8 位(1字节)记录, 单声道

        采样值是指每一次采样周期内声音模拟信号的积分值。
        对于单声道声音文件，采样数据为八位的短整数（short int 00H-FFH）；
        对于双声道立体声声音文件，每次采样数据为一个16位的整数（int），
            高八位和低八位分别代表左右两个声道

        对噪音采取单声道，但高采样率，16位记录，便于分析噪音
        """
        RECORD_SECONDS = 10
        CHANNELS = 1            # 声道数1
        FRAMERATE = 44100              # 采样率
        FORMAT = pyaudio.paInt16    # 采样值16位，2个字节
        CHUNK = 1024

        pa = pyaudio.PyAudio()
        stream = pa.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=FRAMERATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        frames = []
        start_time = time.time()
        print("*"*10, "开始录音10秒钟","*"*10)
        for i in range(0, int(FRAMERATE / CHUNK * RECORD_SECONDS+1)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("录音时长：%d"%(time.time()-start_time))
        print("*"*10, "录音结束","*"*10)

        stream.stop_stream()
        stream.close()
        pa.terminate()

        return frames, FRAMERATE, pa.get_sample_size(FORMAT), CHANNELS
                

    def splitChannel(self,file_path):
        framerate,data = wavfile.read(file_path)
        left = []
        right = []
        for item in data:
            left.append(item[0])
            right.append(item[1])
        wavfile.write('wav\\_left.wav',framerate,np.array(left))
        wavfile.write('wav\\_right.wav',framerate,np.array(right))

        
    def playWav(self, file_path):
        """PyAudio Example: Play a wave file."""
        # (nchannels, sampwidth, framerate, nframes, comptype, compname)
        str_data, wav_data, wav_time, params = AudioProcess().readWav(file_path)
        
        #创建PyAudio对象        
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(params[1]),
                                    channels=params[0],
                                    rate=params[2],
                                    output=True)

        # play stream
        stream.write(str_data)
           
        stream.stop_stream()
        stream.close()
        p.terminate()


    def playWav2(self, file_path):
        """把wav文件读到变量."""
        with wave.open(file_path,'rb') as f:
            # 读取格式信息，返回tuple，数据对应如下
            # (nchannels, sampwidth, framerate, nframes, comptype, compname)
            params = f.getparams()
            print("nchannels:%d , sampwidth:%d , framerate:%d , nframes:%d "
                  %(params[0],params[1],params[2],params[3]),
                  "\ncomptype:%s,compname:%s"%(params[4],params[5]))
            
            # 读取完整的帧数据到str_data中，这是一个string类型的数据
            str_data = f.readframes(params[3])
        #print(str_data[-20:])
        wav_data = np.frombuffer(str_data, dtype=np.short)
        print(wav_data[-10:])
        wav_data = np.concatenate((wav_data,-wav_data))
        wav_data.shape = 2,-1
        wav_data = wav_data.T
        wav_data = wav_data.reshape(1,-1)
        str_data2 = list(wav_data[0])
        print(str_data2[-20:])
        str_data2 = b''.join(str_data2)
        #print(str_data2[-40:])
        #创建PyAudio对象        
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(params[1]),
                                    channels=2,
                                    rate=params[2],
                                    output=True)

        # play stream
        stream.write(str_data2)
           
        stream.stop_stream()
        stream.close()
        p.terminate()
# plot wav

    def wavTimeplot(self, file_path):
        # (nchannels, sampwidth, framerate, nframes, comptype, compname)
        str_data, wav_data, wav_time, params = AudioProcess().readWav(file_path)

        pl.subplot(211)
        pl.plot(wav_time, wav_data[0])
        pl.xlabel("Time (seconds)")
        pl.ylabel('R Amplitude')
        pl.subplot(212)
        pl.plot(wav_time, wav_data[1], c="g")
        pl.xlabel("Time (seconds)")
        pl.ylabel('L Amplitude')
        pl.show()

    def wavFftplot(self,file_path):
        '''读取wav文件进行傅里叶变换获取频率值'''
        # (nchannels, sampwidth, framerate, nframes, comptype, compname)
        str_data, wav_data, wav_time, params = AudioProcess().readWav(file_path)
        '''
        df = 1
        freq = [df * n for n in range(0, len(wav_data[0]))]
        c = np.fft.fft(wav_data[0]) * params[0]
        d = int(len(c) / 2)
        '''
        N = 44100
        start = 0
        df = params[2]/(N-1)
        freq = [df*n for n in range(0,N)]
        data = wav_data[0][start:start+N]
        c = np.fft.fft(data) * 2/N
        d = int(len(c)/2)
        
        pl.plot(freq[:d-1],abs(c[:d-1]),'r')
        pl.show()

    def wavFft(self,file_path):
        sampling_freq,audio = wavfile.read(file_path)
        audio = audio/(2.**15)
        len_audio = len(audio)

        transformed_signal = np.fft.fft(audio)
        half_length = np.ceil((len_audio+1)/2.0)
        transformed_signal = abs(transformed_signal[0:int(half_length)])
        transformed_signal /= float(len_audio)
        transformed_signal **= 2

        len_ts = len(transformed_signal)

        if len_audio %2:
            transformed_signal[1:len_ta] *= 2
        else:
            transformed_signal[1:len_ts-1] *= 2

        power = -10 * np.log10(transformed_signal)
        x_values = np.arange(0, half_length, 1) * (sampling_freq / len_audio) / 1000.0 
        
        plt.figure()
        plt.plot(x_values,power,color='black')
        plt.xlabel('Freq (in kHz)')
        plt.ylabel('Power (in dB)')
        plt.show()


    def fft(yt, sampling_rate, fft_size=None):
        if fft_size is None:  
            fft_size = len(yt)  
        yt = yt[:fft_size]  
        yf = abs( np.fft.rfft(yt)/fft_size )  
        freqs = np.linspace(0, 1.0*sampling_rate/2, 1.0*fft_size/2+1)
    
        return freqs, yf

    
        
