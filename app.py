import time
import automationhat

from flask import Flask, flash, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' #changeme, just a test

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/water', methods=['POST'])
def water():
    automationhat.relay.one.on()
    time.sleep(5)
    automationhat.relay.one.off()
    
    flash('Yay, you just watered your trees for 5 seconds!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
