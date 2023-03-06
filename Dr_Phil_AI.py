import io

import requests
import openai
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play


def listen() -> str:
    """ Uses the default sound device to record audio. Stops recording when you stop talking.

    Returns:
        str: The attempted text transcription of what you said during the recording.
    """
    while(1):   
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                break
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occurred")
    
    return MyText


def ask_chatGPT(prompt: str) -> str:
    """Connects to ChatGPT and passes through the text transcription of your voice as input.

    Args:
        prompt (str): The text transcription to input into ChatGPT.

    Returns:
        str: Response fromChatGPT as a str.
    """
    print("Initailizing connection to the chatGPT API")
    print("Awaiting response from chatGPT")
    openai.api_key = ''
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt},
    ]
    )

    return response['choices'][0]['message']['content'].replace("\n", "")


def generate_Dr_Phils_voice(text: str) -> None:
    """Uses the ElevenLabs API to play an audio stream from a returned POST request.

    Args:
        text (str): The text to be translated into an audio stream
    """
    done = False
    while not done:
        try:
            elevenLabsKey = ''
            voice_id = ''
            body = {'text' : text}
            url = f'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream'
            print('Awaiting response from Dr. Phil')
            response = requests.post(url, headers={'xi-api-key' : elevenLabsKey}, json=body)
            if response.status_code == 200:
                recording = AudioSegment.from_file(io.BytesIO(response.content), format="mp3")
                play(recording)
                done = True
        except:
            continue


if __name__ == '__main__':
    print("Please ask your question quickly and clearly.")
    
    r = sr.Recognizer()
    MyText =listen()
    print("Successfully generated text from speech input")
    
    
    MySpeech = MyText.split('\n')[-1].capitalize() + '?'
    print(f"Prompt Sent to chatGPT: {MySpeech}")
    chatGPTResponse = ask_chatGPT(MySpeech)
    print("successfuly received a response from chatGPT")
    
    print("Sending chatGPT response to the ElevenLabs voice cloning API")
    generate_Dr_Phils_voice(chatGPTResponse)
