from flask import Flask, request, jsonify, render_template
import os
from openai import OpenAI
from flask_cors import CORS

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

template_dir = os.path.join(os.path.dirname(__file__), 'Public')
app = Flask(__name__, template_folder=template_dir)
CORS(app)

@app.route('/')
def index():
    return render_template('chat-interface.html')

@app.route('/chat', methods=['POST'])
def chat():
    model_name = request.form['model_name']
    user_input = request.form['user_input']
    
    messages = [{'role': 'user', 'content': user_input}]

    try:
        response = client.chat.completions.create(model=model_name, messages=messages)
        return jsonify({'response': response.choices[0].message.content.strip()})
    except Exception as e:
        return jsonify({'response': 'Error: ' + str(e)})

if __name__ == '__main__':
    app.run(debug=True)
