# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\PROYECTOS_IH\trunk\Visor_WMS_QGIS\VisorWMS\libvisor\animation\Animation_menu.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_dockAnimationWidget(object):
    def setupUi(self, dockAnimationWidget):
        dockAnimationWidget.setObjectName(_fromUtf8("dockAnimationWidget"))
        dockAnimationWidget.resize(311, 749)
        dockAnimationWidget.setFloating(True)
        dockAnimationWidget.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        dockAnimationWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea|QtCore.Qt.TopDockWidgetArea)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setEnabled(True)
        self.dockWidgetContents.setMinimumSize(QtCore.QSize(265, 532))
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableLayerList = QtGui.QTableWidget(self.dockWidgetContents)
        self.tableLayerList.setEnabled(True)
        self.tableLayerList.setMaximumSize(QtCore.QSize(16777215, 100))
        self.tableLayerList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableLayerList.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableLayerList.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableLayerList.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tableLayerList.setObjectName(_fromUtf8("tableLayerList"))
        self.tableLayerList.setColumnCount(0)
        self.tableLayerList.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableLayerList)
        self.addWCSButton = QtGui.QPushButton(self.dockWidgetContents)
        self.addWCSButton.setObjectName(_fromUtf8("addWCSButton"))
        self.verticalLayout_2.addWidget(self.addWCSButton)
        self.addWMSButton = QtGui.QPushButton(self.dockWidgetContents)
        self.addWMSButton.setObjectName(_fromUtf8("addWMSButton"))
        self.verticalLayout_2.addWidget(self.addWMSButton)
        self.addOtherButton = QtGui.QPushButton(self.dockWidgetContents)
        self.addOtherButton.setObjectName(_fromUtf8("addOtherButton"))
        self.verticalLayout_2.addWidget(self.addOtherButton)
        self.removeButton = QtGui.QPushButton(self.dockWidgetContents)
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.verticalLayout_2.addWidget(self.removeButton)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.loopCheckbox = QtGui.QCheckBox(self.dockWidgetContents)
        self.loopCheckbox.setTristate(False)
        self.loopCheckbox.setObjectName(_fromUtf8("loopCheckbox"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.loopCheckbox)
        self.labelFrameRate = QtGui.QLabel(self.dockWidgetContents)
        self.labelFrameRate.setObjectName(_fromUtf8("labelFrameRate"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelFrameRate)
        self.cancelButton = QtGui.QPushButton(self.dockWidgetContents)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.cancelButton)
        self.progressBar = QtGui.QProgressBar(self.dockWidgetContents)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.progressBar)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtGui.QFormLayout.FieldRole, spacerItem)
        self.frameRateSpinbox = QtGui.QSpinBox(self.dockWidgetContents)
        self.frameRateSpinbox.setMinimum(150)
        self.frameRateSpinbox.setMaximum(10000)
        self.frameRateSpinbox.setSingleStep(50)
        self.frameRateSpinbox.setProperty("value", 500)
        self.frameRateSpinbox.setObjectName(_fromUtf8("frameRateSpinbox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.frameRateSpinbox)
        self.labelTimeFrame = QtGui.QLabel(self.dockWidgetContents)
        self.labelTimeFrame.setObjectName(_fromUtf8("labelTimeFrame"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.labelTimeFrame)
        self.buttonLoad = QtGui.QPushButton(self.dockWidgetContents)
        self.buttonLoad.setObjectName(_fromUtf8("buttonLoad"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.buttonLoad)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.daysFrameVariation = QtGui.QSpinBox(self.dockWidgetContents)
        self.daysFrameVariation.setMaximum(10000000)
        self.daysFrameVariation.setObjectName(_fromUtf8("daysFrameVariation"))
        self.horizontalLayout.addWidget(self.daysFrameVariation)
        self.timeFrameVariation = QtGui.QTimeEdit(self.dockWidgetContents)
        self.timeFrameVariation.setMinimumTime(QtCore.QTime(0, 0, 1))
        self.timeFrameVariation.setObjectName(_fromUtf8("timeFrameVariation"))
        self.horizontalLayout.addWidget(self.timeFrameVariation)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.daysTolerance = QtGui.QSpinBox(self.dockWidgetContents)
        self.daysTolerance.setMaximum(10000000)
        self.daysTolerance.setObjectName(_fromUtf8("daysTolerance"))
        self.horizontalLayout_2.addWidget(self.daysTolerance)
        self.timeTolerance = QtGui.QTimeEdit(self.dockWidgetContents)
        self.timeTolerance.setObjectName(_fromUtf8("timeTolerance"))
        self.horizontalLayout_2.addWidget(self.timeTolerance)
        self.formLayout.setLayout(4, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.labelInfo = QtGui.QLabel(self.dockWidgetContents)
        self.labelInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInfo.setObjectName(_fromUtf8("labelInfo"))
        self.verticalLayout_2.addWidget(self.labelInfo)
        self.animationSlider = QtGui.QSlider(self.dockWidgetContents)
        self.animationSlider.setMaximum(0)
        self.animationSlider.setSingleStep(0)
        self.animationSlider.setPageStep(0)
        self.animationSlider.setOrientation(QtCore.Qt.Horizontal)
        self.animationSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.animationSlider.setObjectName(_fromUtf8("animationSlider"))
        self.verticalLayout_2.addWidget(self.animationSlider)
        self.playButton = QtGui.QPushButton(self.dockWidgetContents)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.verticalLayout_2.addWidget(self.playButton)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        dockAnimationWidget.setWidget(self.dockWidgetContents)
        self.labelFrameRate.setBuddy(self.frameRateSpinbox)
        self.labelTimeFrame.setBuddy(self.daysFrameVariation)

        self.retranslateUi(dockAnimationWidget)
        QtCore.QMetaObject.connectSlotsByName(dockAnimationWidget)

    def retranslateUi(self, dockAnimationWidget):
        dockAnimationWidget.setWindowTitle(_translate("dockAnimationWidget", "THREDDS Animator", None))
        self.addWCSButton.setText(_translate("dockAnimationWidget", "Add WCS layer to animation...", None))
        self.addWMSButton.setText(_translate("dockAnimationWidget", "Add WMS layer to animation...", None))
        self.addOtherButton.setText(_translate("dockAnimationWidget", "Add external layer to animation...", None))
        self.removeButton.setText(_translate("dockAnimationWidget", "Remove selected layer", None))
        self.loopCheckbox.setText(_translate("dockAnimationWidget", "Loop animation", None))
        self.labelFrameRate.setToolTip(_translate("dockAnimationWidget", "Defines for how long will each frame be shown.\n"
"WARNING: If too low, some frames may be skipped due to rendering overload.", None))
        self.labelFrameRate.setText(_translate("dockAnimationWidget", "Frame update rate", None))
        self.cancelButton.setText(_translate("dockAnimationWidget", "Cancel", None))
        self.frameRateSpinbox.setToolTip(_translate("dockAnimationWidget", "Defines for how long will each frame be shown.\n"
"WARNING: If too low, some frames may be skipped due to rendering overload.", None))
        self.frameRateSpinbox.setSuffix(_translate("dockAnimationWidget", " ms", None))
        self.labelTimeFrame.setToolTip(_translate("dockAnimationWidget", "The (map) time which will pass in each frame of this animation.", None))
        self.labelTimeFrame.setText(_translate("dockAnimationWidget", "Time variation/frame", None))
        self.buttonLoad.setText(_translate("dockAnimationWidget", "Prepare animation", None))
        self.daysFrameVariation.setToolTip(_translate("dockAnimationWidget", "The (map) time which will pass in each frame of this animation.", None))
        self.daysFrameVariation.setSuffix(_translate("dockAnimationWidget", " days", None))
        self.timeFrameVariation.setToolTip(_translate("dockAnimationWidget", "The (map) time which will pass in each frame of this animation.", None))
        self.daysTolerance.setToolTip(_translate("dockAnimationWidget", "How much deviation is accepted between the expected time to be shown in the next frame and the actual time of the map shown.\n"
" Useful when mixing maps which have slightly different times.", None))
        self.daysTolerance.setSuffix(_translate("dockAnimationWidget", " days", None))
        self.timeTolerance.setToolTip(_translate("dockAnimationWidget", "How much deviation is accepted between the expected time to be shown in the next frame and the actual time of the map shown.\n"
" Useful when mixing maps which have slightly different times.", None))
        self.label.setToolTip(_translate("dockAnimationWidget", "How much deviation is accepted between the expected time to be shown in the next frame and the actual time of the map shown.\n"
" Useful when mixing maps which have slightly different times.", None))
        self.label.setText(_translate("dockAnimationWidget", "Max time offset", None))
        self.labelInfo.setText(_translate("dockAnimationWidget", "animation_info_label", None))
        self.playButton.setText(_translate("dockAnimationWidget", "Play", None))

