import pyodbc


def execute_sql(query):
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=SalesAnalyticsDB;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes"
    )

    cursor = conn.cursor()
    cursor.execute(query)

    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()

    results = []

    for row in rows:
        results.append(dict(zip(columns, row)))
        # results.append(f"\n")

    conn.close()

    return results
