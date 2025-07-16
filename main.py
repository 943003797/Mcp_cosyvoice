from collections.abc import Buffer
import os
import dashscope
from dashscope.audio.tts_v2 import VoiceEnrollmentService, SpeechSynthesizer
from dashscope.audio.tts_v2.speech_synthesizer import json
from mcp.server.fastmcp import FastMCP
import json
from dotenv import load_dotenv
load_dotenv()

mcp = FastMCP("GetAudio", port=8001)

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
    
    def __init__(self):
        pass
    
    def generate_audio(self, text: str, out_path) -> str:
        dashscope.api_key = os.getenv("ALI_KEY")
        target_model = "cosyvoice-v1"
        voice_id = "cosyvoice-prefix-4eec46a3b5d8499a8c29c46766452a63"
        synthesizer = SpeechSynthesizer(model=target_model, voice=voice_id)
        audio_result = synthesizer.call(str(text))
        try:
            with open(out_path, "wb") as f:
                if audio_result is not None:
                    f.write(audio_result)
                else:
                    raise Exception("Geneal audio faild")
            return "Success"
        except Exception as e:
            return "Failed"
if __name__ == "__main__":
    mcp.run(transport='sse')