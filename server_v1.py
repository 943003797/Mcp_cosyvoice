from collections.abc import Buffer
import os
import dashscope
from dashscope.audio.tts_v2 import VoiceEnrollmentService, SpeechSynthesizer
from mcp.server.fastmcp import FastMCP
import time
import magic

mcp = FastMCP("GetAudio")

@mcp.tool()
def create_text_to_audio(text: str,file_neme: str, file_path: str) -> str:
    """
    Use this tool to generate voiceover. Input text and directory to generate and save voiceover to the specified directory
    Parameters:
        text: Text to generate voiceover from
        file_neme: File name
        file_path: Save directory
    Returns:
        Success: Operation successful
        Failed: Operation failed
    """
    cv = Cosyvoice()
    return cv.create_text_to_audio(text, file_neme, file_path)

class Cosyvoice:
    
    sleepTime = 0
    
    def __init__(self):
        pass
    def create_text_to_audio(self, text: str, file_neme: str, file_path: str) -> str:
        if self.sleepTime >= 2:
            time.sleep(1)
            self.create_text_to_audio(text, file_neme, file_path)
        self.sleepTime += 1
        
        dashscope.api_key = os.getenv("DASHSCOPE_API_KEY")
        # url = "https://api.hostize.com/files/d7B0_pGfZZ/download/file.wav"
        # prefix = 'prefix'
        target_model = "cosyvoice-v1"

        # service = VoiceEnrollmentService()

        voice_id = "cosyvoice-prefix-84fa79f3ce034aea89727a81bb7222f9"
        synthesizer = SpeechSynthesizer(model=target_model, voice=voice_id)
        audio_result = synthesizer.call(text)
        self.sleepTime -= 1

        save_directory = file_path if file_path else ""
        os.makedirs(save_directory, exist_ok=True)
        file_path = os.path.join(save_directory, f"{file_neme}.mp3")
        try:
            with open(file_path, "wb") as f:
                # 检查 audio_result 是否为 None，如果不是则写入文件
                if audio_result is not None:
                    f.write(audio_result)
                else:
                    raise Exception("音频生成结果为空")
            # txt_file_path = os.path.join(save_directory, f"{file_neme}.txt")
            # with open(txt_file_path, "w", encoding="utf-8") as txt_file:
            #     txt_file.write(text)
            # 检查文件是否为有效的 MP3 文件
            file_mime = magic.from_file(file_path, mime=True)
            if file_mime != 'audio/mpeg':
                return "Failed"
            return "Success"
        except Exception as e:
            return "Failed"
if __name__ == "__main__":
    mcp.run(transport='stdio')
