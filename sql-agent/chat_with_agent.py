from dotenv import load_dotenv
import os
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition
from azure.identity import DefaultAzureCredential

load_dotenv()

AGENT_NAME = "SalesAnalyticsAgent"
PROJECT_ENDPOINT = os.getenv("PROJECT_ENDPOINT")
MODEL_NAME = os.getenv("MODEL_DEPLOYMENT_NAME")
container_id = ""
file_id = ""

project_client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=DefaultAzureCredential())

agent = project_client.agents.get("SalesAnalyticsAgent")
print(f"Agent : {agent.name} loaded successfully")

openai_client = project_client.get_openai_client()

# print(type(openai_client))
# print(dir(openai_client))


# Create a conversation

conversation  = openai_client.conversations.create()
print(f"Conversation Id : {conversation.id}")


response  = openai_client.responses.create(
    model=MODEL_NAME,
    conversation=conversation.id,
    # input = "What kind of Sales Analytics can you help me with?"
    input="""
        Create a bar chart. Use ProductName on X-axis and Price on Y-axis.Use the uploaded products.csv file
    """,
    extra_body={ 
        "agent_reference" : 
        {
            "type":"agent_reference",
            "name" : AGENT_NAME
        }
    }
)

# print(response)

for item in response.output:
    if item.type == "message":
        for content in item.content:
            for ann in content.annotations:
                if ann.type == "container_file_citation":
                    container_id = ann.container_id
                    file_id = ann.file_id

print(f"Container Id {container_id}")
print(f"File Id {file_id}")

content = openai_client.containers.files.content.retrieve(
    container_id=container_id,
    file_id=file_id
)

with open("product_bar_chart.png", "wb") as f:
    f.write(content.read())

print("Chart downloaded successfully.")









# list and print all Agents
# agents = list(project_client.agents.list())
# print(f"Found {len(agents)} agents")
# for agent in agents:
#     print(f"Name : {agent.name}")
#     print(f"Version : {agent.versions}")
