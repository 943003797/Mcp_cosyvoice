from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Say Hello")

@mcp.tool()
def say_hello(name: str) -> str:
    """
    Say hello to a person
    """
    return f"Hello ddddddddddddddd!"

if __name__ == "__main__":
    mcp.run(transport='stdio')
