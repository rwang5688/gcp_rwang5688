#!/bin/bash
# set env vars
. ../env.sh

gcloud functions delete -q update_visitors

