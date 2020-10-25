#!/bin/bash
# set env vars
. ../env.sh

# deploy cloud function
gcloud functions deploy --region=$TARGET_REGION update_visitors \
--runtime python38 \
--env-vars-file=env_vars.yml \
--trigger-resource $NEWGARDEN_VISITORS_DATA_BUCKET \
--trigger-event google.storage.object.finalize

