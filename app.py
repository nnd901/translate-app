from flask import Flask, render_template, request, jsonify
from translate_test import translate_prompt, send_prompt
from dotenv import load_dotenv
import os
from flask_cors import CORS, cross_origin

load_dotenv()
port=os.getenv("PORT")
app=Flask(__name__)
# CORS(app, origins="https://translate-frontend-032f.onrender.com/", methods=["GET", "POST"])
CORS(app)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/message', methods=['POST'])
# @cross_origin(origin='https://translate-frontend-032f.onrender.com')
def translate():
    data = request.get_json()
    message = data.get('message', '')
    #Call my script to translate and send the prompt to gemma
    translatedText=translate_prompt(message)
    answer = send_prompt(translatedText)
    return jsonify({'response': answer})       

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=port)
