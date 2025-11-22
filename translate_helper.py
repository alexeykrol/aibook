#!/usr/bin/env python3
"""
Helper script to manage translation of Russian markdown files to English.
This creates the file list and directory mappings.
"""

import os
import json

# Define directory mappings from Russian to English
DIR_MAPPINGS = {
    "1. Что конкретно вы теперь можете с помощью ИИ?": "1. What You Can Now Do With AI",
    "Доп. файлы": "Additional Files",
    "Идеи книги": "Book Ideas",
    "Исходные тексты": "Source Texts",
    "1_Введение": "1_Introduction",
    "2_Инструкция по выживанию": "2_Survival Guide",
    "Текст": "Text",
    "Текст-1": "Text-1",
    "база текстов": "text base",
    "Википедия ИИ": "AI Encyclopedia",
    "Уровень 10": "Level 10",
    "Уровень 2": "Level 2",
    "Уровень 3": "Level 3",
    "Уровень 4": "Level 4",
    "Уровень 5": "Level 5",
    "Уровень 6": "Level 6",
    "Уровень 7": "Level 7",
    "Уровень 8": "Level 8",
    "Уровень 9": "Level 9",
    "Что двльше?": "What Next?",
    "Промо и фрагменты": "Promo and Excerpts",
    "Финальные тексты": "Final Texts",
}

def translate_path(rus_path, base_rus="Rus", base_eng="Eng"):
    """Convert Russian path to English path"""
    eng_path = rus_path.replace(base_rus, base_eng, 1)

    for rus, eng in DIR_MAPPINGS.items():
        eng_path = eng_path.replace(rus, eng)

    return eng_path

def find_all_md_files(base_dir="Rus"):
    """Find all markdown files in Rus directory"""
    md_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                md_files.append(full_path)
    return sorted(md_files)

def main():
    rus_files = find_all_md_files("Rus")

    file_mappings = []
    for rus_file in rus_files:
        eng_file = translate_path(rus_file)
        file_mappings.append({
            "source": rus_file,
            "target": eng_file
        })

    # Save to JSON
    with open("translation_mappings.json", "w", encoding="utf-8") as f:
        json.dump(file_mappings, f, ensure_ascii=False, indent=2)

    print(f"Found {len(rus_files)} markdown files")
    print(f"Mappings saved to translation_mappings.json")

    # Print first few mappings as example
    print("\nExample mappings:")
    for mapping in file_mappings[:5]:
        print(f"  {mapping['source']}")
        print(f"  -> {mapping['target']}\n")

if __name__ == "__main__":
    main()
