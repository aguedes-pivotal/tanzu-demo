#!/bin/bash
set -e

pip install --no-cache-dir -r $1
for filename in $2/*.py; do
        python "$filename"
done
