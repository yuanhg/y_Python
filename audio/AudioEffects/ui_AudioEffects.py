# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AudioEffects.ui'
#
# Created: Mon Mar 24 00:54:46 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_AudioEffects(object):
    def setupUi(self, AudioEffects):
        AudioEffects.setObjectName(_fromUtf8("AudioEffects"))
        AudioEffects.resize(600, 370)
        AudioEffects.setMinimumSize(QtCore.QSize(600, 370))
        AudioEffects.setMaximumSize(QtCore.QSize(600, 370))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("music/Music.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AudioEffects.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(AudioEffects)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.plotWidget = MPL_Widget(self.centralwidget)
        self.plotWidget.setGeometry(QtCore.QRect(0, 10, 601, 131))
        self.plotWidget.setStyleSheet(_fromUtf8(""))
        self.plotWidget.setObjectName(_fromUtf8("plotWidget"))
        self.seekSlider = phonon.Phonon.SeekSlider(self.centralwidget)
        self.seekSlider.setGeometry(QtCore.QRect(10, 270, 581, 22))
        self.seekSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.seekSlider.setAutoFillBackground(False)
        self.seekSlider.setIconVisible(False)
        self.seekSlider.setOrientation(QtCore.Qt.Horizontal)
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 291, 91, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.playToolButton = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.playToolButton.setMinimumSize(QtCore.QSize(30, 30))
        self.playToolButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("music/Play.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.playToolButton.setIcon(icon1)
        self.playToolButton.setObjectName(_fromUtf8("playToolButton"))
        self.horizontalLayout.addWidget(self.playToolButton)
        self.stopToolButton = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.stopToolButton.setMinimumSize(QtCore.QSize(30, 30))
        self.stopToolButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("music/Stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.stopToolButton.setIcon(icon2)
        self.stopToolButton.setObjectName(_fromUtf8("stopToolButton"))
        self.horizontalLayout.addWidget(self.stopToolButton)
        self.volumeSlider = phonon.Phonon.VolumeSlider(self.centralwidget)
        self.volumeSlider.setGeometry(QtCore.QRect(420, 310, 161, 22))
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.plotWidget_2 = MPL_Widget(self.centralwidget)
        self.plotWidget_2.setGeometry(QtCore.QRect(0, 140, 601, 131))
        self.plotWidget_2.setStyleSheet(_fromUtf8(""))
        self.plotWidget_2.setObjectName(_fromUtf8("plotWidget_2"))
        AudioEffects.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(AudioEffects)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 25))
        self.menubar.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAudioEffects = QtGui.QMenu(self.menubar)
        self.menuAudioEffects.setObjectName(_fromUtf8("menuAudioEffects"))
        AudioEffects.setMenuBar(self.menubar)
        self.fileOpenAction = QtGui.QAction(AudioEffects)
        self.fileOpenAction.setObjectName(_fromUtf8("fileOpenAction"))
        self.fileExitAction = QtGui.QAction(AudioEffects)
        self.fileExitAction.setObjectName(_fromUtf8("fileExitAction"))
        self.actionWavesReverb = QtGui.QAction(AudioEffects)
        #self.actionWavesReverb.setCheckable(False)
        self.actionWavesReverb.setObjectName(_fromUtf8("actionWavesReverb"))
        self.actionLowPassFilter = QtGui.QAction(AudioEffects)
        self.actionLowPassFilter.setObjectName(_fromUtf8("actionLowFilter"))
        #self.actionLowPassFilter.setCheckable(False)
        self.actionEcho = QtGui.QAction(AudioEffects)
        self.actionEcho.setObjectName(_fromUtf8("actionEcho"))
        #self.actionEcho.setCheckable(False)
        self.menuFile.addAction(self.fileOpenAction)
        self.menuFile.addAction(self.fileExitAction)
        self.menuAudioEffects.addAction(self.actionWavesReverb)
        self.menuAudioEffects.addAction(self.actionLowPassFilter)
        self.menuAudioEffects.addAction(self.actionEcho)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAudioEffects.menuAction())

        self.retranslateUi(AudioEffects)
        QtCore.QMetaObject.connectSlotsByName(AudioEffects)

    def retranslateUi(self, AudioEffects):
        AudioEffects.setWindowTitle(_translate("AudioEffects", "AudioEffects", None))
        self.stopToolButton.setToolTip(_translate("AudioEffects", "<html><head/><body><p>停止</p></body></html>", None))
        self.menuFile.setTitle(_translate("AudioEffects", "&File", None))
        self.menuAudioEffects.setTitle(_translate("AudioEffects", "&Effects", None))
        self.fileOpenAction.setText(_translate("AudioEffects", "Open", None))
        self.fileOpenAction.setShortcut(_translate("AudioEffects", "Ctrl+P", None))
        self.fileExitAction.setText(_translate("AudioEffects", "Exit", None))
        self.fileExitAction.setShortcut(_translate("AudioEffects", "Ctrl+E", None))
        self.actionWavesReverb.setText(_translate("AudioEffects", "WavesReverb", None))
        self.actionLowPassFilter.setText(_translate("AudioEffects", "LowPassFilter", None))
        self.actionEcho.setText(_translate("AudioEffects", "Echo", None))

from PyQt4 import phonon
from mpl_pyqt4_widget import MPL_Widget
