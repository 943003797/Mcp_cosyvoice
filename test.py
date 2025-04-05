import os
import dashscope
from dashscope.audio.tts_v2 import VoiceEnrollmentService, SpeechSynthesizer

dashscope.api_key = 'sk-30d9c41320b94ca09f1eb917261ed379'  # 如果您没有配置环境变量，请在此处用您的API-KEY进行替换
# url = "https://api.hostize.com/files/d7B0_pGfZZ/download/file.wav"  # 请按实际情况进行替换
url = "https://api.hostize.com/files/B8dLShNAE5/download/file.wav"
prefix = 'prefix'
target_model = "cosyvoice-v1"

# 创建语音注册服务实例
service = VoiceEnrollmentService()

# 调用create_voice方法复刻声音，并生成voice_id
voice_id = service.create_voice(target_model=target_model, prefix=prefix, url=url)
print("requestId: ", service.get_last_request_id())
print(f"your voice id is {voice_id}")