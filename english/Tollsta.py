import sys
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtWidgets import (QLineEdit, QMessageBox, QHBoxLayout, QPushButton, QLabel, QApplication, QWidget, QComboBox, QVBoxLayout, QShortcut)
import os
import subprocess
import platform
import configparser

# Read the config.ini file
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

class Window1(QWidget):
    def __init__(self):
        super().__init__()
        self.tools()

    def tools(self):
        # UI display animation
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)

        folder_path = 'png'

        # Check if the folder exists
        if os.path.exists(folder_path):

            self.setWindowTitle('Tools Box')

            # Create a layout
            layout = QVBoxLayout()

            # Set the window size
            self.resize(320, 100)  # Width 400 pixels, height 300 pixels

            # Set the window icon
            pixmap = QPixmap('png/logo.jpg')  # Ensure the icon file path is correct
            icon = QIcon(pixmap)
            self.setWindowIcon(icon)

            label = QLabel('Tools Box')
            layout.addWidget(label)

            # Specify the folder path you want to check and create
            folder_path = 'tools'

            # Check if the folder exists
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Create the first combo box
            comboBox = QComboBox(self)
            layout.addWidget(comboBox)

            # Create the second combo box
            comboBox1 = QComboBox(self)
            layout.addWidget(comboBox1)

            # Create the third combo box
            comboBox2 = QComboBox(self)
            layout.addWidget(comboBox2)

            # Populate the first combo box
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
                    if entry.lower().endswith(('.exe', '.bat')):
                        comboBox2.addItem(entry)

            def chuder():
                try:
                    # Specify the path of the .exe file to be launched
                    exe_path = os.path.join('tools', comboBox.currentText(), comboBox1.currentText(), comboBox2.currentText())
                    process = subprocess.Popen(exe_path, shell=True)
                except:
                    ts = QMessageBox()
                    ts.setIcon(QMessageBox.Critical)
                    ts.setText("Failed to start the program. Please check if the software is a runnable exe/bat.")
                    ts.setWindowTitle("Error")
                    ts.setStandardButtons(QMessageBox.Ok)

            # Connect the currentIndexChanged signal of the first combo box to the slot function
            comboBox.currentIndexChanged.connect(updateComboBox1)

            # Connect the currentIndexChanged signal of the second combo box to the slot function
            comboBox1.currentIndexChanged.connect(updateComboBox2)

            # Create a button
            button = QPushButton('Start Program', self)
            layout.addWidget(button)

            button.clicked.connect(chuder)

            # Set the window layout
            self.setLayout(layout)

        else:
            msg2 = QMessageBox()
            msg2.setIcon(QMessageBox.Information)
            msg2.setText("The png folder does not exist, which is a fatal error.")
            msg2.setWindowTitle("Window")
            msg2.setStandardButtons(QMessageBox.Ok)

class Window2(QWidget):
    def __init__(self):
        super().__init__()
        self.tools()

    def tools(self):
        # UI display animation
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)

        self.setWindowTitle('Simple Tools in the System')

        # Create a layout
        layout = QVBoxLayout()

        # Set the window size
        self.resize(320, 100)  # Width 400 pixels, height 300 pixels

        # Set the window icon
        pixmap = QPixmap('png/logo.jpg')  # Ensure the icon file path is correct
        icon = QIcon(pixmap)
        self.setWindowIcon(icon)

        # Read the text1 key from the 'set' section and set it as the variable text1
        text1 = config.get('set', 'text1')
        self.label = QLabel(text1)
        layout.addWidget(self.label)

        text2 = config.get('set', 'text2')
        self.label1 = QLabel(text2)
        layout.addWidget(self.label1)

        def open_window2():
            window.show()  # Show Window

        # Create a button
        button1 = QPushButton('Open System Toolset', self)
        layout.addWidget(button1)
        button1.clicked.connect(open_window2)

        # GitHub
        def open_github():
            os.startfile('https://github.com/shuiyu0407/tolls')

        buttonc = QPushButton('GitHub')
        icon = QIcon('png/GitHub-Simbolo.png')
        buttonc.setIcon(icon)
        buttonc.clicked.connect(open_github)

        # Settings
        def open_i():
            set.show()

        buttoni = QPushButton('Settings')
        icon = QIcon('png/R-C.png')
        buttoni.setIcon(icon)
        buttoni.clicked.connect(open_i)

        # System Information
        def open_window():
            try:
                msg1 = QMessageBox()
                msg1.setIcon(QMessageBox.Information)
                # Get CPU information
                cpu_info = platform.processor()
                # Get memory information
                memory_info = platform.machine()
                # Get system architecture
                system_arch = platform.system()
                # Get system version
                system_version = platform.version()
                msg1.setText(f"CPU: {cpu_info}\nMemory: {memory_info}\nSystem: {system_arch}\nSystem Version: {system_version}")
                msg1.setWindowTitle("Window")
                msg1.setStandardButtons(QMessageBox.Ok)
                msg1.exec_()

            except:
                ts = QMessageBox()
                ts.setIcon(QMessageBox.Critical)
                ts.setText("Failed to get system information. Please check if your system is Windows 10 or above.")
                ts.setWindowTitle("Error")
                ts.setStandardButtons(QMessageBox.Ok)

        buttonw = QPushButton('System Information')
        icon = QIcon('png/window.png')
        buttonw.setIcon(icon)
        buttonw.clicked.connect(open_window)

        # Create a horizontal layout and add two buttons
        horizontalLayout = QHBoxLayout()
        horizontalLayout.addWidget(buttonc)
        horizontalLayout.addWidget(buttoni)
        horizontalLayout.addWidget(buttonw)

        # Add the horizontal layout to the main layout
        layout.addLayout(horizontalLayout)

        # Set the window layout
        self.setLayout(layout)

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox
from PyQt5.QtGui import QPixmap, QIcon

class Window3(QWidget):
    def __init__(self):
        super().__init__()
        self.tools()

    def tools(self):
        # Create layout and window
        self.setWindowTitle('Tools Box')

        # Create a layout
        layout = QVBoxLayout()

        # Set the window size
        self.resize(320, 100)  # Width 400 pixels, height 300 pixels

        # Set the window icon
        pixmap = QPixmap('png/logo.jpg')  # Ensure the icon file path is correct
        icon = QIcon(pixmap)
        self.setWindowIcon(icon)

        # Create a horizontal layout
        horizontalLayout = QHBoxLayout()

        # Create a text label
        label = QLabel('Use Toolbox')
        horizontalLayout.addWidget(label)

        # Create an input box
        self.lineEdit = QLineEdit()
        horizontalLayout.addWidget(self.lineEdit)

        def search():
            # Get the content of the input box
            text = self.lineEdit.text()
            # Write to the config.ini file
            try:
                # Detect the first line content of the config.ini file and set it as the variable cerf
                with open('config.ini', 'r') as f:
                    cerf = f.readline()

                # Download the cerf address file to the tools folder
                subprocess.Popen(f'curl -o tools/cerf.zip {cerf}', shell=True)

                # Unzip the cerf.zip file to the tools folder, do not use unzip
                subprocess.Popen(f'7z x tools/cerf.zip -o"tools"', shell=True)

                # Prompt for successful download
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Download successful, please reopen the toolbox.")
                msg.setWindowTitle("Window")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                # Close the window
                self.close()
            except:
                # Prompt for download failure
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Download failed, please check your network connection/address.")
                msg.setWindowTitle("Error")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

        # Add a confirm button
        button = QPushButton('Confirm')
        horizontalLayout.addWidget(button)
        button.clicked.connect(search)

        # Add the horizontal layout
        layout.addLayout(horizontalLayout)

        # Set the window layout
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create a QApplication instance
    window = Window1()
    windows = Window2()
    set = Window3()
    windows.show()  # Show Windows
    sys.exit(app.exec_())  # Enter the event loop
