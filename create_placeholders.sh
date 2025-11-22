#!/bin/bash

# Create placeholder files for remaining translations
# These will be translated in final batch

BASE_RUS="/Users/alexeykrolmini/Downloads/Code/aibook/Rus"
BASE_ENG="/Users/alexeykrolmini/Downloads/Code/aibook/Eng"

# Function to create English path from Russian path
translate_path() {
    local rus_path="$1"
    local eng_path="${rus_path//$BASE_RUS/$BASE_ENG}"
    
    # Apply all directory name translations
    eng_path="${eng_path//Доп. файлы/Additional Files}"
    eng_path="${eng_path//Исходные тексты/Source Texts}"
    eng_path="${eng_path//1_Введение/1_Introduction}"
    eng_path="${eng_path//2_Инструкция по выживанию/2_Survival Guide}"
    eng_path="${eng_path//Финальные тексты/Final Texts}"
    
    echo "$eng_path"
}

# Export for use in subshell
export -f translate_path
export BASE_RUS BASE_ENG

# Find all MD files and count them
echo "Counting remaining files to translate..."
find "$BASE_RUS" -name "*.md" -type f | wc -l

