#!/bin/bash

# Check if commit message is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <commit-message>"
  exit 1
fi

COMMIT_MESSAGE=$1

# Run tests
python3 -m unittest test_simple_api.py

# Check if tests passed
if [ $? -eq 0 ]; then
  # Commit changes
  git add simple_api.py test_simple_api.py
  git commit -m "$COMMIT_MESSAGE"

  # Push changes
  git push

  echo "Changes committed and pushed with commit message: '$COMMIT_MESSAGE'"
else
  echo "Tests failed. Aborting commit and push."
fi