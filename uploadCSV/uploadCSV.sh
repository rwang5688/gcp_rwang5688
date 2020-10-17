#!/bin/bash
# set env vars
. ./env.sh

# import GCP credentials


# upload CSV file
echo "[CMD] python3 uploadCSV.py $1"
python3 ./uploadCSV.py $1

