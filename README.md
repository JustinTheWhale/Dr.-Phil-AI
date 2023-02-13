# Dr. Phil AI

## About 

#### Python program that records your voice, creates a text transcription of your voice,
#### uses the transcription as input to ChatGPT, and plays ChatGPT's response in Dr. Phil's voice.
#### You can technically do any voice with ElevenLabs but I chose Dr. Phil in this case.

#### Tested and working on Python 3.10. Should work on others too. Additionally I've only used this on Windows but I'm sure others can figure out MacOS and Linux.

## Installation 
### Windows
- #### Make an account for ChatGPT and ElevenLabs.
- #### Clone this repo or download the zipped source code.
- #### Follow the same setup from [chatgpt-wrapper](https://github.com/mmabrouk/chatgpt-wrapper) 
- #### Requires [ffmpeg](https://ffmpeg.org/) to be in your PATH to playback the sound.
- #### Install [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) with ``` pip install SpeechRecognition ```
- #### Install [pydub](https://github.com/jiaaro/pydub) with ``` pip install pydub ```

## Usage
``` python Dr_Phil_AI.py ```