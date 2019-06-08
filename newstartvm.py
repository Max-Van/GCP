"""
BEFORE RUNNING:
---------------
1. If not already done, enable the Compute Engine API
   and check the quota for your project at
   https://console.developers.google.com/apis/api/compute
2. This sample uses Application Default Credentials for authentication.
   If not already done, install the gcloud CLI from
   https://cloud.google.com/sdk and run
   `gcloud beta auth application-default login`.
   For more information, see
   https://developers.google.com/identity/protocols/application-default-credentials
3. Install the Python client library for Google APIs by running
   `pip install --upgrade google-api-python-client`
"""
from pprint import pprint

from googleapiclient import discovery
#from oauth2client.client import GoogleCredentials
from google.auth import compute_engine

#credentials = GoogleCredentials.get_application_default()

#credentials = compute_engine.Credentials()


from google.oauth2 import service_account

#servername=input('Which Server? 1 : max-server; 2: win \n')
#if servername == '1':
SERVICE_ACCOUNT_FILE = '/Users/max/Downloads/hubcrms-6acbadeaae4e.json'
    #servername='max2'
instance = 'max2'
zone = 'us-central1-a'
project = 'hubcrms'
#elif servername == '2':
#    SERVICE_ACCOUNT_FILE = '/Users/max/Downloads/maxproject101-621fc75e5639.json'
#    instance = 'win'
#    zone = 'us-central1-a'
#else :
#    print('Invalid input, bye.')
#    quit()



SCOPES = ['https://www.googleapis.com/auth/cloud-platform','https://www.googleapis.com/auth/compute']

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


service = discovery.build('compute', 'v1', credentials=credentials)

# Project ID for this request.
#project = 'maxproject101'  # TODO: Update placeholder value.

# The name of the zone for this request.
  # TODO: Update placeholder value.

# Name of the instance resource to start.
#instance = 'max-server'  # TODO: Update placeholder value.

request = service.instances().start(project=project, zone=zone, instance=instance)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)
