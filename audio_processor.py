from gtts import gTTS

def text_to_speech(text, language='en', output_file='Audio.mp3'):
    """
    Convert text to speech and save as an MP3 file.

    :param text: The text to convert to speech.
    :param language: The language of the text.
    :param output_file: The output MP3 file name.
    """
    my_audio = gTTS(text=text, lang=language, slow=False)
    my_audio.save(output_file)
