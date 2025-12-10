# Thirukkural Voice-Based Retrieval Application

## Overview
This project is a Python-based application that retrieves Thirukkural verses using Tamil speech input. 
It integrates speech recognition, NLP-based text matching, and a graphical user interface.

## Technologies Used
- Python
- pandas (data processing)
- speech_recognition (speech-to-text)
- Tkinter (GUI)
- ElevenLabs Text-to-Speech API
- cx_Freeze (application packaging)

## System Architecture
1. Speech input is captured via microphone.
2. Speech is converted to text (Tamil).
3. Recognized text is matched against indexed Thirukkural verses.
4. Retrieved verse is displayed and synthesized as speech output.

## Artificial Intelligence Components
- Speech-to-text processing
- NLP-based text matching
- Multilingual text-to-speech synthesis

## How to Run
1. Install dependencies listed in `requirements.txt`
2. Set API key via environment variable
3. Run `Thirukkural.py`

## Notes
API keys and file paths are excluded for security and portability reasons.
