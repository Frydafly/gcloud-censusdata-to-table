## Instructions 

## Before you get started

- Create or select a google cloud project in the console. 
- Create or make a note of the dataset you want to load your data to

### STEP 1: Install Dependencies 

**Use bash script**
You can run `bash dependency_install.sh` to install various dependencies for the project. This will run a terminal program to install Google Cloud SDK, upgrade google cloud bigquery, and upgrade google auth. You can also copy and paste these to your terminal and run individual programs appropriate for your install. 

**Requirements.txt**
See also the requirements.txt document for specific requirements. 

### STEP 2: Run the bootstrap script

**You only run this the first time**

The `bootstrap.sh` script will initialize the Google Cloud SDK, load your Project ID,  enable the Bigquery API, create a service account with bigquery admin permissions, and load a service account key to your working directory called `key.json`

### Step 3: Run the python script
Recommended: Use a virtual environment. You can use pipenv. Remember to run `pipenv install` and `pipenv shell` to activate your virtual environment. 

Then run `python main.py`. Follow the prompts!

There are two outputs, a CSV, and a bigquery table!


### GeoViz!

- Link to GeoViz: [GeoViz]<https://bigquerygeoviz.appspot.com/project/woven-ceremony-355016/job/bquxjob_45fdc7e4_1853725b751/location/US>

