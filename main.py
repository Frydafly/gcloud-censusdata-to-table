
# Import the libraries
import os
from google.cloud import bigquery
import google.auth
import json
import csv

# Set the environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

# ask user the name of the dataset they will write to
dataset_id = input("Enter the name of the dataset in bigquery you want to write to: ")
table_id = input("Enter the name of the table in bigquery you want to write to: ")
location = input("Enter the location of the table in bigquery you want to write to: ")   

def read_service_account_key():
    # Read the service account key file
    with open("key.json", "r") as f:
        key = json.load(f)

    # Extract the project ID from the key file
    project_id = key["project_id"]
    return project_id

def read_sql_query():
    # Set the file path for the query
    file_path = "query.sql"

    # Read the query from the file
    with open(file_path, "r") as f:
        query = f.read()

    return query

# create bigquery table from query
def run_query_and_load_to_bq(project_id, dataset_id, table_id, query, location):
    # Create a client object
    client = bigquery.Client(project=project_id)
    
    # Set up the table creation job
    job_config = bigquery.QueryJobConfig()
    table_ref = client.dataset(dataset_id).table(table_id)
    job_config.destination = table_ref

    # Run the query and create the table
    query_job = client.query(query, job_config=job_config, location=location)
    query_job.result()
    
    #get the results
    results = query_job.result()
    
    return results

# display results using csv writer
def display_results_csv(results):
    with open('results.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(results.schema)
        for row in results:
            writer.writerow(row)


if __name__ == "__main__":
    # Read the service account key file
    project_id = read_service_account_key()

    # Read the query from the query.sql file
    query = read_sql_query()

    # Run the query
    results = run_query_and_load_to_bq(project_id, dataset_id, table_id, query, location)
    # Display the results as a table
    print(f'Query results saved to table {table_id} in dataset {dataset_id}')

    # Display the results as csv
    display_results_csv(results)
    print('Query results saved to csv file')
    
    
    
    
    