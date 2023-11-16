import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog, QAction

from airspeed import Template

class VelocityTemplatePreviewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.templateEditor = QTextEdit()
        self.outputViewer = QTextEdit()
        self.renderButton = QPushButton("Render")

        layout.addWidget(self.templateEditor)
        layout.addWidget(self.renderButton)
        layout.addWidget(self.outputViewer)

        # Create menu bar and actions
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('File')

        openAction = QAction('Open', self)
        openAction.triggered.connect(self.openFile)
        fileMenu.addAction(openAction)

        saveAction = QAction('Save', self)
        saveAction.triggered.connect(self.saveFile)
        fileMenu.addAction(saveAction)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        self.renderButton.clicked.connect(self.renderTemplate)

    def openFile(self):
        # Function to open and read a file
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Template File", "", "Velocity Templates (*.vm)")
        if fileName:
            with open(fileName, 'r') as file:
                self.templateEditor.setText(file.read())

    def saveFile(self):
        # Function to save the current content to a file
        fileName, _ = QFileDialog.getSaveFileName(self, "Save Template File", "", "Velocity Templates (*.vm)")
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.templateEditor.toPlainText())

    def renderTemplate(self):
        template_str = self.templateEditor.toPlainText()
        try:
            # Directly use Template class to parse the string
            template = Template(template_str)
            rendered = template.merge({})
            self.outputViewer.setText(rendered)
        except Exception as e:
            self.outputViewer.setText(f"Error: {e}")

def main():
    app = QApplication(sys.argv)
    mainWin = VelocityTemplatePreviewer()
    mainWin.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
