#!/bin/bash
set -e

echo "Starting compilation of all recipes..."

# Find all .tex files, excluding preamble.tex
find . -name "*.tex" ! -name "preamble.tex" -print0 | while IFS= read -r -d '' file; do
    dir=$(dirname "$file")
    base=$(basename "$file")
    
    echo "=========================================="
    echo "Compiling $base in $dir"
    echo "=========================================="
    
    # Run compilation in a subshell to avoid changing directory for the main loop
    (
        cd "$dir" || exit 1
        # Run pdflatex
        pdflatex -interaction=nonstopmode -halt-on-error "$base"
    )
done

echo "All recipes compiled successfully."
