from dotenv import load_dotenv
import os
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import MCPTool, PromptAgentDefinition
from azure.identity import DefaultAzureCredential

load_dotenv()

AGENT_NAME = "MCPAgent"
PROJECT_ENDPOINT = os.getenv("PROJECT_ENDPOINT")
MODEL_NAME = os.getenv("MODEL_DEPLOYMENT_NAME")
MCP_SERVER_NAME = os.getenv("MCP_SERVER_NAME")
connection_id = ""

project_client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=DefaultAzureCredential())

openai_client = project_client.get_openai_client()

# Creating MCP Server Connection Id

for conn in project_client.connections.list():
    if conn.name == MCP_SERVER_NAME:
        connection_id = conn.id
        break

print(f"The MCP Connection Id is : {connection_id}")


# Creating MCP tool for Agent to use
mcp_tool = MCPTool(
    server_label="microsoft_learn_server",
    server_url="https://learn.microsoft.com/api/mcp",
    require_approval="never",
    project_connection_id=connection_id
) 

# Creating the MCP Agent
agent = project_client.agents.create_version(
    agent_name = AGENT_NAME,
    definition=PromptAgentDefinition(
        model = MODEL_NAME,
        instructions = "You are intelligent assistant that can interact with Microsoft Learn MCP Server",
        tools=[mcp_tool] 
    ),
)

print("Agent created successfully...")
print(f"Agent Id : {agent.id}")
print(f"Agent Name : {agent.name}")




