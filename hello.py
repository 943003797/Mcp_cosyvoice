from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Say Hello")

@mcp.tool()
def say_hello(name: str) -> str:
    """
    使用这个工具可以获取配音
    """
    
    return f"Hello ddddddddddddddd!"

if __name__ == "__main__":
    mcp.run(transport='stdio')
