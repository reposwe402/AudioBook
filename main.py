from file_handler import extract_text_from_pdf
from audio_processor import text_to_speech
import config


def main():
    # Extract text from the PDF file
    text = extract_text_from_pdf(config.PDF_PATH)
    
    # Convert the extracted text to speech
    text_to_speech(text, language=config.LANGUAGE, output_file=config.OUTPUT_AUDIO_FILE)
    
    print("Audio book created successfully.")


if __name__ == "__main__":
    main()
