# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1212, 738)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.VisualsBox = QtWidgets.QGroupBox(self.centralwidget)
        self.VisualsBox.setGeometry(QtCore.QRect(0, 110, 191, 331))
        self.VisualsBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.VisualsBox.setObjectName("VisualsBox")
        self.layoutWidget = QtWidgets.QWidget(self.VisualsBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 17, 171, 239))
        self.layoutWidget.setObjectName("layoutWidget")
        self.VisualSettingsMenu = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.VisualSettingsMenu.setContentsMargins(0, 0, 0, 0)
        self.VisualSettingsMenu.setObjectName("VisualSettingsMenu")
        self.scale = QtWidgets.QHBoxLayout()
        self.scale.setObjectName("scale")
        self.scale_slider = QtWidgets.QLabel(self.layoutWidget)
        self.scale_slider.setObjectName("scale_slider")
        self.scale.addWidget(self.scale_slider)
        self.scale_label = QtWidgets.QSlider(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scale_label.sizePolicy().hasHeightForWidth())
        self.scale_label.setSizePolicy(sizePolicy)
        self.scale_label.setOrientation(QtCore.Qt.Horizontal)
        self.scale_label.setObjectName("scale_label")
        self.scale.addWidget(self.scale_label)
        self.VisualSettingsMenu.addLayout(self.scale)
        self.start = QtWidgets.QHBoxLayout()
        self.start.setObjectName("start")
        self.start_slider = QtWidgets.QLabel(self.layoutWidget)
        self.start_slider.setObjectName("start_slider")
        self.start.addWidget(self.start_slider)
        self.start_label = QtWidgets.QSlider(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_label.sizePolicy().hasHeightForWidth())
        self.start_label.setSizePolicy(sizePolicy)
        self.start_label.setOrientation(QtCore.Qt.Horizontal)
        self.start_label.setObjectName("start_label")
        self.start.addWidget(self.start_label)
        self.VisualSettingsMenu.addLayout(self.start)
        self.end = QtWidgets.QHBoxLayout()
        self.end.setObjectName("end")
        self.end_slider = QtWidgets.QLabel(self.layoutWidget)
        self.end_slider.setObjectName("end_slider")
        self.end.addWidget(self.end_slider)
        self.end_label = QtWidgets.QSlider(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_label.sizePolicy().hasHeightForWidth())
        self.end_label.setSizePolicy(sizePolicy)
        self.end_label.setOrientation(QtCore.Qt.Horizontal)
        self.end_label.setObjectName("end_label")
        self.end.addWidget(self.end_label)
        self.VisualSettingsMenu.addLayout(self.end)
        self.flip_one_check = QtWidgets.QCheckBox(self.layoutWidget)
        self.flip_one_check.setObjectName("flip_one_check")
        self.VisualSettingsMenu.addWidget(self.flip_one_check)
        self.flip_two_check = QtWidgets.QCheckBox(self.layoutWidget)
        self.flip_two_check.setObjectName("flip_two_check")
        self.VisualSettingsMenu.addWidget(self.flip_two_check)
        self.font_size = QtWidgets.QHBoxLayout()
        self.font_size.setObjectName("font_size")
        self.font_size_slider = QtWidgets.QLabel(self.layoutWidget)
        self.font_size_slider.setObjectName("font_size_slider")
        self.font_size.addWidget(self.font_size_slider)
        self.font_size_label = QtWidgets.QSlider(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.font_size_label.sizePolicy().hasHeightForWidth())
        self.font_size_label.setSizePolicy(sizePolicy)
        self.font_size_label.setOrientation(QtCore.Qt.Horizontal)
        self.font_size_label.setObjectName("font_size_label")
        self.font_size.addWidget(self.font_size_label)
        self.VisualSettingsMenu.addLayout(self.font_size)
        self.font_y = QtWidgets.QHBoxLayout()
        self.font_y.setObjectName("font_y")
        self.font_y_slider = QtWidgets.QLabel(self.layoutWidget)
        self.font_y_slider.setObjectName("font_y_slider")
        self.font_y.addWidget(self.font_y_slider)
        self.font_y_label = QtWidgets.QSlider(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.font_y_label.sizePolicy().hasHeightForWidth())
        self.font_y_label.setSizePolicy(sizePolicy)
        self.font_y_label.setOrientation(QtCore.Qt.Horizontal)
        self.font_y_label.setObjectName("font_y_label")
        self.font_y.addWidget(self.font_y_label)
        self.VisualSettingsMenu.addLayout(self.font_y)
        self.startButton = QtWidgets.QPushButton(self.VisualsBox)
        self.startButton.setGeometry(QtCore.QRect(10, 280, 81, 28))
        self.startButton.setObjectName("startButton")
        self.stopButton = QtWidgets.QPushButton(self.VisualsBox)
        self.stopButton.setGeometry(QtCore.QRect(102, 280, 71, 28))
        self.stopButton.setObjectName("stopButton")
        self.SettingsBox = QtWidgets.QGroupBox(self.centralwidget)
        self.SettingsBox.setGeometry(QtCore.QRect(-1, 10, 191, 101))
        self.SettingsBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.SettingsBox.setObjectName("SettingsBox")
        self.layoutWidget1 = QtWidgets.QWidget(self.SettingsBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 21, 183, 78))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.SettingsMenu = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.SettingsMenu.setContentsMargins(0, 0, 0, 0)
        self.SettingsMenu.setObjectName("SettingsMenu")
        self.show_gui_check = QtWidgets.QCheckBox(self.layoutWidget1)
        self.show_gui_check.setStyleSheet("")
        self.show_gui_check.setObjectName("show_gui_check")
        self.SettingsMenu.addWidget(self.show_gui_check)
        self.full_screen_check = QtWidgets.QCheckBox(self.layoutWidget1)
        self.full_screen_check.setObjectName("full_screen_check")
        self.SettingsMenu.addWidget(self.full_screen_check)
        self.select_screen = QtWidgets.QHBoxLayout()
        self.select_screen.setObjectName("select_screen")
        self.select_screen_label = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_screen_label.sizePolicy().hasHeightForWidth())
        self.select_screen_label.setSizePolicy(sizePolicy)
        self.select_screen_label.setObjectName("select_screen_label")
        self.select_screen.addWidget(self.select_screen_label)
        self.select_screen_btn = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_screen_btn.sizePolicy().hasHeightForWidth())
        self.select_screen_btn.setSizePolicy(sizePolicy)
        self.select_screen_btn.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.select_screen_btn.setObjectName("select_screen_btn")
        self.select_screen.addWidget(self.select_screen_btn)
        self.SettingsMenu.addLayout(self.select_screen)
        self.InfoBox = QtWidgets.QGroupBox(self.centralwidget)
        self.InfoBox.setGeometry(QtCore.QRect(0, 430, 191, 231))
        self.InfoBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.InfoBox.setObjectName("InfoBox")
        self.layoutWidget2 = QtWidgets.QWidget(self.InfoBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(11, 20, 171, 181))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.InFoBoxMenu = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.InFoBoxMenu.setContentsMargins(0, 0, 0, 0)
        self.InFoBoxMenu.setObjectName("InFoBoxMenu")
        self.scene = QtWidgets.QHBoxLayout()
        self.scene.setObjectName("scene")
        self.scene_label = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scene_label.sizePolicy().hasHeightForWidth())
        self.scene_label.setSizePolicy(sizePolicy)
        self.scene_label.setObjectName("scene_label")
        self.scene.addWidget(self.scene_label)
        self.scene_value = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scene_value.sizePolicy().hasHeightForWidth())
        self.scene_value.setSizePolicy(sizePolicy)
        self.scene_value.setObjectName("scene_value")
        self.scene.addWidget(self.scene_value)
        self.InFoBoxMenu.addLayout(self.scene)
        self.position = QtWidgets.QHBoxLayout()
        self.position.setObjectName("position")
        self.position_label = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.position_label.sizePolicy().hasHeightForWidth())
        self.position_label.setSizePolicy(sizePolicy)
        self.position_label.setObjectName("position_label")
        self.position.addWidget(self.position_label)
        self.position_value = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.position_value.sizePolicy().hasHeightForWidth())
        self.position_value.setSizePolicy(sizePolicy)
        self.position_value.setObjectName("position_value")
        self.position.addWidget(self.position_value)
        self.InFoBoxMenu.addLayout(self.position)
        self.correlation = QtWidgets.QHBoxLayout()
        self.correlation.setObjectName("correlation")
        self.correlation_label = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.correlation_label.sizePolicy().hasHeightForWidth())
        self.correlation_label.setSizePolicy(sizePolicy)
        self.correlation_label.setObjectName("correlation_label")
        self.correlation.addWidget(self.correlation_label)
        self.correlation_value = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.correlation_value.sizePolicy().hasHeightForWidth())
        self.correlation_value.setSizePolicy(sizePolicy)
        self.correlation_value.setObjectName("correlation_value")
        self.correlation.addWidget(self.correlation_value)
        self.InFoBoxMenu.addLayout(self.correlation)
        self.power_one = QtWidgets.QHBoxLayout()
        self.power_one.setObjectName("power_one")
        self.power_one_label = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.power_one_label.sizePolicy().hasHeightForWidth())
        self.power_one_label.setSizePolicy(sizePolicy)
        self.power_one_label.setObjectName("power_one_label")
        self.power_one.addWidget(self.power_one_label)
        self.power_one_value = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.power_one_value.sizePolicy().hasHeightForWidth())
        self.power_one_value.setSizePolicy(sizePolicy)
        self.power_one_value.setObjectName("power_one_value")
        self.power_one.addWidget(self.power_one_value)
        self.InFoBoxMenu.addLayout(self.power_one)
        self.power_two = QtWidgets.QHBoxLayout()
        self.power_two.setObjectName("power_two")
        self.power_two_label = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.power_two_label.sizePolicy().hasHeightForWidth())
        self.power_two_label.setSizePolicy(sizePolicy)
        self.power_two_label.setObjectName("power_two_label")
        self.power_two.addWidget(self.power_two_label)
        self.power_two_value = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.power_two_value.sizePolicy().hasHeightForWidth())
        self.power_two_value.setSizePolicy(sizePolicy)
        self.power_two_value.setObjectName("power_two_value")
        self.power_two.addWidget(self.power_two_value)
        self.InFoBoxMenu.addLayout(self.power_two)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(189, 50, 1261, 531))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.CentralArea = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.CentralArea.setContentsMargins(0, 0, 0, 0)
        self.CentralArea.setObjectName("CentralArea")
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(640, 0, 121, 41))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.ScoreBox = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.ScoreBox.setContentsMargins(0, 0, 0, 0)
        self.ScoreBox.setObjectName("ScoreBox")
        self.score_label = QtWidgets.QLabel(self.layoutWidget4)
        self.score_label.setWordWrap(True)
        self.score_label.setObjectName("score_label")
        self.ScoreBox.addWidget(self.score_label)
        self.score_value = QtWidgets.QLabel(self.layoutWidget4)
        self.score_value.setWordWrap(True)
        self.score_value.setObjectName("score_value")
        self.ScoreBox.addWidget(self.score_value)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1212, 26))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.VisualsBox.setTitle(_translate("MainWindow", "Visuals"))
        self.scale_slider.setText(_translate("MainWindow", "Scale"))
        self.start_slider.setText(_translate("MainWindow", "Start"))
        self.end_slider.setText(_translate("MainWindow", "End"))
        self.flip_one_check.setText(_translate("MainWindow", "Flip Head 1"))
        self.flip_two_check.setText(_translate("MainWindow", "Flip Head 2"))
        self.font_size_slider.setText(_translate("MainWindow", "FontSize"))
        self.font_y_slider.setText(_translate("MainWindow", "FontY"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.SettingsBox.setTitle(_translate("MainWindow", "Settings"))
        self.show_gui_check.setText(_translate("MainWindow", "Show GUI (G)"))
        self.full_screen_check.setText(_translate("MainWindow", "Full Screen (F)"))
        self.select_screen_label.setText(_translate("MainWindow", "Select Screen"))
        self.select_screen_btn.setText(_translate("MainWindow", "1"))
        self.InfoBox.setTitle(_translate("MainWindow", "Info"))
        self.scene_label.setText(_translate("MainWindow", "Scene"))
        self.scene_value.setText(_translate("MainWindow", "0"))
        self.position_label.setText(_translate("MainWindow", "Position"))
        self.position_value.setText(_translate("MainWindow", "0"))
        self.correlation_label.setText(_translate("MainWindow", "Correlation"))
        self.correlation_value.setText(_translate("MainWindow", "0"))
        self.power_one_label.setText(_translate("MainWindow", "Power 1"))
        self.power_one_value.setText(_translate("MainWindow", "0"))
        self.power_two_label.setText(_translate("MainWindow", "Power 2"))
        self.power_two_value.setText(_translate("MainWindow", "0"))
        self.score_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Score:</span></p></body></html>"))
        self.score_value.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">0</span></p></body></html>"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))

