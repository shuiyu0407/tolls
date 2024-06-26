
import sys
from PyQt5.QtGui import QIcon , QPixmap
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtWidgets import (QLineEdit,QMessageBox,QHBoxLayout,QPushButton, QLabel , QApplication, QWidget, QComboBox, QVBoxLayout, QShortcut)
import os
import subprocess
import platform
import configparser

#读取config.ini文件
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

class Window1(QWidget):
    def __init__(self):
        super().__init__()
        self.tolls()
    def tolls(self):
        
        #ui显示动画
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)

        folder_path = 'png'

        # 检测文件夹是否存在
        if os.path.exists(folder_path):

         self.setWindowTitle('tools box')
        
         # 创建一个布局
         layout = QVBoxLayout()
        
         # 设置窗口的大小
         self.resize(320, 100)  # 宽度400像素，高度300像素
        
         # 设置窗口图标
         pixmap = QPixmap('png/logo.jpg')  # 确保图标文件路径正确
         icon = QIcon(pixmap)
         self.setWindowIcon(icon)
        
         label = QLabel('tolls box')
         layout.addWidget(label)
        
         # 指定你想要检查和创建的文件夹路径
         folder_path = 'tools'
        
         # 检查文件夹是否存在
         if not os.path.exists(folder_path):
                 os.makedirs(folder_path)
        
        
         # 创建第一个下拉框
         comboBox = QComboBox(self)
         layout.addWidget(comboBox)
        
         # 创建第二个下拉框
         comboBox1 = QComboBox(self)
         layout.addWidget(comboBox1)
        
         # 创建第三个下拉框
         comboBox2 = QComboBox(self)
         layout.addWidget(comboBox2)
        
         # 填充第一个下拉框
         for entry in os.listdir('tools'):
             if os.path.isdir(os.path.join('tools', entry)):
                 comboBox.addItem(entry)
        
         def updateComboBox1(index):
             selected_folder = comboBox.currentText()
             subfolder_path = os.path.join('tools', selected_folder)
             comboBox1.clear()
             for entry in os.listdir(subfolder_path):
                 if os.path.isdir(os.path.join(subfolder_path, entry)):
                     comboBox1.addItem(entry)
        
        
         def updateComboBox2(index):
             selected_subfolder = comboBox1.currentText()
             subfolder_path = os.path.join('tools', comboBox.currentText(), selected_subfolder)
             comboBox2.clear()
             for entry in os.listdir(subfolder_path):
                 if entry.lower().endswith(('.exe','.bat')):
                     comboBox2.addItem(entry)

 
         def chuder():
           try:
            # 指定要启动的.exe文件的路径
            exe_path = os.path.join('tools', comboBox.currentText(), comboBox1.currentText(), comboBox2.currentText())
            process = subprocess.Popen(exe_path, shell=True)
           except:
            ts = QMessageBox()
            ts.setIcon(QMessageBox.Critical)
            ts.setText("程序启动失败，请检查软件是否是可运行的exe/bat")
            ts.setWindowTitle("error")
            ts.setStandardButtons(QMessageBox.Ok)
         
         
         # 连接第一个下拉框的 currentIndexChanged 信号到槽函数
         comboBox.currentIndexChanged.connect(updateComboBox1)
     
         # 连接第二个下拉框的 currentIndexChanged 信号到槽函数
         comboBox1.currentIndexChanged.connect(updateComboBox2)
     
         # 创建一个按钮
         button = QPushButton('启动程序', self)
         layout.addWidget(button)
     
         button.clicked.connect(chuder)
     
         # 设置窗口的布局
         self.setLayout(layout)
         
         
        else:
         msg2 = QMessageBox()
         msg2.setIcon(QMessageBox.Information)
         msg2.setText("png 文件夹不存在，这是一个致命的错误")
         msg2.setWindowTitle("window")
         msg2.setStandardButtons(QMessageBox.Ok)

class Window2(QWidget):
    def __init__(self):
        super().__init__()
        self.tolls()
    def tolls(self):
         
        #ui显示动画
         self.animation = QPropertyAnimation(self, b"windowOpacity")
         self.animation.setDuration(1000)
         self.animation.setStartValue(0)
         self.animation.setEndValue(1)

         self.setWindowTitle('Simple tools in the system')

         # 创建一个布局
         layout = QVBoxLayout()
        
         # 设置窗口的大小
         self.resize(320, 100)  # 宽度400像素，高度300像素
        
         # 设置窗口图标
         pixmap = QPixmap('png/logo.jpg')  # 确保图标文件路径正确
         icon = QIcon(pixmap)
         self.setWindowIcon(icon)
         
         #读取“基本配置”节，读取text1建的文本设置为变量text1
         text1 = config.get('set', 'text1')
         self.label = QLabel(text1)
         layout.addWidget(self.label)
         
         text2 = config.get('set', 'text2')
         self.label1 = QLabel(text2)
         layout.addWidget(self.label1)
         
         def open_window2():
           window.show()  # 显示Window
         # 创建一个按钮
         butto1n = QPushButton('打开系统工具集', self)
         layout.addWidget(butto1n)
         butto1n.clicked.connect(open_window2)
         
        #github
         def open_github():
             os.startfile('https://github.com/shuiyu0407/tolls')
         buttonc = QPushButton('github')
         icon = QIcon('png\GitHub-Simbolo.png') 
         buttonc.setIcon(icon)
         buttonc.clicked.connect(open_github)
        
         #i
         def open_i():
             set.show()
         buttoni = QPushButton('set')
         icon = QIcon('png\R-C.png') 
         buttoni.setIcon(icon)
         buttoni.clicked.connect(open_i)
         
         #window
         def open_window():
             try:
              msg1 = QMessageBox()
              msg1.setIcon(QMessageBox.Information)
              # 获取CPU信息
              cpu_info = platform.processor()
              # 获取内存信息
              memory_info = platform.machine()
              # 获取系统架构
              system_arch = platform.system()
              
              # 获取系统版本
              system_version = platform.version()
              msg1.setText(f"CPU: {cpu_info}\n内存: {memory_info}\n系统: {system_arch}\nSystem Version: {system_version}")
              msg1.setWindowTitle("window")
              msg1.setStandardButtons(QMessageBox.Ok)
              msg1.exec_()

             except:
              ts = QMessageBox()
              ts.setIcon(QMessageBox.Critical)
              ts.setText("获取系统信息失败，请检查你的系统是否是win10及以上")
              ts.setWindowTitle("error")
              ts.setStandardButtons(QMessageBox.Ok)
         buttonw = QPushButton('window')
         icon = QIcon('png\window.png') 
         buttonw.setIcon(icon)
         buttonw.clicked.connect(open_window)
         # 创建一个水平布局并添加两个按钮
         horizontalLayout = QHBoxLayout()
         horizontalLayout.addWidget(buttonc)
         horizontalLayout.addWidget(buttoni)
         horizontalLayout.addWidget(buttonw)

          # 将水平布局添加到主布局中
         layout.addLayout(horizontalLayout)
         # 设置窗口的布局
         self.setLayout(layout)

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox
from PyQt5.QtGui import QPixmap, QIcon

class window3(QWidget):
    def __init__(self):
        super().__init__()
        self.tolls()

    def tolls(self):
        # 创建布局和窗口
        self.setWindowTitle('tools box')

        # 创建一个布局
        layout = QVBoxLayout()

        # 设置窗口的大小
        self.resize(320, 100)  # 宽度400像素，高度300像素

        # 设置窗口图标
        pixmap = QPixmap('png/logo.jpg')  # 确保图标文件路径正确
        icon = QIcon(pixmap)
        self.setWindowIcon(icon)
        
        #创建一个水平布局
        horizontalLayout = QHBoxLayout()

        #创建一个文本
        label = QLabel('使用工具箱')
        horizontalLayout.addWidget(label)
        
        #创建一个输入框
        self.lineEdit = QLineEdit()
        horizontalLayout.addWidget(self.lineEdit)
        def search():
            #获取输入框的内容
            text = self.lineEdit.text()
            #写入config.ini文件
            try:
                #检测config.ini文件第一行内容,讲内容设置为变量cerf
                with open('config.ini', 'r') as f:
                    cerf = f.readline()
                
                #下载cerf地址文件到tools文件夹
                subprocess.Popen(f'curl -o tools/cerf.zip {cerf}', shell=True)

                #解压cerf.zip文件到tools文件夹,不使用unzip

                subprocess.Popen(f'7z x tools/cerf.zip -o"tools"', shell=True)
                      
                #提示下载成功
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("下载成功，请重新打开工具箱")
                msg.setWindowTitle("window")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                #关闭窗口
                self.close()
            except:
                #提示下载失败
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("下载失败，请检查网络连接/地址")
                msg.setWindowTitle("error")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

                
        #添加确定按钮
        button = QPushButton('确定')
        horizontalLayout.addWidget(button)
        button.clicked.connect(search)

        #把水平布局添加
        layout.addLayout(horizontalLayout)
 
        
        
        # 设置窗口的布局
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建QApplication实例
    window = Window1()
    windows = Window2()
    set = window3()
    windows.show()  # 显示Windows
    sys.exit(app.exec_())  # 进入事件循环
