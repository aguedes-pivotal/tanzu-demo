#!/bin/bash
set -e


echo "Live tests: http://ae4de69e06ae24c19a539949ff38ecb8-1340096117.eu-west-1.elb.amazonaws.com/grid/admin/live?refresh=5&only_active_sessions=true"
pip install --no-cache-dir -r $1
for filename in $2/*.py; do
        python "$filename"
done
