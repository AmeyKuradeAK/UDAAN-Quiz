import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

class HTMLViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HTML Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        with open("basic_form.html", "r") as f:
            html_content = f.read()

        self.browser.setHtml(html_content)

def main():
    app = QApplication(sys.argv)
    viewer = HTMLViewer()
    viewer.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
