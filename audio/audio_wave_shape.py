import wave
import pyaudio
import numpy as np
import pylab as pl

 
# 打开WAV文档
#file_path = 'D:\\wav\\200Hz-44.1K-sine_0dB.wav'
file_path = 'D:\\wav\\mic_record_outfile.wav'

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
wave_data = np.frombuffer(str_data, dtype=np.short)



#time 也是一个数组，与wave_data[0]或wave_data[1]配对形成系列点坐标
#time = numpy.arange(0,nframes)*(1.0/framerate)

#绘制波形图
if 2 == nchannels:
    #将wave_data数组改为2列，行数自动匹配。在修改shape的属性时，需使得数组的总长度不变。
    wave_data.shape = -1,2
    #将数组转置
    wave_data = wave_data.T
    length = len(wave_data[0])
    time = np.arange(0, length) * (1.0 / framerate)
    pl.subplot(211)
    pl.plot(time, wave_data[0])
    pl.subplot(212)
    pl.plot(time, wave_data[1], c="g")
    pl.xlabel("time (seconds)")
    pl.show()
else:
    length = len(wave_data)
    time = np.arange(0, length) * (1.0 / framerate)
    pl.plot(time, wave_data)
    pl.xlabel("时间 (秒)")
    pl.show()



# 采样点数，修改采样点数和起始位置进行不同位置和长度的音频波形分析
N=44100
start=0 #开始采样位置
df = framerate/(N-1) # 分辨率
freq = [df*n for n in range(0,N)] #N个元素
if 2 == nchannels:
    wave_data2=wave_data[0][start:start+N]
else:
    wave_data2=wave_data[start:start+N]
c=np.fft.fft(wave_data2)*2/N

#常规显示采样频率一半的频谱
d=int(len(c)/2)

#仅显示频率在4000以下的频谱
while freq[d]>1000:
    d-=10
pl.plot(freq[:d-1],abs(c[:d-1]),'r')
pl.show()
