import sys
from PyQt5.QtWidgets import  QPushButton,  QLabel , QApplication, QWidget, QComboBox, QVBoxLayout
import os
import subprocess

# 创建一个应用程序实例
app = QApplication(sys.argv)

# 创建一个窗口
window = QWidget()
window.setWindowTitle('window tolls box')

# 创建一个垂直布局
layout = QVBoxLayout()

# 设置窗口的大小
window.resize(320, 100)  # 宽度400像素，高度300像素

label = QLabel('tolls box')
layout.addWidget(label)

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
 # 指定要启动的.exe文件的路径
 exe_path = os.path.join('tools', comboBox.currentText(), comboBox1.currentText(), comboBox2.currentText())
 process = subprocess.Popen(exe_path, shell=True)

# 连接第一个下拉框的 currentIndexChanged 信号到槽函数
comboBox.currentIndexChanged.connect(updateComboBox1)

# 连接第二个下拉框的 currentIndexChanged 信号到槽函数
comboBox1.currentIndexChanged.connect(updateComboBox2)

# 创建一个按钮
button = QPushButton('start', window)
layout.addWidget(button)

button.clicked.connect(chuder)


# 设置窗口的布局
window.setLayout(layout)

# 显示窗口
window.show()

# 进入应用程序的主循环
sys.exit(app.exec_())

