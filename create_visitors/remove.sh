#!/bin/bash
# set env vars
. ../env.sh

gcloud functions delete -q create_visitors

