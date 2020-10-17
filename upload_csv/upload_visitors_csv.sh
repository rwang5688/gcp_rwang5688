#!/bin/bash
# set env vars
. ./env.sh

# upload CSV file
echo "[CMD] python3 upload_visitors_csv.py $1"
python3 ./upload_visitors_csv.py $1

