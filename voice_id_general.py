import os
import dashscope
from dashscope.audio.tts_v2 import VoiceEnrollmentService, SpeechSynthesizer

dashscope.api_key = os.getenv("ALI_KEY")
# url = "https://api.hostize.com/files/B8dLShNAE5/download/file.wav"
url = "https://api.hostize.com/files/adsTkQnQCK/download/file.wav"
prefix = 'prefix'
target_model = "cosyvoice-v2"
service = VoiceEnrollmentService()
voice_id = service.create_voice(target_model=target_model, prefix=prefix, url=url)
print("requestId: ", service.get_last_request_id())
print(f"your voice id is {voice_id}")