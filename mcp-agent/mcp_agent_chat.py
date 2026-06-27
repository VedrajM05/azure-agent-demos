# from mcp_agent_create import MCP_SERVER_NAME, MODEL_NAME, PROJECT_ENDPOINT, AGENT_NAME
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
import os


load_dotenv()

AGENT_NAME = "MCPAgent"
PROJECT_ENDPOINT = os.getenv("PROJECT_ENDPOINT")
MODEL_NAME = os.getenv("MODEL_DEPLOYMENT_NAME")
MCP_SERVER_NAME = os.getenv("MCP_SERVER_NAME")

project_client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=DefaultAzureCredential())

agent = project_client.agents.get(AGENT_NAME)
print(f"Agent : {agent.name} loaded successfully")

openai_client = project_client.get_openai_client()


# Creating conversation object for MCP Agent Chat
conversation  = openai_client.conversations.create()
print(f"Conversation Id : {conversation.id}")

# Create first user query to be fired to MCP Agent
user_query = "Can you please help me with latest AI-103 exam preparation topics?"

response = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={
        "agent_reference":{
            "type":"agent_reference",
            "name" : AGENT_NAME
        }
    },
    input=user_query
)

print(f"Agent Response : {response.output_text}")