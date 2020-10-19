#!/bin/bash
# GCP specific environment variables
export TARGET_COUNTRY=us
export TARGET_REGION=us-central1
export PROJECT_ID=newgarden-cloud-functions
export PROJECT_NUMBER=181775686739
export PROJECT_ARTIFACTS_BUCKET=$TARGET_COUNTRY.artifacts.$PROJECT_ID.appspot.com
export FUNCTION_SOURCES_BUCKET=gcf-sources-$PROJECT_NUMBER-$TARGET_REGION

# App specific environment variables
export SERVICE_ACCOUNT_CREDENTIALS_JSON=$PROJECT_ID-9f405fe88d29.json
export SERVICE_ACCOUNT_DATA_BUCKET=newgarden-service-account-data-bucket
export NEWGARDEN_CUSTOMERS_CSV_DATA_BUCKET=newgarden-customers-csv-data-bucket
export NEWGARDEN_VISITORS_CSV_DATA_BUCKET=newgarden-visitors-csv-data-bucket
export NEWGARDEN_VISITORS_SPREADSHEET_ID="1NX2DQrM2WlVpZdUQHqoSy9jFQHiI-JlWtxCPaMVPKpk"
export NEWGARDEN_VISITORS_HEADER_RANGE_NAME="Visitors!A1:AI1"

