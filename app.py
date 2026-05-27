import os
from flask import Flask, send_from_directory, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='.', static_url_path='')

# Configure Gemini
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# The model for text generation
model = genai.GenerativeModel('gemini-1.5-flash')

SYSTEM_PROMPT = """
You are the "Diverse HR Assistant", a friendly, professional AI representative for the Diverse HRMS cloud platform.
Your job is to answer questions about Diverse HRMS. 
Keep your answers brief, professional, and helpful. 
Do not use markdown in your responses (no bold, no italics), just plain text so the chat widget can display it easily.
"""

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    if os.path.exists(path):
        return send_from_directory('.', path)
    # Fallback to appending .html if missing
    if os.path.exists(path + '.html'):
        return send_from_directory('.', path + '.html')
    return send_from_directory('.', 'index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    try:
        # Generate response using Gemini
        full_prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_message}\nAssistant:"
        response = model.generate_content(full_prompt)
        
        return jsonify({
            'response': response.text.strip()
        })
    except Exception as e:
        print(f"Error calling Gemini: {e}")
        return jsonify({'error': 'Failed to process request'}), 500

if __name__ == '__main__':
    # Run the server on port 8080
    app.run(host='0.0.0.0', port=8080, debug=True)
