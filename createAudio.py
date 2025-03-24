import os
import dashscope
from dashscope.audio.tts_v2 import VoiceEnrollmentService, SpeechSynthesizer
from mcp.server.fastmcp import FastMCP
import time

mcp = FastMCP("GetAudio")

@mcp.tool()
def say_hello(text: str, file_path: str) -> str:
    """
    使用这个工具可以获取配音, 输入文本和目录即可生成配音并保存到指定目录
    参数:
        text: 要生成配音的文本
        file_path: 保存配音的目录
    返回:
        Success: 成功
        Failed: 失败
    """

    dashscope.api_key = 'sk-30d9c41320b94ca09f1eb917261ed379'  # 如果您没有配置环境变量，请在此处用您的API-KEY进行替换
    url = "https://api.hostize.com/files/d7B0_pGfZZ/download/file.wav"  # 请按实际情况进行替换
    prefix = 'prefix'
    target_model = "cosyvoice-v1"
    # 创建语音注册服务实例
    service = VoiceEnrollmentService()

    # 调用create_voice方法复刻声音，并生成voice_id
    # voice_id = service.create_voice(target_model=target_model, prefix=prefix, url=url)
    # print("requestId: ", service.get_last_request_id())
    # print(f"your voice id is {voice_id}")
    voice_id = "cosyvoice-prefix-4eec46a3b5d8499a8c29c46766452a63"

    # 使用复刻的声音进行语音合成
    synthesizer = SpeechSynthesizer(model=target_model, voice=voice_id)
    audio_result = synthesizer.call(text)
    print("requestId: ", synthesizer.get_last_request_id())

    # 将合成的音频文件保存到本地文件
    # 定义保存目录
    save_directory = file_path if file_path else ""
    # 确保保存目录存在
    os.makedirs(save_directory, exist_ok=True)
    # 拼接完整的文件路径
    timestamp = str(int(time.time()))
    file_path = os.path.join(save_directory, f"{timestamp}.mp3")
    try:
        with open(file_path, "wb") as f:
            f.write(audio_result)
        return "Success"
    except Exception as e:
        print(f"Error: {e}")
        return "Failed"

if __name__ == "__main__":
    mcp.run(transport='stdio')
