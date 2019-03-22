# -*- coding:utf-8 -*-

from audio_process import AudioProcess

# 打开WAV文档
file_path_w = 'wav\\mic_0001.wav'
file_path_w_lf = 'wav\\mic_0001_LF.wav.wav'
file_path_r = 'wav\\mic_0000.wav'



#AudioProcess().playWav(file_path)
'''
if input('是否开始录音(y/n):')=='y':
    AudioProcess().recordWav2(file_path_w,file_path_w_lf)


if input('是否开始录音(y/n):')=='y':
    if input('是否录制低频部分(y/n):')=='y':
        AudioProcess().LFrecordWav(file_path_w_lf)
    else:
        AudioProcess().recordWav(file_path_w)

print("*"*10, "按回车键开始播放录音……","*"*10)
input()
'''

#AudioProcess().playWav(file_path_w_lf)
#AudioProcess().playWav(file_path_w)

AudioProcess().plotWav(file_path_w_lf)
AudioProcess().plotWav(file_path_w)

#AudioProcess().plotWav(file_path_r)

#AudioProcess().readWavLF(file_path_w,file_path_w_lf)
