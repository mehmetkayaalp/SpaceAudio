# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ArtistList = QtWidgets.QListWidget(self.centralwidget)
        self.ArtistList.setObjectName("ArtistList")
        self.horizontalLayout.addWidget(self.ArtistList)
        self.AlbumList = QtWidgets.QListWidget(self.centralwidget)
        self.AlbumList.setObjectName("AlbumList")
        self.horizontalLayout.addWidget(self.AlbumList)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.TrackTable = QtWidgets.QTableWidget(self.centralwidget)
        self.TrackTable.setShowGrid(True)
        self.TrackTable.setGridStyle(QtCore.Qt.SolidLine)
        self.TrackTable.setWordWrap(False)
        self.TrackTable.setObjectName("TrackTable")
        self.TrackTable.setColumnCount(8)
        self.TrackTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TrackTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TrackTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TrackTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TrackTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TrackTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TrackTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TrackTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.TrackTable.setHorizontalHeaderItem(7, item)
        self.TrackTable.horizontalHeader().setSortIndicatorShown(True)
        self.TrackTable.horizontalHeader().setStretchLastSection(True)
        self.TrackTable.verticalHeader().setVisible(False)
        self.TrackTable.verticalHeader().setHighlightSections(True)
        self.TrackTable.verticalHeader().setSortIndicatorShown(False)
        self.TrackTable.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.TrackTable)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.PreviousTrack = QtWidgets.QPushButton(self.centralwidget)
        self.PreviousTrack.setText("")
        self.PreviousTrack.setObjectName("PreviousTrack")
        self.horizontalLayout_2.addWidget(self.PreviousTrack)
        self.PlayPause = QtWidgets.QPushButton(self.centralwidget)
        self.PlayPause.setText("")
        self.PlayPause.setIconSize(QtCore.QSize(64, 64))
        self.PlayPause.setObjectName("PlayPause")
        self.horizontalLayout_2.addWidget(self.PlayPause)
        self.NextTrack = QtWidgets.QPushButton(self.centralwidget)
        self.NextTrack.setText("")
        self.NextTrack.setObjectName("NextTrack")
        self.horizontalLayout_2.addWidget(self.NextTrack)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TrackName = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TrackName.sizePolicy().hasHeightForWidth())
        self.TrackName.setSizePolicy(sizePolicy)
        self.TrackName.setObjectName("TrackName")
        self.verticalLayout_2.addWidget(self.TrackName)
        self.TrackSlider = QtWidgets.QSlider(self.centralwidget)
        self.TrackSlider.setMaximum(1000)
        self.TrackSlider.setPageStep(1)
        self.TrackSlider.setOrientation(QtCore.Qt.Horizontal)
        self.TrackSlider.setObjectName("TrackSlider")
        self.verticalLayout_2.addWidget(self.TrackSlider)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ElapsedTime = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ElapsedTime.sizePolicy().hasHeightForWidth())
        self.ElapsedTime.setSizePolicy(sizePolicy)
        self.ElapsedTime.setObjectName("ElapsedTime")
        self.horizontalLayout_3.addWidget(self.ElapsedTime)
        self.TrackLength = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TrackLength.sizePolicy().hasHeightForWidth())
        self.TrackLength.setSizePolicy(sizePolicy)
        self.TrackLength.setObjectName("TrackLength")
        self.horizontalLayout_3.addWidget(self.TrackLength)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.VolumeSlider = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VolumeSlider.sizePolicy().hasHeightForWidth())
        self.VolumeSlider.setSizePolicy(sizePolicy)
        self.VolumeSlider.setMinimumSize(QtCore.QSize(0, 25))
        self.VolumeSlider.setStyleSheet("")
        self.VolumeSlider.setMaximum(100)
        self.VolumeSlider.setSingleStep(5)
        self.VolumeSlider.setProperty("value", 100)
        self.VolumeSlider.setOrientation(QtCore.Qt.Vertical)
        self.VolumeSlider.setObjectName("VolumeSlider")
        self.horizontalLayout_2.addWidget(self.VolumeSlider)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen_File_s = QtWidgets.QAction(MainWindow)
        self.actionOpen_File_s.setObjectName("actionOpen_File_s")
        self.actionManage_Library = QtWidgets.QAction(MainWindow)
        self.actionManage_Library.setObjectName("actionManage_Library")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionReport_Issue = QtWidgets.QAction(MainWindow)
        self.actionReport_Issue.setObjectName("actionReport_Issue")
        self.actionRescan_Library = QtWidgets.QAction(MainWindow)
        self.actionRescan_Library.setObjectName("actionRescan_Library")
        self.actionRescan_Library_Full = QtWidgets.QAction(MainWindow)
        self.actionRescan_Library_Full.setObjectName("actionRescan_Library_Full")
        self.actionContact = QtWidgets.QAction(MainWindow)
        self.actionContact.setObjectName("actionContact")
        self.menuFile.addAction(self.actionOpen_File_s)
        self.menuFile.addAction(self.actionManage_Library)
        self.menuFile.addAction(self.actionRescan_Library)
        self.menuFile.addAction(self.actionRescan_Library_Full)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionReport_Issue)
        self.menuHelp.addAction(self.actionContact)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SpaceAudio"))
        self.ArtistList.setSortingEnabled(False)
        self.TrackTable.setSortingEnabled(True)
        item = self.TrackTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Title"))
        item = self.TrackTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Artist"))
        item = self.TrackTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Album"))
        item = self.TrackTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Length"))
        item = self.TrackTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Track Number"))
        item = self.TrackTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Filename"))
        item = self.TrackTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Path"))
        item = self.TrackTable.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "File Size"))
        self.TrackName.setText(_translate("MainWindow", "Track Name"))
        self.ElapsedTime.setText(_translate("MainWindow", "0:00"))
        self.TrackLength.setText(_translate("MainWindow", "0:00"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen_File_s.setText(_translate("MainWindow", "Open Files"))
        self.actionOpen_File_s.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionManage_Library.setText(_translate("MainWindow", "Manage Library"))
        self.actionManage_Library.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionReport_Issue.setText(_translate("MainWindow", "Report Issue"))
        self.actionRescan_Library.setText(_translate("MainWindow", "Rescan Library"))
        self.actionRescan_Library.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionRescan_Library_Full.setText(_translate("MainWindow", "Rescan Library (Full)"))
        self.actionRescan_Library_Full.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionContact.setText(_translate("MainWindow", "Contact"))

