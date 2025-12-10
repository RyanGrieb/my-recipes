#!/bin/bash
set -e

echo "Starting compilation of all recipes..."

# Initialize the master LaTeX file
MASTER_FILE="all-recipes.tex"
echo "\documentclass{article}" > "$MASTER_FILE"
echo "\usepackage{pdfpages}" >> "$MASTER_FILE"
echo "\usepackage[paperwidth=8.5in, paperheight=11in, margin=0in]{geometry}" >> "$MASTER_FILE" # Ensure standard size
echo "\begin{document}" >> "$MASTER_FILE"

# Find all .tex files, excluding preamble and the master file itself, and sort them
find . -name "*.tex" ! -name "preamble.tex" ! -name "$MASTER_FILE" -print0 | sort -z | while IFS= read -r -d '' file; do
    dir=$(dirname "$file")
    base=$(basename "$file")
    pdf_name="${base%.tex}.pdf"
    
    echo "=========================================="
    echo "Compiling $base in $dir"
    echo "=========================================="
    
    # Run compilation in a subshell
    if (
        cd "$dir" || exit 1
        pdflatex -interaction=nonstopmode -halt-on-error "$base"
    ); then
        # If compilation succeeded, add to master file
        # We need the path relative to the root
        # $dir starts with ./, strip it for cleaner latex paths if needed, though ./ is fine
        # We need to escape underscores in paths for LaTeX if we were printing text, 
        # but \includepdf handles filenames relatively well, though standard latex filename caveats apply.
        # Ideally, we used double quotes for the filename in \includepdf
        
        full_pdf_path="$dir/$pdf_name"
        echo "\includepdf[pages=-]{$full_pdf_path}" >> "$MASTER_FILE"
    else
        echo "Error: Failed to compile $base"
        exit 1
    fi
done

echo "\end{document}" >> "$MASTER_FILE"

echo "=========================================="
echo "Compiling All Recipes (Merged PDF)"
echo "=========================================="

pdflatex -interaction=nonstopmode -halt-on-error "$MASTER_FILE"

echo "All recipes compiled and merged successfully."
