from collections.abc import Buffer
import os
import dashscope
from dashscope.audio.tts_v2 import VoiceEnrollmentService, SpeechSynthesizer
from dashscope.audio.tts_v2.speech_synthesizer import json
from mcp.server.fastmcp import FastMCP
import time
import magic
import json

mcp = FastMCP("GetAudio")

@mcp.tool()
def create_json_to_audio(json_path: str, out_path: str) -> str:
    """
    This tool is used to convert the verses in a JSON file into audio. Input the path of the JSON file and the output directory, and the audio will be generated and saved to the specified directory.
    Parameters:
        json_path: Path to the JSON file
        out_path: Output path
    Returns:
        Success: Operation success
        Failed: Operation failed
    """
    cv = Cosyvoice()
    return cv.create_json_to_audio(json_path, out_path)

@mcp.tool()
def create_text_to_audio(text: str, out_path: str) -> str:
    """
    This tool is used to convert text into audio. Input the text and the output directory, and the audio will be generated and saved to the specified directory.
    Parameters:
        text: String text
        out_path: Output directory for the audio
    Returns:
        Success: Operation success
        Failed: Operation failed
    """
    cv = Cosyvoice()
    return cv.generate_audio(text, out_path)

class Cosyvoice:
    
    sleepTime = 0
    
    def __init__(self):
        pass
    def create_json_to_audio(self, json_path: str, out_path: str) -> str:
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            return "Failed"

        for key, item in enumerate(data):
            shiJuSplit_array = item["shiJuSplit"].split("|")
            for index, value in enumerate(shiJuSplit_array):
                self.generate_audio(value, os.path.join(out_path, f"t{key+1}{index}.mp3"))
        return "Success"
    
    def generate_audio(self, text: str, out_path) -> str:
        dashscope.api_key = os.getenv("DASHSCOPE_API_KEY")
        target_model = "cosyvoice-v1"
        voice_id = "cosyvoice-prefix-4eec46a3b5d8499a8c29c46766452a63"
        synthesizer = SpeechSynthesizer(model=target_model, voice=voice_id)
        audio_result = synthesizer.call(str(text))
        try:
            with open(out_path, "wb") as f:
                if audio_result is not None:
                    f.write(audio_result)
                else:
                    raise Exception("音频生成结果为空")
            return "Success"
        except Exception as e:
            return "Failed"
if __name__ == "__main__":
    # cv = Cosyvoice()
    # cv.create_json_to_audio("S:/AI/AutoGenTest/output/item.json", "S:/AI/AutoGenTest/output")
    mcp.run(transport='stdio')
