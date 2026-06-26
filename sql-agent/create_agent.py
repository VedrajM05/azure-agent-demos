from dotenv import load_dotenv
import os
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition, CodeInterpreterTool, AutoCodeInterpreterToolParam
from azure.identity import DefaultAzureCredential

load_dotenv()

AGENT_NAME = "SalesAnalyticsAgent"
PROJECT_ENDPOINT = os.getenv("PROJECT_ENDPOINT")

project_client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=DefaultAzureCredential())

code_tool = CodeInterpreterTool(container=AutoCodeInterpreterToolParam(
    file_ids=["assistant-YNA9HbEu3wqjCNG2qxMSjw"]
))


agent = project_client.agents.create_version(
    agent_name = AGENT_NAME,
    definition=PromptAgentDefinition(
        model = os.getenv("MODEL_DEPLOYMENT_NAME"),
        instructions = """
            You are a Sales Analytics Agent.

            Capabilities:

            1. Generate SQL Server queries for sales analytics.

            2. Analyze SQL query results.

            3. Use the Code Interpreter tool whenever:
            - the user requests a chart
            - the user requests a graph
            - the user requests visualization
            - the user requests statistical analysis

            Restrictions:

            - Generate only SQL Server compatible SQL.
            - Generate only SELECT statements.
            - Never generate INSERT, UPDATE, DELETE, DROP, ALTER or TRUNCATE statements.
                    """,
            tools=[code_tool]
    ),
)

print("Agent created successfully...")
print(f"Agent Id : {agent.id}")
print(f"Agent Name : {agent.name}")