# Main Python script of FakeSusy for Windows.

# Importing built-in python modules:
import sys
import urllib.request

# Importing PyQt5 Modules
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp, QAction, \
                            QDockWidget, QFileDialog, QTreeWidget, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore

# Define a Janela
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Definindo Acoes

        fakesusy = QAction(QIcon("..\\icons\\codeIcon.png"), 'Sobre o FakeSusy...', self)
        fakesusy.setStatusTip('Informações adicionais sobre o FakeSusy for Windows!')
        fakesusy.setIconText('FakeSusy\n4Windows')
        fakesusy.triggered.connect(self.setWelcomeWidget)

        flags = QAction(QIcon("..\\icons\\flag.svg"), 'Flags de Compilação', self)
        flags.setStatusTip('Configura as flags de compilação de um código em C.')
        flags.setIconText('Flags de\nCompilação')
        flags.triggered.connect(self.showWindow)

        tempo = QAction(QIcon("..\\icons\\clock.svg"), 'Tempo Restante', self)
        tempo.setStatusTip('Ativa/Desativa a exibição do tempo restante para entrega do laboratório.')
        tempo.setIconText('Tempo\nRestante')

        arquivos = QAction(QIcon("..\\icons\\folder.svg"), 'Arquivos', self)
        arquivos.setStatusTip('Exibe uma pasta com os seus arquivos e códigos fonte.')
        arquivos.setIconText('Meus\nArquivos')
        
        servidor = QAction(QIcon("..\\icons\\server.svg"), 'Servidor', self)
        servidor.setStatusTip('Configura o servidor usado no Susy.')
        servidor.setIconText('Servidor\nSusy')
        
        compilar = QAction(QIcon("..\\icons\\box.svg"), 'Compilar Código', self)
        compilar.setStatusTip('Realiza a compilação e teste do seu código em C.')
        compilar.setIconText('Compilar\ne Testar!')

        baixar = QAction(QIcon("..\\icons\\cloud-download.svg"), 'Baixar Testes do Susy', self)
        baixar.setStatusTip('Realiza o download de todos os testes do laboratório atual.')
        baixar.setIconText('Baixar\nLabs')

        submeter = QAction(QIcon("..\\icons\\outbox.svg"), 'Submeter Laboratório', self)
        submeter.setStatusTip('Realiza a submissão do laboratório no sistema Susy.')
        submeter.setIconText('Submeter\nLaboratório')

        aluno = QAction(QIcon("..\\icons\\head.svg"), 'Configurar Login e Senha', self)
        aluno.setStatusTip('Configura as credenciais de login e senha do sistema Susy.')
        aluno.setIconText('Configurar\nLogin')

        sair = QAction(QIcon("..\\icons\\circle-cross.svg"), 'Encerrar o FakeSusy', self)
        sair.setStatusTip('Encerrar o FakeSusy for Windows.')
        sair.setIconText('Encerrar\nFakeSusy')
        sair.triggered.connect(qApp.quit)

        # Barra de Menus
        menubar = self.menuBar()
        dataMenu = menubar.addMenu('&Download/Upload')
        dataMenu.addAction(fakesusy)
        dataMenu.addAction(sair)
        menubar.addMenu('&Disciplinas')
        menubar.addMenu('&Laboratórios')
        menubar.addMenu('&Configurações')
        unichampsMenu = menubar.addMenu('&Aqui é Unichamps!')
        
        # Barra de Status
        self.statusBar()

        # Configurando a Barra de Ferramentas.
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(fakesusy)
        self.toolbar.addAction(servidor)
        self.toolbar.addAction(flags)
        self.toolbar.addAction(tempo)
        self.toolbar.addAction(arquivos)
        
        self.toolbar.addAction(compilar)
        self.toolbar.addAction(baixar)
        self.toolbar.addSeparator()
        self.toolbar.addAction(submeter)
        self.toolbar.addSeparator()
        self.toolbar.addAction(aluno)
        self.toolbar.addAction(sair)
        self.toolbar.setToolButtonStyle(3)
        self.toolbar.setMovable(False)
        
        # Definindo Geometria da Janela
        self.setWindowTitle('FakeSusy for Windows v0.11')
        self.setWindowIcon(QIcon('..\icons\codeIcon.png'))
        self.resize(700, 600)

    def setWelcomeWidget(self):
        welcome = QTextEdit()
        fchangelog = open('..\\changelog.txt', encoding='utf-8', 'r')
        with fchangelog:
            changelog = fchangelog.read()
            welcome.setText(changelog)
        self.dock = QDockWidget('Bem-Vindo!', self)
        self.dock.setWidget(welcome)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dock)

    def showWindow(self):
        newWindow = closeWindow()
        newWindow.exec_()
    
# Exibe a Janela
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
