# AI SQL Agent using Azure AI Foundry

## Project Overview

This project demonstrates how to build an **AI-powered SQL Analytics Agent** using **Azure AI Foundry**.

Instead of directly querying a database, users interact with the agent using **natural language**.

The application:

* Connects to Azure AI Foundry
* Uses a Versioned AI Agent
* Generates SQL queries using GPT
* Executes SQL against SQL Server
* Converts query results into CSV
* Uploads the CSV into Azure AI Foundry
* Uses the **Code Interpreter Tool**
* Generates charts automatically
* Returns generated artifacts (PNG)

---

# Architecture

```
                User

                  │

                  ▼

        Azure AI Foundry Agent

                  │

                  ▼

          GPT Model (gpt-chat-latest)

                  │

          Generates SQL Query

                  │

                  ▼

         Python Application (.NET equivalent)

                  │

                  ▼

            SQL Server Database

                  │

           Query Results (Rows)

                  │

                  ▼

           Export Results to CSV

                  │

                  ▼

        Upload CSV to Foundry

                  │

                  ▼

      Azure Code Interpreter Tool

                  │

          Generates Python Code

                  │

                  ▼

         Executes Python in Sandbox

                  │

                  ▼

         Generated PNG Bar Chart
```

---

# Technologies Used

* Azure AI Foundry
* Azure AI Projects SDK
* Azure Identity
* Azure OpenAI Responses API
* SQL Server
* pyodbc
* Python
* Pandas
* Matplotlib
* Code Interpreter Tool

---

# Prerequisites

Before running this project ensure you have:

* Azure Subscription
* Azure AI Foundry Project
* GPT deployment (gpt-chat-latest)
* Python 3.11+
* SQL Server
* SSMS
* ODBC Driver 18 for SQL Server

---

# Required Python Packages

```bash
pip install azure-ai-projects
pip install azure-identity
pip install python-dotenv
pip install pyodbc
pip install openai
```

---

# Project Structure

```
foundry-sql-agent/

│

├── create_agent.py

├── generate_sql.py

├── execute_sql.py

├── export_to_csv.py

├── upload_file.py

├── chat_with_agent.py

├── SQLScripts.sql

├── products.csv

├── .env

└── README.md
```

---

# Environment Variables

Create a file named:

```
.env
```

Add the following values.

```env
PROJECT_ENDPOINT=https://<your-ai-foundry-project>.services.ai.azure.com/api/projects/<project-name>

MODEL_DEPLOYMENT_NAME=gpt-chat-latest
```

## Where to get PROJECT_ENDPOINT

Azure AI Foundry

↓

Project

↓

Overview

↓

Project Endpoint

Example

```
https://myproject.services.ai.azure.com/api/projects/MyProject
```

---

## MODEL_DEPLOYMENT_NAME

Azure AI Foundry

↓

Models + Endpoints

↓

Deployments

↓

Deployment Name

Example

```
gpt-chat-latest
```

---

# Authentication

The project uses Azure Identity.

Login once:

```bash
az login
```

Verify:

```bash
az account show
```

The SDK automatically authenticates using:

```python
DefaultAzureCredential()
```

No API keys are required.

---

# Database Setup

Run:

```
SQLScripts.sql
```

This creates

Products

Customers

Orders

tables.

Sample data is inserted automatically.

---

# Step-by-Step Execution

## Step 1

Connect to Azure AI Foundry

Concept Learned

* AIProjectClient
* Azure Identity

Sample

```python
project_client = AIProjectClient(
    endpoint=os.getenv("PROJECT_ENDPOINT"),
    credential=DefaultAzureCredential()
)
```

---

## Step 2

Create Versioned Agent

Concept Learned

* Versioned Agents
* PromptAgentDefinition

Sample

```python
agent = project_client.agents.create_version(...)
```

---

## Step 3

Get OpenAI Client

Concept Learned

* OpenAI Client from Foundry

```python
openai_client = project_client.get_openai_client()
```

---

## Step 4

Generate SQL

Concept Learned

* Responses API
* Prompt Engineering

Example

```
Show top 5 products by price
```

Generated SQL

```sql
SELECT TOP 5
ProductId,
ProductName,
Price
FROM Products
ORDER BY Price DESC;
```

---

## Step 5

Execute SQL

Concept Learned

* pyodbc
* SQL Server

```python
cursor.execute(sql_query)
```

---

## Step 6

Export Results

Concept Learned

* CSV Generation

Example

```
ProductId,ProductName,Price
1,Laptop,800
```

---

## Step 7

Upload File

Concept Learned

* Azure AI Foundry File Upload

```python
uploaded_file = openai_client.files.create(...)
```

---

## Step 8

Code Interpreter

Concept Learned

* Auto Code Interpreter Container
* Tool Invocation
* Generated Artifacts

The LLM automatically generated Python similar to:

```python
df = pd.read_csv(...)

plt.bar(df["ProductName"], df["Price"])

plt.savefig(...)
```

The Python was executed inside an Azure sandbox.

---

# Azure AI Concepts Covered

## AIProjectClient

Used to connect to Azure AI Foundry Projects.

---

## DefaultAzureCredential

Provides Azure authentication without API keys.

---

## Versioned Agents

Instead of modifying an agent directly, Azure AI Foundry creates versions.

Version 1

↓

Version 2

↓

Version 3

This enables safe evolution of AI agents.

---

## Responses API

The latest OpenAI API recommended by Microsoft.

Used instead of Chat Completions.

---

## Agent Reference

Instead of calling the model directly, the application invokes a Foundry Agent.

This separates application logic from AI behavior.

---

## SQL Generation

GPT generates SQL Server compatible SELECT queries.

---

## SQL Execution

Python executes generated SQL using pyodbc.

---

## Code Interpreter Tool

Allows GPT to execute Python.

Capabilities

* pandas
* matplotlib
* numpy
* CSV analysis
* Chart generation

---

## Auto Code Interpreter Container

Uploaded files are mounted inside a temporary execution container.

Example

```
cntr_xxxxxxxxx
```

---

## Generated Artifacts

The Code Interpreter generated:

```
product_bar_chart.png
```

inside the execution container.

---

# Sample Prompts

```
Show top 5 products by price
```

```
Create a bar chart using ProductName and Price
```

```
Show the most expensive products
```

```
Generate SQL for products costing more than $100
```

---

# AI-102 Skills Covered

✔ Azure AI Foundry SDK

✔ Azure Identity

✔ Versioned Agents

✔ Responses API

✔ Agent Reference

✔ Prompt Engineering

✔ SQL Generation

✔ SQL Execution

✔ CSV Generation

✔ File Upload

✔ Code Interpreter

✔ Generated Artifacts

✔ Azure Sandbox Execution

---

# Future Improvements

* Tool Calling instead of local SQL execution
* Semantic Kernel Integration
* LangGraph Workflow
* Azure SQL Database
* Power BI Integration
* RAG using Azure AI Search
* Multi-Agent Collaboration
* Streaming Responses

---

# Final Learning Outcome

By completing this project you have built an enterprise-style AI application demonstrating:

* Natural Language → SQL
* SQL → Data
* Data → CSV
* CSV → Code Interpreter
* Code Interpreter → Python
* Python → Visualization

This project combines multiple Azure AI Foundry capabilities into a single end-to-end AI solution and serves as an excellent portfolio project for Azure AI Engineer (AI-102) preparation.
