#!/bin/bash
# set env vars
. ./env.sh


function make_buckets () {
  for BUCKET in "${BUCKETS[@]}"
  do
    echo ----------[ making $BUCKET ]----------
    gsutil mb -c standard -l $TARGET_REGION gs://$BUCKET
  done
}


function deploy_functions () {
  for FUNCTION in "${FUNCTIONS[@]}"
  do
    echo ----------[ deploying $FUNCTION ]----------
    cd $FUNCTION
    . ./deploy.sh
    cd ..
  done
}


# create global resources
BUCKETS=($SERVICE_ACCOUNT_DATA_BUCKET \
            $NEWGARDEN_CUSTOMERS_DATA_BUCKET \
            $NEWGARDEN_VISITORS_DATA_BUCKET)
make_buckets

# deploy cloud functions
FUNCTIONS=(create_visitors)
deploy_functions

