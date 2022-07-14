#!/bin/bash

echo "Starting the application..."

set +euo pipefail
source  ~/.bashrc
conda activate IA

# Re-enable strict mode:
set -euo pipefail

./server.py