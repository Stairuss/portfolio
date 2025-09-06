from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main_page.html')

@app.route('/w-wave')
def w_wave():
    return render_template('layouts/w-wave.html')

if __name__ == '__main__':
    app.run()