#!/bin/bash

# Set the paths
repo_path="/Users/dhruv/Desktop/research/swe/django_menial"
config_file="config/default_from_url.yaml"
cost_limit="20.00"

# Iterate over each file in the problem_statements folder
for file in /Users/dhruv/Desktop/research/swe/problem_statements/instructions_by_type/Descriptive/*; do
    if [[ -f $file ]]; then  # Check if it's a file
        echo "Running for $file"
        python run.py --model_name azure:gpt4 \
          --data_path "$file" \
          --repo_path "$repo_path" \
          --config_file "$config_file" \
          --per_instance_cost_limit "$cost_limit" \
          --cache_task_images
    fi
done