#!/bin/bash

# Function to crop white spaces from PDF files using pdf-crop-margins
crop_pdf() {
    local file="$1"
    echo "Processing $file..."
    pdf-crop-margins -v -p 5 "$file"
}

# Find all PDF files in the current directory and its subdirectories
find . -type f -name "*.pdf" | while IFS= read -r pdf_file; do
    crop_pdf "$pdf_file"
done

