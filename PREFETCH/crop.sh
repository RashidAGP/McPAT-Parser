#!/bin/bash

# Loop through all PDF files in the current directory
for file in *.pdf; do
    # Check if the file is a regular file
    if [ -f "$file" ]; then
        # Use pdfjam to remove margins
        pdfjam --fitpaper true --clip true -- "$file"
        
        echo "Processed: $file"
    fi
done

