# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Kula\Petrobras\OpenPulse\data\user_input\ui\Model\Setup\Structural\stressStiffeningInput.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(400, 482)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(400, 482))
        Dialog.setMaximumSize(QtCore.QSize(400, 482))
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Dialog.setWhatsThis("")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 47))
        self.frame.setMinimumSize(QtCore.QSize(400, 0))
        self.frame.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 6, 340, 35))
        self.label_6.setMinimumSize(QtCore.QSize(340, 35))
        self.label_6.setMaximumSize(QtCore.QSize(340, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.frame_4 = QtWidgets.QFrame(Dialog)
        self.frame_4.setGeometry(QtCore.QRect(0, 122, 400, 360))
        self.frame_4.setMinimumSize(QtCore.QSize(400, 360))
        self.frame_4.setMaximumSize(QtCore.QSize(400, 360))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.tabWidget_stress_stiffening = QtWidgets.QTabWidget(self.frame_4)
        self.tabWidget_stress_stiffening.setGeometry(QtCore.QRect(6, 50, 391, 299))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.tabWidget_stress_stiffening.setFont(font)
        self.tabWidget_stress_stiffening.setObjectName("tabWidget_stress_stiffening")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_confirm = QtWidgets.QPushButton(self.tab)
        self.pushButton_confirm.setGeometry(QtCore.QRect(134, 214, 120, 32))
        self.pushButton_confirm.setMinimumSize(QtCore.QSize(120, 32))
        self.pushButton_confirm.setMaximumSize(QtCore.QSize(120, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_confirm.setFont(font)
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setGeometry(QtCore.QRect(326, 156, 43, 30))
        self.label_18.setMinimumSize(QtCore.QSize(0, 30))
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.lineEdit_external_pressure = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_external_pressure.setGeometry(QtCore.QRect(192, 92, 130, 30))
        self.lineEdit_external_pressure.setMinimumSize(QtCore.QSize(130, 30))
        self.lineEdit_external_pressure.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit_external_pressure.setFont(font)
        self.lineEdit_external_pressure.setText("")
        self.lineEdit_external_pressure.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_external_pressure.setObjectName("lineEdit_external_pressure")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(328, 92, 43, 30))
        self.label_17.setMinimumSize(QtCore.QSize(0, 30))
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_26 = QtWidgets.QLabel(self.tab)
        self.label_26.setGeometry(QtCore.QRect(8, 156, 175, 30))
        self.label_26.setMinimumSize(QtCore.QSize(0, 30))
        self.label_26.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label_25 = QtWidgets.QLabel(self.tab)
        self.label_25.setGeometry(QtCore.QRect(10, 92, 175, 30))
        self.label_25.setMinimumSize(QtCore.QSize(0, 30))
        self.label_25.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.lineEdit_internal_pressure = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_internal_pressure.setGeometry(QtCore.QRect(190, 156, 130, 30))
        self.lineEdit_internal_pressure.setMinimumSize(QtCore.QSize(130, 30))
        self.lineEdit_internal_pressure.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit_internal_pressure.setFont(font)
        self.lineEdit_internal_pressure.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_internal_pressure.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_internal_pressure.setObjectName("lineEdit_internal_pressure")
        self.label_27 = QtWidgets.QLabel(self.tab)
        self.label_27.setGeometry(QtCore.QRect(34, 22, 320, 40))
        self.label_27.setMinimumSize(QtCore.QSize(320, 40))
        self.label_27.setMaximumSize(QtCore.QSize(320, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setFrameShape(QtWidgets.QFrame.Box)
        self.label_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.tabWidget_stress_stiffening.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_29 = QtWidgets.QLabel(self.tab_2)
        self.label_29.setGeometry(QtCore.QRect(11, 10, 362, 33))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setFrameShape(QtWidgets.QFrame.Box)
        self.label_29.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_29.setTextFormat(QtCore.Qt.AutoText)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.pushButton_close = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_close.setGeometry(QtCore.QRect(134, 350, 120, 32))
        self.pushButton_close.setMinimumSize(QtCore.QSize(120, 32))
        self.pushButton_close.setMaximumSize(QtCore.QSize(120, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setStyleSheet("")
        self.pushButton_close.setObjectName("pushButton_close")
        self.tabWidget = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget.setGeometry(QtCore.QRect(8, 56, 367, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_lines = QtWidgets.QWidget()
        self.tab_lines.setObjectName("tab_lines")
        self.pushButton_get_information_line = QtWidgets.QPushButton(self.tab_lines)
        self.pushButton_get_information_line.setGeometry(QtCore.QRect(264, 132, 90, 30))
        self.pushButton_get_information_line.setMinimumSize(QtCore.QSize(90, 29))
        self.pushButton_get_information_line.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_get_information_line.setFont(font)
        self.pushButton_get_information_line.setObjectName("pushButton_get_information_line")
        self.pushButton_remove_line = QtWidgets.QPushButton(self.tab_lines)
        self.pushButton_remove_line.setGeometry(QtCore.QRect(188, 132, 75, 30))
        self.pushButton_remove_line.setMinimumSize(QtCore.QSize(0, 27))
        self.pushButton_remove_line.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_remove_line.setFont(font)
        self.pushButton_remove_line.setObjectName("pushButton_remove_line")
        self.treeWidget_stress_stiffening_lines = QtWidgets.QTreeWidget(self.tab_lines)
        self.treeWidget_stress_stiffening_lines.setGeometry(QtCore.QRect(6, 6, 352, 159))
        self.treeWidget_stress_stiffening_lines.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget_stress_stiffening_lines.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.treeWidget_stress_stiffening_lines.setFont(font)
        self.treeWidget_stress_stiffening_lines.setIndentation(0)
        self.treeWidget_stress_stiffening_lines.setObjectName("treeWidget_stress_stiffening_lines")
        self.treeWidget_stress_stiffening_lines.raise_()
        self.pushButton_get_information_line.raise_()
        self.pushButton_remove_line.raise_()
        self.tabWidget.addTab(self.tab_lines, "")
        self.tab_elements = QtWidgets.QWidget()
        self.tab_elements.setObjectName("tab_elements")
        self.pushButton_remove_elem = QtWidgets.QPushButton(self.tab_elements)
        self.pushButton_remove_elem.setGeometry(QtCore.QRect(188, 132, 75, 30))
        self.pushButton_remove_elem.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_remove_elem.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_remove_elem.setFont(font)
        self.pushButton_remove_elem.setObjectName("pushButton_remove_elem")
        self.treeWidget_stress_stiffening_elements = QtWidgets.QTreeWidget(self.tab_elements)
        self.treeWidget_stress_stiffening_elements.setGeometry(QtCore.QRect(6, 6, 352, 159))
        self.treeWidget_stress_stiffening_elements.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget_stress_stiffening_elements.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.treeWidget_stress_stiffening_elements.setFont(font)
        self.treeWidget_stress_stiffening_elements.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.treeWidget_stress_stiffening_elements.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.treeWidget_stress_stiffening_elements.setIndentation(0)
        self.treeWidget_stress_stiffening_elements.setObjectName("treeWidget_stress_stiffening_elements")
        self.pushButton_get_information_elem = QtWidgets.QPushButton(self.tab_elements)
        self.pushButton_get_information_elem.setGeometry(QtCore.QRect(264, 132, 90, 30))
        self.pushButton_get_information_elem.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton_get_information_elem.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_get_information_elem.setFont(font)
        self.pushButton_get_information_elem.setObjectName("pushButton_get_information_elem")
        self.treeWidget_stress_stiffening_elements.raise_()
        self.pushButton_get_information_elem.raise_()
        self.pushButton_remove_elem.raise_()
        self.tabWidget.addTab(self.tab_elements, "")
        self.tabWidget_stress_stiffening.addTab(self.tab_2, "")
        self.pushButton_reset = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_reset.setGeometry(QtCore.QRect(304, 48, 90, 26))
        self.pushButton_reset.setMinimumSize(QtCore.QSize(90, 26))
        self.pushButton_reset.setMaximumSize(QtCore.QSize(90, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_reset.setFont(font)
        self.pushButton_reset.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.lineEdit_id_labels = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_id_labels.setEnabled(False)
        self.lineEdit_id_labels.setGeometry(QtCore.QRect(18, 12, 110, 26))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.lineEdit_id_labels.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit_id_labels.setFont(font)
        self.lineEdit_id_labels.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_id_labels.setAutoFillBackground(False)
        self.lineEdit_id_labels.setFrame(False)
        self.lineEdit_id_labels.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_id_labels.setObjectName("lineEdit_id_labels")
        self.lineEdit_selected_ID = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_selected_ID.setEnabled(False)
        self.lineEdit_selected_ID.setGeometry(QtCore.QRect(130, 12, 249, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit_selected_ID.setFont(font)
        self.lineEdit_selected_ID.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_selected_ID.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_selected_ID.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_selected_ID.setObjectName("lineEdit_selected_ID")
        self.frame_10 = QtWidgets.QFrame(Dialog)
        self.frame_10.setGeometry(QtCore.QRect(0, 46, 400, 77))
        self.frame_10.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_10.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_10.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_10.setLineWidth(1)
        self.frame_10.setObjectName("frame_10")
        self.label_3 = QtWidgets.QLabel(self.frame_10)
        self.label_3.setGeometry(QtCore.QRect(16, 8, 185, 30))
        self.label_3.setMinimumSize(QtCore.QSize(185, 30))
        self.label_3.setMaximumSize(QtCore.QSize(185, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_10)
        self.label_4.setGeometry(QtCore.QRect(16, 38, 185, 30))
        self.label_4.setMinimumSize(QtCore.QSize(185, 30))
        self.label_4.setMaximumSize(QtCore.QSize(185, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.radioButton_selected_elements = QtWidgets.QRadioButton(self.frame_10)
        self.radioButton_selected_elements.setGeometry(QtCore.QRect(234, 54, 180, 17))
        self.radioButton_selected_elements.setMinimumSize(QtCore.QSize(180, 17))
        self.radioButton_selected_elements.setMaximumSize(QtCore.QSize(180, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.radioButton_selected_elements.setFont(font)
        self.radioButton_selected_elements.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.radioButton_selected_elements.setChecked(False)
        self.radioButton_selected_elements.setObjectName("radioButton_selected_elements")
        self.radioButton_selected_lines = QtWidgets.QRadioButton(self.frame_10)
        self.radioButton_selected_lines.setGeometry(QtCore.QRect(234, 30, 180, 17))
        self.radioButton_selected_lines.setMinimumSize(QtCore.QSize(180, 17))
        self.radioButton_selected_lines.setMaximumSize(QtCore.QSize(180, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.radioButton_selected_lines.setFont(font)
        self.radioButton_selected_lines.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.radioButton_selected_lines.setChecked(False)
        self.radioButton_selected_lines.setObjectName("radioButton_selected_lines")
        self.radioButton_all_lines = QtWidgets.QRadioButton(self.frame_10)
        self.radioButton_all_lines.setGeometry(QtCore.QRect(234, 6, 180, 17))
        self.radioButton_all_lines.setMinimumSize(QtCore.QSize(180, 17))
        self.radioButton_all_lines.setMaximumSize(QtCore.QSize(180, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.radioButton_all_lines.setFont(font)
        self.radioButton_all_lines.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.radioButton_all_lines.setChecked(True)
        self.radioButton_all_lines.setObjectName("radioButton_all_lines")

        self.retranslateUi(Dialog)
        self.tabWidget_stress_stiffening.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", " Set: stress stiffening"))
        self.label_6.setText(_translate("Dialog", "STRESS STIFFENING SETUP"))
        self.pushButton_confirm.setText(_translate("Dialog", "Confirm"))
        self.label_18.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">[Pa]</span></p></body></html>"))
        self.label_17.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">[Pa]</span></p></body></html>"))
        self.label_26.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">Internal pressure:</p></body></html>"))
        self.label_25.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">External pressure:</p></body></html>"))
        self.label_27.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Stress stiffening parameters:</p></body></html>"))
        self.tabWidget_stress_stiffening.setTabText(self.tabWidget_stress_stiffening.indexOf(self.tab), _translate("Dialog", "Model"))
        self.label_29.setText(_translate("Dialog", "Get more info or remove a selected group:"))
        self.pushButton_close.setText(_translate("Dialog", "Close"))
        self.pushButton_get_information_line.setText(_translate("Dialog", "See details"))
        self.pushButton_remove_line.setText(_translate("Dialog", "Remove"))
        self.treeWidget_stress_stiffening_lines.headerItem().setText(0, _translate("Dialog", "Group"))
        self.treeWidget_stress_stiffening_lines.headerItem().setText(1, _translate("Dialog", "Lines"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_lines), _translate("Dialog", "Group of lines"))
        self.pushButton_remove_elem.setText(_translate("Dialog", "Remove"))
        self.treeWidget_stress_stiffening_elements.headerItem().setText(0, _translate("Dialog", "Group"))
        self.treeWidget_stress_stiffening_elements.headerItem().setText(1, _translate("Dialog", "Elements"))
        self.pushButton_get_information_elem.setText(_translate("Dialog", "See details"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_elements), _translate("Dialog", "Group of elements"))
        self.tabWidget_stress_stiffening.setTabText(self.tabWidget_stress_stiffening.indexOf(self.tab_2), _translate("Dialog", "Remove"))
        self.pushButton_reset.setText(_translate("Dialog", "Reset all"))
        self.lineEdit_id_labels.setText(_translate("Dialog", "Selected ID"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Activate stiffening</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">effect to:</span></p></body></html>"))
        self.radioButton_selected_elements.setText(_translate("Dialog", "Selected elements"))
        self.radioButton_selected_lines.setText(_translate("Dialog", "Selected lines"))
        self.radioButton_all_lines.setText(_translate("Dialog", "All lines"))
