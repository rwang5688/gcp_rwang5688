#!/bin/bash
# set env vars
. ../env.sh

# upload CSV file
echo "[CMD] python3 upload_credentials.py"
python3 ./upload_credentials.py

