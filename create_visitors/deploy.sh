#!/bin/bash
# set env vars
. ./env.sh

gcloud functions deploy --region=us-central1 create_visitors \
--runtime python38 \
--trigger-resource $NEWGARDEN_VISITORS_CSV_DATA_BUCKET \
--trigger-event google.storage.object.finalize

