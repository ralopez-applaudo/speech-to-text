from flask import Flask, request, jsonify
import whisper
import tempfile
import os
from flask_cors import CORS

model = whisper.load_model("large-v3")

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
print("asdf")
print(model.device)

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    uploaded_file = request.files['file']
    original_filename = uploaded_file.filename
    ext = os.path.splitext(original_filename)[1].lower().replace('.', '')

    # Guardar archivo temporal con extensión original
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{ext}") as temp_audio:
        uploaded_file.save(temp_audio.name)

    # Transcribe directamente con Whisper
    result = model.transcribe(temp_audio.name, language='en')
    raw_text = result['text']

    os.remove(temp_audio.name)

    return jsonify({
        'raw_transcription': raw_text.strip()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
