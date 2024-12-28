import duckdb  # Import the DuckDB library
from config.config import MOTHERDUCK_TOKEN  # Import the MOTHERDUCK_TOKEN from the config file

def get_connection():
    # Establish a connection to the DuckDB database using the MOTHERDUCK_TOKEN
    return duckdb.connect(f"md:?token={MOTHERDUCK_TOKEN}")

def get_reviews_for_sentiment():
    conn = get_connection()  # Get a connection to the database
    query = """
    SELECT 
        _airbyte_raw_id,
        content,
        score,
        _airbyte_extracted_at
    FROM dropbox_reviews
    WHERE content IS NOT NULL AND content != ''
    """  # Define the SQL query to select relevant review data
    return conn.execute(query).fetch_df()  # Execute the query and fetch the results as a DataFrame