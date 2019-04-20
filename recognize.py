import random
import time

import speech_recognition as sr

def recognize_speech_from_mic(recognizer, microphone):
 
  if not isinstance(recognizer, sr.Recognizer):
    raise TypeError("`recognizer` must be `Recognizer` instance")
  
  if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")
  with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
  response = {
        "success": True,
        "error": None,
        "transcription": None
    }
  try:
        response["transcription"] = recognizer.recognize_google(audio)
  except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
  except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

  return response

if __name__ == "__main__":
 recognizer = sr.Recognizer()
 microphone = sr.Microphone()
 NUM_GUESSES=1
for i in range(NUM_GUESSES):
       # for j in range(PROMPT_LIMIT):
            print('Guess {}. Speak!'.format(i+1))
            guess = recognize_speech_from_mic(recognizer, microphone)
            if guess["transcription"]:
                print("{}".format(guess["transcription"]))
            if not guess["success"]:
           
                print("I didn't catch that. What did you say?\n")

        # if there was an error, stop the game
            if guess["error"]:
             print("ERROR: {}".format(guess["error"]))
             

        # show the user the transcription
 #           print("You said: {}".format(guess["transcription"]))
 
