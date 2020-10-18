#!/bin/bash
# set env vars
. ../env.sh

# deploy cloud function
gcloud functions deploy --region=$TARGET_REGION create_visitors \
--runtime python38 \
--trigger-resource $NEWGARDEN_VISITORS_CSV_DATA_BUCKET \
--trigger-event google.storage.object.finalize

