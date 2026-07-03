# 🎙️ Voice-to-Voice Assistant

A Python-based Voice-to-Voice AI Assistant that listens to user speech, converts it into text using Speech Recognition, sends the transcript to the OpenAI API for processing, and returns an intelligent response.

## 🚀 Features

* 🎤 Speech-to-Text (STT) using SpeechRecognition
* 🤖 AI-powered responses using the OpenAI API
* 🔊 Ready for Speech-to-Speech  integration
* 🔐 Secure API key management with `.env`
* 🧩 Simple and easy-to-understand Python implementation

## 🛠️ Technologies Used

* Python
* OpenAI API
* SpeechRecognition
* PyAudio
* python-dotenv

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/riyagodambe29-netizen/voice-to-voice-assistant.git
cd voice-to-voice-assistant
```

### 2. Install the required packages

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

Create a `.env` file in the project root and add your OpenAI API key:

```env
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

Replace `YOUR_OPENAI_API_KEY` with your own API key.

### 4. Run the application

```bash
python app.py
```

## 📁 Project Structure

```text
voice-to-voice-assistant/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
└── .env (not included)
```

## 🔒 Security

* Never upload your `.env` file to GitHub.
* Keep your OpenAI API key private.
* Ensure `.env` is listed in your `.gitignore` file.

## 📄 License

This project is licensed under the MIT License.
.
