import os
import dashscope
from dashscope.audio.tts_v2 import VoiceEnrollmentService, SpeechSynthesizer
from dashscope.audio.tts_v2.speech_synthesizer import json
from mcp.server.fastmcp import FastMCP
import json
from dotenv import load_dotenv
load_dotenv()

def get_audio(text: str, out_path: str) -> str:
        dashscope.api_key = os.getenv("ALI_KEY")
        target_model = "cosyvoice-v2"
        voice_id = "cosyvoice-v2-prefix-2b8af8aa641345bbb715e58f0079c2a1"
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
    get_audio("zhāo 辞白帝彩云间。千里江陵一 rì huán。", "test.mp3")