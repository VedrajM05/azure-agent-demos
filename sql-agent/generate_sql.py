from dotenv import load_dotenv
import os
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition
from azure.identity import DefaultAzureCredential
from execute_sql import execute_sql
import pyodbc

from export_to_csv import export_csv

load_dotenv()

AGENT_NAME = "SalesAnalyticsAgent"
PROJECT_ENDPOINT = os.getenv("PROJECT_ENDPOINT")
MODEL_NAME = os.getenv("MODEL_DEPLOYMENT_NAME")
FILENAME = "products.csv"

project_client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=DefaultAzureCredential())

agent = project_client.agents.get("SalesAnalyticsAgent")
print(f"Agent : {agent.name} loaded successfully")

openai_client = project_client.get_openai_client()

# Create a conversation

conversation  = openai_client.conversations.create()
print(f"Conversation Id : {conversation.id}")


schema = """
Database Schema

Products(
    ProductId,
    ProductName,
    Price
)

Customers(
    CustomerId,
    CustomerName
)

Orders(
    OrderId,
    CustomerId,
    ProductId,
    Quantity
)

Rules:
- Generate ONLY SQL
- Use SQL Server syntax
- Return only SQL
- No explanations
- Read-only queries only

"""
question = "Show top 5 products by price"


response  = openai_client.responses.create(
    model=MODEL_NAME,
    instructions=schema,
    input = question
)

query = response.output[1].content[0].text

print(f"SQL Query :  {query}")

# print(pyodbc.drivers())

results = execute_sql(query)

for row in results:
    print(row)


export_csv(results, FILENAME)


print(f"CSV Exported Successfully : {FILENAME}")

with open(FILENAME, "rb") as file:
    uploaded_file = openai_client.files.create(
        file=file,
        # Tells the API how you intend to use this file. Setting this to 'assistants' is mandatory 
        # so you can attach it to an Assistant for features like the Code Interpreter or File Search
        purpose="assistants"
    )

print(f"File uploaded successfully")
print(f"File Id {uploaded_file.id}")
print(f"File Name {uploaded_file.filename}")