#encoding:utf-8
import ui_AudioEffects
from ui_AudioEffects import Ui_AudioEffects
from PyQt4 import QtCore, QtGui
from PyQt4.Qt import QApplication, SIGNAL, QFileDialog, QIcon,QWidget
from PyQt4 import phonon
from PyQt4.phonon import Phonon
#from mpl_pyqt4_widget import MPL_Widget
import numpy as np
import wave
import scipy.signal as signal
import os, sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Player(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QWidget.__init__(self)
        Ui_AudioEffects.__init__(self)
        self.mediaSource = None
        self.audioPath = ''
        self.file = ''
        self.ui = Ui_AudioEffects
        self.t = []
        self.sources = []
        self.i=1
        self.j=1
        self.k=1
        self.temp="temp.wav"
        self.flag=0
        self.mediaObj = phonon.Phonon.MediaObject(self)
        self.audioSink = Phonon.AudioOutput(Phonon.MusicCategory, self)
        self.audioPath = Phonon.createPath(self.mediaObj, self.audioSink)
        self._createUI()
        self._connect()
        self.show()
    def _createUI(self):
        self.ui = ui_AudioEffects.Ui_AudioEffects()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        #将按钮转换为图片
        self.playIcon= QIcon("play.png")
        self.pauseIcon= QIcon("pause.png")
        stopIcon= QIcon("stop.png")
        musicIcon=QIcon("music.png")
        self.setWindowIcon(musicIcon)
        self.ui.playToolButton.setIcon(self.playIcon)
        self.ui.stopToolButton.setIcon(stopIcon)
        #激活进度条和声音
        self.ui.seekSlider.setMediaObject(self.mediaObj)
        self.ui.volumeSlider.setAudioOutput(self.audioSink)
        #将幅度和频谱框背景置黑
        self.ui.plotWidget.canvas.ax.patch.set_facecolor("black")
        self.ui.plotWidget_2.canvas.ax.patch.set_facecolor("black")
        #打开文件前禁用某些功能
        self.ui.playToolButton.setEnabled(False)
        self.ui.stopToolButton.setEnabled(False)
        self.ui.actionWavesReverb.setEnabled(False)
        self.ui.actionLowPassFilter.setEnabled(False)
        self.ui.actionEcho.setEnabled(False)
    #创建信号槽事件
    def _connect(self):
        #打开文件
        self.connect(self.ui.fileOpenAction,SIGNAL("triggered()"),self.openFileDialog)
        #关闭窗体
        self.connect(self.ui.fileExitAction,SIGNAL("triggered()"),self.close)
        #改变音效
        self.connect(self.ui.actionWavesReverb,SIGNAL("triggered()"),self.reverbEffect)
        self.connect(self.ui.actionEcho,SIGNAL("triggered()"),self.echoEffect)
        self.connect(self.ui.actionLowPassFilter,SIGNAL("triggered()"),self.lpEffect)
        #播放、暂停音乐
        self.connect(self.ui.playToolButton,SIGNAL("clicked()"),self.playMedia)
        #停止音乐
        self.connect(self.ui.stopToolButton,SIGNAL("clicked()"),self.stopMedia)        
    #打开文件
    def openFileDialog(self):
        self.file = ''
        self.file = \
            str(QFileDialog.getOpenFileName(
                self,
                "Open Audio File","/video",
                "wav(*.wav);;"))
        if self.file!='':
            #打开文件后清除checked信息
            self.ui.actionLowPassFilter.setChecked(False)
            self.ui.actionWavesReverb.setChecked(False)
            self.ui.actionEcho.setChecked(False)
            #打开文件后使能check功能
            self.ui.actionWavesReverb.setEnabled(True)
            self.ui.actionLowPassFilter.setEnabled(True)
            self.ui.actionEcho.setEnabled(True)
            self.ui.actionWavesReverb.setCheckable(True)
            self.ui.actionLowPassFilter.setCheckable(True)
            self.ui.actionEcho.setCheckable(True)
            #使能playToolButton
            self.ui.playToolButton.setEnabled(True)
            self.ui.stopToolButton.setEnabled(True)
            self.flag=1
            self.readMediaData()
            self.abs_fft_y=self.fftData(self.y,self.nframes,self.framerate)
            self.plotMediaData(self.y[0],self.abs_fft_y[0])
            self.p = 1
            self.loadNewMedia()
    #缓存新歌
    def loadNewMedia(self):
        if self.mediaSource:
            self.stopMedia()
            del self.mediaSource
        self.mediaSource = phonon.Phonon.MediaSource(self.file)
        self.mediaObj.setCurrentSource(self.mediaSource)
        self.ui.playToolButton.setIcon(self.playIcon) 
    #播放音乐    
    def playMedia(self):  
        
        if self.mediaObj is None:
            print "Error playing Audio"
            return     
        if self.p == 1:
            self.p=0
            self.mediaObj.play()
            self.ui.playToolButton.setIcon(self.pauseIcon)
        else:
            self.pauseMedia()
            self.p = 1
            self.ui.playToolButton.setIcon(self.playIcon) 
        
   #停止播放
    def stopMedia(self):
        self.p=1
        self.mediaObj.stop()   
        self.ui.playToolButton.setIcon(self.playIcon) 
        
    #暂停播放
    def pauseMedia(self):
        self.mediaObj.pause()
    
    def readMediaData(self):
        f = wave.open(self.file, 'rb')
        self.nchannels,self.sampwidth,self.framerate,self.nframes,self.comptype, self.compname=f.getparams()
        str_y=f.readframes(self.nframes)
        f.close()
        y=np.fromstring(str_y,dtype=np.short)
        y.shape = -1,self.nchannels
        self.y=y.T
        
    def fftData(self,y,nframes,framerate):
        #计算信号的频谱
        fft_y=np.fft.fft(y)/nframes
        abs_fft_y = np.abs(fft_y)
        return abs_fft_y
        
    def plotMediaData(self,y,abs_fft_y):
        #绘图
        self.ui.plotWidget.canvas.ax.clear()
        self.ui.plotWidget.canvas.ax.patch.set_facecolor("black")
        self.ui.plotWidget.canvas.ax.plot(y,'-b') 
        self.ui.plotWidget.canvas.draw()
        self.ui.plotWidget_2.canvas.ax.clear()
        self.ui.plotWidget_2.canvas.ax.patch.set_facecolor("black")
        self.ui.plotWidget_2.canvas.ax.plot(abs_fft_y,'-b')
        self.ui.plotWidget_2.canvas.draw()
        
    def reverbEffect(self):
        if self.flag==1:        
            self.loadNewMedia()
            self.i=self.i+1
            self.stopMedia()
            self.ui.actionEcho.setChecked(False)
            self.ui.actionLowPassFilter.setChecked(False)
            if self.ui.actionWavesReverb.isChecked()==True:
                t1=0.4
                t2=0.5
                t3=0.6
                count1=t1*self.framerate
                count2=t2*self.framerate
                count3=t3*self.framerate
                Count=self.nframes+count3
                a1=0.5
                a2=0.4
                a3=0.3
                y1=np.append(self.y,np.zeros(count3))
                y2=np.append(np.zeros(count1),self.y)
                y2=np.append(y2,np.zeros(count3-count1))
                y3=np.append(np.zeros(count2),self.y)
                y3=np.append(y3,np.zeros(count3-count2))
                y4=np.append(np.zeros(count3),self.y)
                y_reverb=y1+a1*y2+a2*y3+a3*y4
            
                abs_fft_y_reverb=self.fftData(y_reverb,Count,self.framerate)
                self.plotMediaData(y_reverb,abs_fft_y_reverb)
                self.saveData(y_reverb,Count,self.nchannels,self.sampwidth,self.framerate,self.comptype,self.compname)
                
                self.loadEffectsMedia()
            else:
                self.plotMediaData(self.y[0],self.abs_fft_y[0])
                self.loadNewMedia()
        
    def echoEffect(self):
        if self.flag==1:      
            self.loadNewMedia()
            self.stopMedia()
            self.ui.actionLowPassFilter.setChecked(False)
            self.ui.actionWavesReverb.setChecked(False)
            if self.ui.actionEcho.isChecked()==True:
                alpha=0.6
                t=0.5
                count=t*self.framerate
                Count=count+self.nframes
                zero=np.zeros(count)
                y1=np.append(self.y,zero)
                y2=np.append(zero,self.y)
                y_echo=y1+alpha*y2
                
                abs_fft_y_echo=self.fftData(y_echo,Count,self.framerate)
                self.plotMediaData(y_echo,abs_fft_y_echo)
                
                self.saveData(y_echo,Count,self.nchannels,self.sampwidth,self.framerate,self.comptype,self.compname)
                self.loadEffectsMedia()     
            else:
                self.plotMediaData(self.y[0],self.abs_fft_y[0])
                self.loadNewMedia()

    def lpEffect(self): 
        if self.flag==1:        
            self.loadNewMedia()
            self.stopMedia()
            self.ui.actionEcho.setChecked(False)
            self.ui.actionWavesReverb.setChecked(False)
            
            if self.ui.actionLowPassFilter.isChecked()==True:   
                b= signal.remez(201, (0, 0.1,  0.12,  0.50), (1, 0.01))
                y_lp=signal.lfilter(b,1,self.y)
                abs_fft_y_lp=self.fftData(y_lp,self.nframes,self.framerate)
                self.plotMediaData(y_lp[0],abs_fft_y_lp[0])
                self.saveData(y_lp,self.nframes,self.nchannels,self.sampwidth,self.framerate,self.comptype,self.compname)
                self.loadEffectsMedia()
             
            else:
                self.plotMediaData(self.y[0],self.abs_fft_y[0])
                self.loadNewMedia()

    #保存音效数据
    def saveData(self,data,nframes,nchannels,sampwidth,framerate,comptype,compname):

        wave_data = data.astype(np.short)
        # 打开WAV文档
        f = wave.open("temp.wav", "wb")
        # 配置声道数、量化位数和取样频率
        f.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))
        # 将wav_data转换为二进制数据写入文件
        f.writeframes(wave_data.tostring())
        f.close()
    #为音频播放插件加载处理后的音效数据  
    def loadEffectsMedia(self):
        if self.mediaSource:
                del self.mediaSource
        self.mediaSource = phonon.Phonon.MediaSource(self.temp)
        self.mediaObj.setCurrentSource(self.mediaSource)
        
app = QApplication(sys.argv)
musicPlayer = Player()
app.exec_()
#程序退出时删除产生的临时文件“temp.wav”
s=os.getcwd()
s=s+"\\"+"temp.wav"
os.remove(s)
#sys.exit(app.exec_())