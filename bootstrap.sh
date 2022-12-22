#!/usr/bin/bash

# This is a script to initialize the Google Cloud SDK and create a service account and key

# Ask the user for their project ID and store it in a variable
read -p "Enter your existing google cloud project ID: " project_id

# Ask the user for their service account name and store it in a variable
read -p "Create a service account name you want to use (only dashes and letters) " service_account_name


# Initialize the SDK
gcloud init

# enable the bigquery API
gcloud services enable bigquery.googleapis.com

# Create a service account
gcloud iam service-accounts create $service_account_name

# Create a key for the service account
gcloud iam service-accounts keys create key.json --iam-account=$service_account_name@"$project_id".iam.gserviceaccount.com

# grant the service account the bigquery admin role
gcloud projects add-iam-policy-binding $project_id --member serviceAccount:$service_account_name@"$project_id".iam.gserviceaccount.com --role roles/bigquery.admin


