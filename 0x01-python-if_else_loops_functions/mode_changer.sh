#!/bin/bash

# Finds all Python files in the current directory and its subdirectories
find . -name "*.py" -type f -exec chmod u+x {} \;

echo "Permissions for Python files updated to u+x."
