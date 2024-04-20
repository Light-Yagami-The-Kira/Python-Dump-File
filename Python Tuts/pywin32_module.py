from win32com.client import Dispatch
voice = Dispatch('SAPI.SpVoice')

voice.speak("Hello there, I am your Virtual Assistant Arsee.")