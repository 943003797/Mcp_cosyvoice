## 📝 简介

本项目是一个基于Python的Mcp server应用程序，用于调用Ali CosyVoice1接口，转换Text为音频到指定目录。

## 🚀 使用步骤

### 创建Python 3.12虚拟环境
uv venv .venv -p 3.12

### 激活虚拟环境（Windows）
.venv\Scripts\activate

### 安装项目依赖
uv sync

### Autogen中调用
```bash
shiciToAudio = await mcp_server_tools(
        StdioServerParams(
            command="uv",
            args=[
                "--directory",
                "../../Mcp/Mcp_cosyvoice",
                "run",
                "server_json.py"
            ],
            env={
                "DASHSCOPE_API_KEY": "API_KEY",
            }
        )
    )