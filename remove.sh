#!/bin/bash
# set env vars
. ./env.sh


function remove_buckets () {
  for BUCKET in "${BUCKETS[@]}"
  do
    echo ----------[ removing $BUCKET ]----------
    gsutil -m rm -r gs://$BUCKET
  done
}


function remove_functions () {
  for FUNCTION in "${FUNCTIONS[@]}"
  do
    echo ----------[ removing $FUNCTION ]----------
    cd $FUNCTION
    . ./remove.sh
    cd ..
  done
}


# remove cloud functions
FUNCTIONS=(create_visitors)
remove_functions

# remove project artifacts and function sources buckets
BUCKETS=($PROJECT_ARTIFACTS_BUCKET \
            $FUNCTION_SOURCES_BUCKET)
remove_buckets

# remove global resources
BUCKETS=($SERVICE_ACCOUNT_DATA_BUCKET \
            $NEWGARDEN_CUSTOMERS_DATA_BUCKET \
            $NEWGARDEN_VISITORS_DATA_BUCKET)
remove_buckets

