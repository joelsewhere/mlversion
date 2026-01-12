from pyiceberg.catalog import load_catalog
import pyarrow as pa
import pathlib, dotenv

assert dotenv.load_dotenv(pathlib.Path(__file__).parent.parent / '.env')


# Define catalog properties
catalog_name = "glue_catalog"
database_name = "your_database_name" # e.g., "iceberg_catalog"
table_name = "your_table_name"
s3_bucket_path = "s3://mlversion-test/warehouse"

# Load the Glue catalog
catalog = load_catalog(catalog_name, **{
    "type": "glue",
    "warehouse": s3_bucket_path
})
print(f"Catalog '{catalog_name}' loaded successfully.")

# Create a sample PyArrow table (dataframe alternative)
schema = pa.schema([
    pa.field("city", pa.string()),
    pa.field("lat", pa.float64()),
    pa.field("long", pa.float64())
])
data = pa.Table.from_pylist([
    {"city": "Amsterdam", "lat": 52.371807, "long": 4.896029},
    {"city": "San Francisco", "lat": 37.773972, "long": -122.431297}
], schema=schema)

# --- Write to S3 ---
# If the table doesn't exist, create it.

try:
    # Create the namespace (database)
    catalog.create_namespace(database_name)
    print(f"Database '{database_name}' created successfully.")
except Exception as e:
    print(f"Error creating database: {e}")


try:
    table = catalog.create_table(
        f"{database_name}.{table_name}", 
        schema, 
        location=f"{s3_bucket_path}/{database_name}/{table_name}"
    )
except Exception as e:
    print(f"Table already exists or creation failed: {e}. Loading existing table.")
    table = catalog.load_table(f"{database_name}.{table_name}")

# Append data to the table. PyIceberg handles the file writes to S3 automatically.
table.append(data)
print(f"Data written to S3 for table '{table_name}'.")


# --- Read from S3 ---
# Read the data back from the Iceberg table
scanned_data = table.scan().to_arrow()
print("Data read from S3:")
print(scanned_data)