import os
from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Initialize Groq Client
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']

    response = groq_client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    reply = response.choices[0].message.content.strip()
    return jsonify({'response': reply})

if __name__ == '__main__':
    app.run(debug=True)
