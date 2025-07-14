#!/bin/bash

# Navigate to project root
cd ~/p1_system || { echo "Project folder not found"; exit 1; }

# Add all changes
git add .

# Commit with timestamp
commit_msg="Update from ONE_SYSTEM at $(date '+%Y-%m-%d %H:%M:%S')"
git commit -m "$commit_msg"

# Push to main branch
git push origin main
