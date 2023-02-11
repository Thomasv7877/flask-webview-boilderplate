from PyQt6.QtCore import *
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtWidgets import QApplication
import sys
import threading

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def start_server():
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':

    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()

    qt_app = QApplication(sys.argv)# Initialize web engine
    web = QWebEngineView()# Set window title
    web.setWindowTitle("webengine test qt6")
        
    # set window size
    #web.resize(900, 800)# set window zoom
    #web.setZoomFactor(1.5)# load the url
    web.load(QUrl("http://localhost:5000/"))# Show the results
    web.show()
    sys.exit(qt_app.exec())