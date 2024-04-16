import pyodbc
import os

conn = pyodbc.connect(
  "Driver=/Library/simba/spark/lib/libsparkodbc_sb64-universal.dylib;" +
  f"Host={os.getenv('DATABRICKS_HOST')};" +
  "Port=443;" +
  f"HTTPPath={os.getenv('DATABRICKS_HTTP_PATH')};" +
  "SSL=1;" +
  "ThriftTransport=2;" +
  "AuthMech=3;" +
  "UID=token;" +
  f"PWD={os.getenv('DATABRICKS_TOKEN')}",
  autocommit = True
)

# Run a SQL query by using the preceding connection.
cursor = conn.cursor()
cursor.execute("SELECT * FROM samples.nyctaxi.trips")

# Print the rows retrieved from the query.
for row in cursor.fetchall():
  print(row)
