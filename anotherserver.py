from mcp.server.fastmcp import FastMCP

# Creating a demo FastMCP server
mcp = FastMCP("My demo sse Server", host="0.0.0.0", port=8000)

# Add a sample tool
@mcp.tool()
def calculate_sum(a: int, b: int) -> int:
    """Adds two numbers together."""
    return a + b

# Adding a resource
@mcp.resource("echo://{message}")
def echo_resource(message: str) -> str:
    """Returns the message provided in the URI."""
    return f"Resource content: {message}"

if __name__ == "__main__":
    # Start the server using SSE transport
    mcp.run(transport="sse")
