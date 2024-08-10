# web-week5-task-1

smart methods internship

# Text-to-Speech Web App
A simple web application that converts text to speech using Python, Flask, and gTTS.

## Features
- Convert text to speech in English or Arabic.
- User-friendly web interface.

## Requirements
- Python 3.x
- Flask
- gTTS

## Installation
1- Create and activate a virtual environment (optional but recommended): This isolates project dependencies:

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

2- Install the required packages: Install Flask and gTTS using pip:
```bash
pip install Flask gTTS
```

3- Create the static directory: Ensure a static folder exists to store generated audio files.

4- Code (available in the repository)
  - app.py
    - Imports:
      - Flask: Web framework for Python.
      - gTTS: Google Text-to-Speech library.
      - os: For file operations.
    - Flask App Setup:
      - Create a Flask app instance.
      - Define routes and handle HTTP methods.
    - Index Route (/):
      - Handles both GET and POST requests.
      - On POST, retrieves text and language from the form.
      - Utilizes gTTS to convert text to speech and saves it as output.mp3 in the static directory.
      - Renders index.html with the audio file path.
  - templates/index.html
    - HTML Form:
      - Textarea for user input.
      - Dropdown to select language (English or Arabic).
      - Submit button to trigger TTS conversion.
    - Audio Playback:
      - If audio is generated, display an HTML5 audio player to listen to the output.
  - static/output.mp3
      - to save the audio in it 

5- Usage
  - Run the Flask app: Start the server:
  bash
  python app.py
  This will host the app locally on http://127.0.0.1:5000.
  - Open your web browser and navigate to: http://127.0.0.1:5000
  - Interact with the app:
    - Enter text in the provided textarea.
    - Select a language (English or Arabic).
    - Click "Convert to Speech" to generate and play the audio.
