#!/bin/bash
# set env vars
. ../env.sh

# upload JSON file
echo "[CMD] python3 upload_visitors_json.py $1"
python3 ./upload_visitors_json.py $1

