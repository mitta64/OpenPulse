# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Kula\Petrobras\OpenPulse\data\user_input\ui\Project\setProjectAttributesInput.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 490)
        Dialog.setMinimumSize(QtCore.QSize(650, 490))
        Dialog.setMaximumSize(QtCore.QSize(650, 490))
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 650, 490))
        self.frame.setMinimumSize(QtCore.QSize(650, 490))
        self.frame.setMaximumSize(QtCore.QSize(650, 490))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(34, 96, 200, 25))
        self.label_8.setMinimumSize(QtCore.QSize(200, 25))
        self.label_8.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 685, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(34, 60, 200, 25))
        self.label_2.setMinimumSize(QtCore.QSize(200, 25))
        self.label_2.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_current_project_name = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_current_project_name.setEnabled(False)
        self.lineEdit_current_project_name.setGeometry(QtCore.QRect(244, 60, 350, 25))
        self.lineEdit_current_project_name.setMinimumSize(QtCore.QSize(350, 25))
        self.lineEdit_current_project_name.setMaximumSize(QtCore.QSize(350, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit_current_project_name.setFont(font)
        self.lineEdit_current_project_name.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_current_project_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_current_project_name.setObjectName("lineEdit_current_project_name")
        self.lineEdit_current_project_folder = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_current_project_folder.setEnabled(False)
        self.lineEdit_current_project_folder.setGeometry(QtCore.QRect(244, 96, 350, 25))
        self.lineEdit_current_project_folder.setMinimumSize(QtCore.QSize(350, 25))
        self.lineEdit_current_project_folder.setMaximumSize(QtCore.QSize(350, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lineEdit_current_project_folder.setFont(font)
        self.lineEdit_current_project_folder.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_current_project_folder.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_current_project_folder.setObjectName("lineEdit_current_project_folder")
        self.toolButton_search_project_folder = QtWidgets.QToolButton(self.frame)
        self.toolButton_search_project_folder.setGeometry(QtCore.QRect(556, 390, 75, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_search_project_folder.sizePolicy().hasHeightForWidth())
        self.toolButton_search_project_folder.setSizePolicy(sizePolicy)
        self.toolButton_search_project_folder.setMinimumSize(QtCore.QSize(75, 25))
        self.toolButton_search_project_folder.setMaximumSize(QtCore.QSize(75, 25))
        self.toolButton_search_project_folder.setSizeIncrement(QtCore.QSize(0, 1))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.toolButton_search_project_folder.setFont(font)
        self.toolButton_search_project_folder.setObjectName("toolButton_search_project_folder")
        self.lineEdit_new_project_name = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_new_project_name.setEnabled(True)
        self.lineEdit_new_project_name.setGeometry(QtCore.QRect(198, 350, 350, 25))
        self.lineEdit_new_project_name.setMinimumSize(QtCore.QSize(350, 25))
        self.lineEdit_new_project_name.setMaximumSize(QtCore.QSize(350, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit_new_project_name.setFont(font)
        self.lineEdit_new_project_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 255);")
        self.lineEdit_new_project_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_new_project_name.setObjectName("lineEdit_new_project_name")
        self.lineEdit_new_project_folder = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_new_project_folder.setEnabled(True)
        self.lineEdit_new_project_folder.setGeometry(QtCore.QRect(198, 390, 350, 25))
        self.lineEdit_new_project_folder.setMinimumSize(QtCore.QSize(350, 25))
        self.lineEdit_new_project_folder.setMaximumSize(QtCore.QSize(350, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lineEdit_new_project_folder.setFont(font)
        self.lineEdit_new_project_folder.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 255);")
        self.lineEdit_new_project_folder.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_new_project_folder.setObjectName("lineEdit_new_project_folder")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 350, 180, 25))
        self.label_3.setMinimumSize(QtCore.QSize(180, 25))
        self.label_3.setMaximumSize(QtCore.QSize(180, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(10, 390, 180, 25))
        self.label_9.setMinimumSize(QtCore.QSize(180, 25))
        self.label_9.setMaximumSize(QtCore.QSize(180, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.toolButton_clean_project_name = QtWidgets.QToolButton(self.frame)
        self.toolButton_clean_project_name.setGeometry(QtCore.QRect(556, 350, 75, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_clean_project_name.sizePolicy().hasHeightForWidth())
        self.toolButton_clean_project_name.setSizePolicy(sizePolicy)
        self.toolButton_clean_project_name.setMinimumSize(QtCore.QSize(75, 25))
        self.toolButton_clean_project_name.setMaximumSize(QtCore.QSize(75, 25))
        self.toolButton_clean_project_name.setSizeIncrement(QtCore.QSize(0, 1))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.toolButton_clean_project_name.setFont(font)
        self.toolButton_clean_project_name.setObjectName("toolButton_clean_project_name")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 132, 650, 192))
        self.frame_2.setMinimumSize(QtCore.QSize(650, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(650, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(74, 16, 500, 75))
        self.frame_3.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.radioButton_projectName = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_projectName.setGeometry(QtCore.QRect(38, 38, 80, 25))
        self.radioButton_projectName.setMinimumSize(QtCore.QSize(80, 25))
        self.radioButton_projectName.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_projectName.setFont(font)
        self.radioButton_projectName.setIconSize(QtCore.QSize(30, 30))
        self.radioButton_projectName.setChecked(True)
        self.radioButton_projectName.setObjectName("radioButton_projectName")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_projectName)
        self.radioButton_projectDirectory = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_projectDirectory.setGeometry(QtCore.QRect(146, 38, 100, 25))
        self.radioButton_projectDirectory.setMinimumSize(QtCore.QSize(100, 25))
        self.radioButton_projectDirectory.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_projectDirectory.setFont(font)
        self.radioButton_projectDirectory.setObjectName("radioButton_projectDirectory")
        self.buttonGroup_2.addButton(self.radioButton_projectDirectory)
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setEnabled(True)
        self.label_11.setGeometry(QtCore.QRect(0, 0, 500, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(500, 30))
        self.label_11.setMaximumSize(QtCore.QSize(500, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setFrameShape(QtWidgets.QFrame.Box)
        self.label_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_11.setTextFormat(QtCore.Qt.AutoText)
        self.label_11.setScaledContents(False)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setWordWrap(False)
        self.label_11.setIndent(0)
        self.label_11.setObjectName("label_11")
        self.radioButton_projectNameDirectory = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_projectNameDirectory.setGeometry(QtCore.QRect(294, 38, 180, 25))
        self.radioButton_projectNameDirectory.setMinimumSize(QtCore.QSize(180, 25))
        self.radioButton_projectNameDirectory.setMaximumSize(QtCore.QSize(180, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_projectNameDirectory.setFont(font)
        self.radioButton_projectNameDirectory.setObjectName("radioButton_projectNameDirectory")
        self.buttonGroup_2.addButton(self.radioButton_projectNameDirectory)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(74, 102, 500, 75))
        self.frame_4.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")
        self.radioButton_maintain_current_project_folder = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_maintain_current_project_folder.setGeometry(QtCore.QRect(122, 38, 80, 25))
        self.radioButton_maintain_current_project_folder.setMinimumSize(QtCore.QSize(80, 25))
        self.radioButton_maintain_current_project_folder.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_maintain_current_project_folder.setFont(font)
        self.radioButton_maintain_current_project_folder.setIconSize(QtCore.QSize(30, 30))
        self.radioButton_maintain_current_project_folder.setChecked(True)
        self.radioButton_maintain_current_project_folder.setObjectName("radioButton_maintain_current_project_folder")
        self.buttonGroup = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_maintain_current_project_folder)
        self.radioButton_remove_current_project_folder = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_remove_current_project_folder.setGeometry(QtCore.QRect(312, 38, 80, 25))
        self.radioButton_remove_current_project_folder.setMinimumSize(QtCore.QSize(80, 25))
        self.radioButton_remove_current_project_folder.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_remove_current_project_folder.setFont(font)
        self.radioButton_remove_current_project_folder.setObjectName("radioButton_remove_current_project_folder")
        self.buttonGroup.addButton(self.radioButton_remove_current_project_folder)
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        self.label_12.setEnabled(True)
        self.label_12.setGeometry(QtCore.QRect(0, 0, 500, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(500, 30))
        self.label_12.setMaximumSize(QtCore.QSize(500, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setFrameShape(QtWidgets.QFrame.Box)
        self.label_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_12.setTextFormat(QtCore.Qt.AutoText)
        self.label_12.setScaledContents(False)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setWordWrap(False)
        self.label_12.setIndent(0)
        self.label_12.setObjectName("label_12")
        self.pushButton_cancel = QtWidgets.QPushButton(self.frame)
        self.pushButton_cancel.setGeometry(QtCore.QRect(184, 438, 120, 30))
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(120, 30))
        self.pushButton_cancel.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_confirm = QtWidgets.QPushButton(self.frame)
        self.pushButton_confirm.setGeometry(QtCore.QRect(350, 438, 120, 30))
        self.pushButton_confirm.setMinimumSize(QtCore.QSize(120, 30))
        self.pushButton_confirm.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_confirm.setFont(font)
        self.pushButton_confirm.setObjectName("pushButton_confirm")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Set Project Attributes"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">Current project directory:</p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Modify the Project attributes</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">Current project name:</p></body></html>"))
        self.toolButton_search_project_folder.setText(_translate("Dialog", "Search"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">New project name:</p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">New project directory:</p></body></html>"))
        self.toolButton_clean_project_name.setText(_translate("Dialog", "Clean"))
        self.radioButton_projectName.setText(_translate("Dialog", "Name"))
        self.radioButton_projectDirectory.setText(_translate("Dialog", "Directory"))
        self.label_11.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Modify the following Project attributes</p></body></html>"))
        self.radioButton_projectNameDirectory.setText(_translate("Dialog", "Name and Directory"))
        self.radioButton_maintain_current_project_folder.setText(_translate("Dialog", "Yes"))
        self.radioButton_remove_current_project_folder.setText(_translate("Dialog", "No"))
        self.label_12.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Do you want to maintain the current project in the computer?</p></body></html>"))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel"))
        self.pushButton_confirm.setText(_translate("Dialog", "Confirm"))
