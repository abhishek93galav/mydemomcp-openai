import os
from mcp.server.fastmcp import FastMCP
from openai import OpenAI
#from fastapi import FastAPI
#from fastapi.middleware.cors import CORSMiddleware
# Initialize FastMCP with name and transport type

# Using host and port to be more specific about connection
mcp = FastMCP("SummarizationServer", host="0.0.0.0", port=8000)
# Use your own key here
os.environ['OPENAI_API_KEY'] = <api key goes here>
# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# a sample tool to summarize text using the gpt-4o model
@mcp.tool()
async def summarize_text(text: str) -> str:
    """
    Summarizes a long text into a concise paragraph using OpenAI.
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Summarize the following text briefly."},
            {"role": "user", "content": text}
        ]
    )
    # result from openai
    return response.choices[0].message.content

if __name__ == "__main__":
    # Start the server
    mcp.run(transport="streamable-http")
