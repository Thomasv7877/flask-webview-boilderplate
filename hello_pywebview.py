from flask import Flask
import webview
import sys
import threading

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return "<p>Hello, World!</p>"

def start_server():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':

    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()
    
    webview.create_window("PyWebView & Flask", "http://localhost:5000")
    webview.start()
    sys.exit()
