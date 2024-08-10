from flask import Flask, render_template, request
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text')
        language = request.form.get('language', 'en')
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save('static/output.mp3')
        return render_template('index.html', audio_file='static/output.mp3')
    return render_template('index.html', audio_file=None)

if __name__ == '__main__':
    app.run(debug=True)