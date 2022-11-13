from maya import OpenMayaUI as omui 
from PySide2.QtCore import * 
from PySide2.QtGui import * 
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance 

import maya.cmds as cmds

# Get a reference to the main Maya application window
mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QWidget) 

class MyMayaWidget(QWidget):    
    def __init__(self, *args, **kwargs):        
        super(MyMayaWidget, self).__init__(*args, **kwargs)
        
        # Parent widget under Maya main window        
        self.setParent(mayaMainWindow)        
        self.setWindowFlags(Qt.Window)   
        
        # UI Window 
        self.setWindowTitle('Snowman Generator')        
        self.setGeometry(50, 50, 250, 150)
        
        #Widgets
        self.title_label = QLabel('Snowman Generator', self)
        self.title_label.move(5, 10)
        
        self.my_button = QPushButton('Build Snowman!', self)
        self.my_button.move(5,120)
        
        self.options_label = QLabel('Height:', self)
        self.options_label.move(5, 40)
        self.my_options = QComboBox(self)
        self.my_options.addItems(['Tall','Short'])
        self.my_options.move(45,37)
        
        self.my_checkbox = QCheckBox('Add Extra Features', self)
        self.my_checkbox.move(5,80)

        # On Click
        self.my_button.clicked.connect(self.button_onClicked)   
         
    def button_onClicked(self):
        self.build_snowman()
        print(self.my_options.currentText())
        
    def build_snowman(self):
        #Generate Body
        baseRad = 1.25
        coreRad = 1
        headRad = 0.75

        if(self.my_options.currentText() == 'Tall'):
            cmds.polySphere(r=baseRad, n=('bodyBase'))
            cmds.move(-1.7, y=True)
    
        cmds.polySphere(r=coreRad, n=('bodyCore'))
        
        cmds.polySphere(r=headRad, n=('bodyHead'))
        cmds.move(1.4, y=True)
        
        #Generate Hat
        brimRad = 0.7
        brimHeight = 0.1
        crownRad = 0.4
        crownHeight = 1
        
        cmds.polyCylinder(r=brimRad, h=brimHeight, n=('hatBrim'))
        cmds.move(2, y=True)
        
        cmds.polyCylinder(r=crownRad, h=crownHeight, n=('hatCrown'))
        cmds.move(2.5, y=True)
        
        if(self.my_checkbox.isChecked()):
            #Generate Buttons
            buttonRad = 0.1
            
            cmds.polySphere(r=buttonRad, n=('buttonLower'))
            cmds.move(0.95, z=True)
        
            cmds.polySphere(r=buttonRad, n=('buttonMiddle'))
            cmds.move(0, 0.25, 0.9)
        
            cmds.polySphere(r=buttonRad, n=('buttonUpper'))
            cmds.move(0, 0.5, 0.8)
        
            #Generate Face
            eyeRad = 0.1
            noseRad = 0.1
            noseHeight = 0.5
            
            cmds.polySphere(r=eyeRad, n=('eyeLeft'))
            cmds.move(0.25, 1.7, 0.6)
        
            cmds.polySphere(r=eyeRad, n=('eyeRight'))
            cmds.move(-0.25, 1.7, 0.6)
        
            cmds.polyCone(r=noseRad, h=noseHeight, n=('nose'))
            cmds.move(0, 1.5, 0.95)
            cmds.rotate('85deg', 0, 0)
           
my_widget = MyMayaWidget()     
my_widget.show()