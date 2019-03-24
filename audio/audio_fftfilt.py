from scipy import signal
import numpy as np
import wave
import math
import matplotlib.pyplot as plt

def fft(yt, sampling_rate, fft_size=None):  
    if fft_size is None:  
        fft_size = len(yt)  
    yt = yt[:fft_size]  
    yf = abs( np.fft.rfft(yt) / fft_size )  
    freqs = np.linspace(0, 1.0*sampling_rate/2, 1.0*fft_size/2+1)
    
    return freqs, yf  



# 打开WAV文档
file_path = 'wav\\ThatGirl.WAV'
#file_path = 'wav\\noise001_enhanced.wav'

with wave.open(file_path,'rb') as f:
    params = f.getparams()
    str_data = f.readframes(params[3])
    
'''
print("nchannels:%d , sampwidth:%d , framerate:%d , nframes:%d "
                  %(params[0],params[1],params[2],params[3]))
'''

wav_data = np.frombuffer(str_data, dtype=np.short)
if params[0] == 2:
    wav_data.shape = -1, 2
    wav_data = wav_data.T
else:
    wav_data = np.concatenate((wav_data,wav_data))
    wav_data.shape = 2,-1

time = np.arange(0, params[3]) * (1.0 / params[2])


fs = params[2] # sample rate
nyq = fs / 2   # nyqust rate, the maximun rate that can be rebuild
yt = wav_data[0]


plt.subplot(221)
plt.plot(time,yt)
plt.ylabel('Amplitude(original)')

freqs, yf = fft(yt, fs)
plt.subplot(222)
plt.plot(freqs, yf)

'''
# 低通滤波器
# 阶数；最大纹波允许低于通频带中的单位增益。
# 以分贝表示，以正数表示；频率(Hz)/奈奎斯特频率（采样率*0.5）
'''
b, a = signal.butter(4, 110/nyq, "lowpass") # lowpass
#b, a = signal.cheby1(4, 5, 110/nyq, "lowpass") # lowpass
yt  = signal.filtfilt(b, a, yt)
plt.subplot(223)
plt.plot(time,yt)
plt.xlabel("Time (seconds)")
plt.ylabel('Amplitude(filt)')

freqs, yf = fft(yt, fs)
plt.subplot(224)
plt.plot(freqs, yf)
plt.xlabel('Freq (in kHz)')

plt.show()
