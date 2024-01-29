#!/bin/bash

# Finds all Python files in the current directory and its subdirectories
find . -name "*.py" -type f -exec chmod u+x {} \;
read -p "Enter your commit message here: " commit_msg

git add .
git commit -m "$commit_msg"
git push

echo "Permissions for Python files updated to u+x."