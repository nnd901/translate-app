from flask import Flask, render_template, request
from translate_test import translate_prompt, send_prompt

app=Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']

    #Call my script to translate and send the prompt to gemma
    translatedText=translate_prompt(text)
    answer = send_prompt(translatedText)
    return render_template('index.html',translation=answer)       

if __name__ == '__main__':
    app.run(debug=True)
