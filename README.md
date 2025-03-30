# Audio Recorder & Translator

## Overview
This is a web-based application that allows users to record audio, transcribe the speech, and translate it into a specified language using AssemblyAI for transcription and Groq's API for translation. The application is built using Flask for the backend and JavaScript for the frontend.

## Features
- Record audio in the browser
- Upload recorded audio to the server
- Transcribe audio using AssemblyAI
- Translate transcriptions using Groq API
- Play back the recorded audio
- Responsive UI with a gradient background

## Technologies Used
### Frontend:
- HTML, CSS (Gradient UI)
- JavaScript (MediaRecorder API, Fetch API)

### Backend:
- Flask (Python Web Framework)
- AssemblyAI (Speech-to-Text API)
- Groq API (Translation Service)
- dotenv (Environment Variable Management)
- uuid (Unique File Naming)

## Installation
### Prerequisites
- Python 3.x
- Pip
- Virtual environment (optional but recommended)
- AssemblyAI API key
- Groq API key

### Steps to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/audio-translator.git
   cd audio-translator
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your API keys:
   ```env
   GROQ_API_KEY=your_groq_api_key
   api_key=your_assemblyai_api_key
   ```

5. Run the Flask application:
   ```bash
   python app.py
   ```

6. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## API Endpoints
### `GET /`
- Serves the frontend UI.

### `POST /upload/<from_lang>/<to_lang>`
- Uploads an audio file, transcribes it, and translates it.
- **Request Body:** FormData with an `audio` file.
- **Response:**
  ```json
  {
    "message": "Transcription result",
    "original_text": "Original transcription",
    "translated_text": "Translated text",
    "file_path": "path/to/audio/file"
  }
  ```

### `GET /record_file/<filename>`
- Serves the recorded audio file for playback.

## Known Issues & Limitations
- PythonAnywhere may have **file storage and request size limitations**.
- Browser compatibility issues with MediaRecorder API (works best on Chrome & Edge).
- Only supports selected languages in the translation dropdown.

## Future Improvements
- Add support for more languages.
- Improve UI with better error handling and loading indicators.
- Allow users to download transcribed and translated text.

## License
This project is licensed under the MIT License.

