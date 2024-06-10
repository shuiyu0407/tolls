
import sys
from PyQt5.QtGui import QIcon , QPixmap
from PyQt5.QtWidgets import (QMessageBox,QHBoxLayout,QPushButton, QLabel , QApplication, QWidget, QComboBox, QVBoxLayout)
import os
import subprocess
import platform

folder_path = 'png'

# 检测文件夹是否存在
if os.path.exists(folder_path):
 # 创建一个应用程序实例
 app = QApplication(sys.argv)
 
 # 创建1个窗口
 window = QWidget()
 window.setWindowTitle('tools box')
 
 # 创建一个布局
 layout = QVBoxLayout()
 
 # 设置窗口的大小
 window.resize(320, 100)  # 宽度400像素，高度300像素
 
 # 设置窗口图标
 pixmap = QPixmap('png/logo.jpg')  # 确保图标文件路径正确
 icon = QIcon(pixmap)
 window.setWindowIcon(icon)
 
 label = QLabel('tolls box')
 layout.addWidget(label)
 
 # 指定你想要检查和创建的文件夹路径
 folder_path = 'tools'
 
 # 检查文件夹是否存在
 if not os.path.exists(folder_path):
         os.makedirs(folder_path)
 
 
 # 创建第一个下拉框
 comboBox = QComboBox(window)
 layout.addWidget(comboBox)
 
 # 创建第二个下拉框
 comboBox1 = QComboBox(window)
 layout.addWidget(comboBox1)
 
 # 创建第三个下拉框
 comboBox2 = QComboBox(window)
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
 button = QPushButton('启动程序', window)
 layout.addWidget(button)
 
 button.clicked.connect(chuder)
 
 
 #github
 def open_github():
     os.startfile('https://github.com/shuiyu0407/tolls')
 buttonc = QPushButton('github')
 icon = QIcon('png\GitHub-Simbolo.png') 
 buttonc.setIcon(icon)
 buttonc.clicked.connect(open_github)
 
 #i
 def open_i():
     msg = QMessageBox()
     msg.setIcon(QMessageBox.Information)
     msg.setText("我们不提供服务，只是帮助一些作者整合工具")
     msg.setWindowTitle("i")
     msg.setStandardButtons(QMessageBox.Ok)
     msg.exec_()
 buttoni = QPushButton('')
 icon = QIcon('png\R-C.png') 
 buttoni.setIcon(icon)
 buttoni.clicked.connect(open_i)
 
 #window
 def open_window():
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
 window.setLayout(layout)
 
 # 显示窗口
 window.show()
 
 #Pyqt循环
 sys.exit(app.exec_())
else:
     msg2 = QMessageBox()
     msg2.setIcon(QMessageBox.Information)
     msg2.setText("png 文件夹不存在，这是一个致命的错误")
     msg2.setWindowTitle("window")
     msg2.setStandardButtons(QMessageBox.Ok)
