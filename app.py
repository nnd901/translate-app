from flask import Flask, render_template, request, jsonify
from translate_test import translate_prompt, send_prompt

app=Flask(__name__)
# @app.route('/')

# def index():
#     return render_template('index.html')

@app.route('/message', methods=['POST'])
def translate():
    data = request.get_json()
    message = data.get('message', '')
    #Call my script to translate and send the prompt to gemma
    translatedText=translate_prompt(message)
    answer = send_prompt(translatedText)
    return jsonify({'response': answer})       

if __name__ == '__main__':
    app.run(debug=True,port=5000)
