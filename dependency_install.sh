#!/usr/bin/bash

# This is a script to install all the dependencies for the project

# Install the Google Cloud SDK
curl https://sdk.cloud.google.com | bash

# install google cloud bigquery
pip install --upgrade google-cloud-bigquery

# upgrade google auth
pip install google-auth --upgrade

