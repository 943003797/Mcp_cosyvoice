import os
import dashscope
from dashscope.audio.tts_v2 import VoiceEnrollmentService, SpeechSynthesizer

dashscope.api_key = 'sk-30d9c41320b94ca09f1eb917261ed379'  # 如果您没有配置环境变量，请在此处用您的API-KEY进行替换
prefix = 'prefix'
target_model = "cosyvoice-v1"

# 创建语音注册服务实例
service = VoiceEnrollmentService()

# 调用create_voice方法复刻声音，并生成voice_id
voice_id = "cosyvoice-prefix-84fa79f3ce034aea89727a81bb7222f9"

# 使用复刻的声音进行语音合成
synthesizer = SpeechSynthesizer(model=target_model, voice=voice_id)
audio = synthesizer.call("千古词帝，李煜的巅峰之作，哪句更触动你心")
print("requestId: ", synthesizer.get_last_request_id())

# 将合成的音频文件保存到本地文件
# 定义保存目录
save_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
# 确保保存目录存在
os.makedirs(save_directory, exist_ok=True)
# 拼接完整的文件路径
file_path = os.path.join(save_directory, "output.mp3")
with open(file_path, "wb") as f:
    f.write(audio)