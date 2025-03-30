from flask import Flask,render_template,request,jsonify,send_from_directory
import os
from dotenv import load_dotenv
import assemblyai as aai
import uuid
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
API_KEY = os.getenv("api_key")
aai.settings.api_key = API_KEY

UPLOAD_FOLDER = "record_file"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


client = Groq(
    api_key=GROQ_API_KEY
)


transcriber = aai.Transcriber()

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def translate(text,from_lang,to_lang):
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful translator."},
            {"role": "user", "content": f"Translate this from {from_lang} to {to_lang}: {text}"}
        ],
        model="llama-3.3-70b-versatile"
    )
    return response.choices[0].message.content

@app.route('/',methods=["GET"])
def main():
    return render_template('index.html')


@app.route('/upload/<from_lang>/<to_lang>', methods=["POST"])
def upload(from_lang,to_lang):
    if "audio" not in request.files:
        return jsonify({"error": "No audio file found"}), 400

    audio_file = request.files["audio"]
    unique_filename = f"{uuid.uuid4()}.wav"
    file_path = os.path.join(UPLOAD_FOLDER, unique_filename)
    audio_file.save(file_path)
    
    transript = transcriber.transcribe(file_path)
    if transript.status == aai.TranscriptStatus.error:
        return jsonify({"message": "File failed to transcribe", "file_path": "not available"}), 500
    
    transcript_result = transript.text
    
    translated_text = translate(transcript_result, from_lang=from_lang, to_lang=to_lang)
    return jsonify({
        "message": transcript_result,
        "original_text": transcript_result,
        "translated_text": translated_text,
        "file_path": file_path
    }), 200


@app.route("/record_file/<filename>")
def get_audio(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == '__main__':
    app.run()
