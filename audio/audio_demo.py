# -*- coding:utf-8 -*-

from audio_process import AudioProcess

# 打开WAV文档
file_path_w = 'wav\\mic_record.wav'
file_path_r1 = 'wav\\mic_1001.wav'
file_path_r2 = 'wav\\SongStero.wav'

AudioProcess().playWav(file_path_r1)
AudioProcess().playWav2(file_path_r1)
#AudioProcess().readWav(file_path_r)
#AudioProcess().splitChannel(file_path_r2)
#AudioProcess().wavTimeplot(file_path_r)
#AudioProcess().wavFftplot(file_path_r)

'''
if input('是否开始录音(y/n):')=='y':
    frames, framerate, samplewidth, nchannel = AudioProcess().recordWav()
    AudioProcess().writeWav(file_path_w, "wb",
                                frames, framerate, samplewidth, nchannel)
    
'''

#AudioProcess().playWav(file_path_r1)
#AudioProcess().playWav(file_path_w2)

#AudioProcess().wavTimeplot(file_path_r1)
#AudioProcess().wavTimeplot(file_path_r2)

#AudioProcess().wavFftplot(file_path_r1)
#AudioProcess().wavFft(file_path_r1)
#AudioProcess().wavFftplot(file_path_r2)
#AudioProcess().wavFft(file_path_r2)


