import time
import automationhat

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world <a href="/water">Water plants</a>'

@app.route('/water')
def water():
    automationhat.relay.one.on()
    time.sleep(5)
    automationhat.relay.one.off()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
