import sys
import os
from settings import ICON_DIR
from PyQt6.QtWidgets import (
    QMainWindow, 
    QApplication, 
    QToolBar, 
    QStatusBar,
    QDialog,
    QDialogButtonBox,
    QVBoxLayout,
    QLabel,
    QFileDialog,)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt, QSize

class CustomDialog(QDialog): #Кастомный класс под диалоговые окна 
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle('CustomDialog')
        
        buttons = (QDialogButtonBox.StandardButton.Open | QDialogButtonBox.StandardButton.Cancel)
        
        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
        self.layout = QVBoxLayout()
        message = QLabel('CustomDialog OK?')
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('New App')
        
        self.setMinimumSize(800, 600)
        
        # Панель инструментов  
        toolbar = QToolBar('Main toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        
        button_action = QAction(
            QIcon(os.path.join(ICON_DIR, 'globe-small.png')),
            'tb-button 1', self)
        button_action.setStatusTip('Open file')
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        button_action.triggered.connect(self.get_filename)
        toolbar.addAction(button_action)
        
        # Меню главное
        menu = self.menuBar()
        
        p1_menu = menu.addMenu('menu 1')
        p1_menu.addAction(button_action)
        
        p2_menu = menu.addMenu('menu 2')
        p2_menu.addAction('item')
        
        p3_menu = menu.addMenu('menu 3')
        p3_menu.addAction('item')
        
        p4_menu = menu.addMenu('menu 4')
        p4_menu.addAction('item')
        
        
        
        self.setStatusBar(QStatusBar(self))
        
    def get_filename(self):
        """ 
        Функция вызова диалогового окна открытия файла.
        """
        
        filters = 'Файлы Excel (*.xls, *.xlsx);; Текстовые файлы (*.csv);;\
                   Все файлы (*.*)'                   
        print('Filters are:', filters)        
        filename, selected_filter = QFileDialog.getOpenFileName(self, filter=filters)
        print('Result: ', filename, selected_filter)
    
    # Заглушка для тестирования    
    def test_click(self, s): 
        print('TEST CLICK')
        
        

app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()