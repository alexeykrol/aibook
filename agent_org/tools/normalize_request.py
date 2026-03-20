#!/usr/bin/env python3
"""
Intake Normalization Tool (Mode B)
Converts free-text project descriptions into structured PROJECT_REQUEST.md.

Usage:
    python3 normalize_request.py [--input RAW_INPUT.txt] [--output PROJECT_REQUEST.md]

Reads from project_input/RAW_INPUT.txt by default.
Generates project_input/PROJECT_REQUEST.md.
"""

import argparse
import os
import re
import sys
from pathlib import Path


def find_project_root():
    """Walk up from script location to find project_input/."""
    current = Path(__file__).resolve().parent
    for _ in range(5):
        if (current / "project_input").is_dir():
            return current
        current = current.parent
    return Path(__file__).resolve().parent.parent.parent


def extract_field(text, patterns, context_lines=3):
    """Extract text matching patterns from the raw input."""
    results = []
    lines = text.split('\n')

    for i, line in enumerate(lines):
        for pattern in patterns:
            if re.search(pattern, line, re.IGNORECASE):
                # Grab this line and a few context lines after it
                chunk = []
                for j in range(i, min(i + context_lines + 1, len(lines))):
                    cleaned = lines[j].strip()
                    if cleaned and not re.match(r'^[-=#*]{3,}$', cleaned):
                        chunk.append(cleaned)
                if chunk:
                    results.append(' '.join(chunk))
                break

    return ' '.join(results).strip() if results else ''


def extract_project_name(text):
    """Try to extract a project name from the text."""
    # Look for explicit naming patterns
    patterns = [
        r'(?:called|named|name[:\s]+)\s*["\']?([^"\'.\n]+)["\']?',
        r'(?:build|create|make|develop)\s+(?:a\s+)?([A-Z][a-zA-Z0-9\s]{2,20}?)(?:\s+(?:app|application|tool|system|platform|service|website|site))',
        r'^#\s+(.+)',  # Markdown header
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
        if match:
            name = match.group(1).strip()
            if len(name) > 2 and len(name) < 60:
                return name
    return ''


def extract_goal(text):
    """Extract the main goal/what to build."""
    patterns = [
        r'(?:want|need|build|create|make|develop|implement)',
        r'(?:goal|objective|purpose|aim)',
        r'(?:should|must|will)\s+(?:be able to|have|support)',
    ]
    result = extract_field(text, patterns, context_lines=4)
    if not result:
        # Fallback: use the first substantial paragraph
        paragraphs = re.split(r'\n\s*\n', text.strip())
        for p in paragraphs:
            p = p.strip()
            if len(p) > 30:
                return p[:500]
    return result[:500] if result else ''


def extract_audience(text):
    """Extract who the project is for."""
    patterns = [
        r'(?:for|target|audience|users?|customers?|people who)',
        r'(?:aimed at|designed for|intended for)',
    ]
    return extract_field(text, patterns, context_lines=2)


def extract_features(text):
    """Extract feature list from the text."""
    features = []

    # Look for numbered or bulleted lists
    list_items = re.findall(
        r'(?:^|\n)\s*(?:[-*•]|\d+[.)]\s)\s*(.+)',
        text
    )
    for item in list_items:
        item = item.strip()
        if len(item) > 5 and len(item) < 200:
            features.append(item)

    # Look for "should/must/will" statements
    if not features:
        should_items = re.findall(
            r'(?:should|must|will|needs? to)\s+(.{10,100}?)(?:\.|$)',
            text,
            re.IGNORECASE
        )
        features.extend([s.strip() for s in should_items[:10]])

    return features[:10]  # Cap at 10


def extract_technical(text):
    """Extract technical preferences."""
    tech = {}
    # Languages
    lang_match = re.search(
        r'(?:in|using|with)\s+(Python|JavaScript|TypeScript|Go|Rust|Java|C\+\+|Ruby|PHP|Swift|Kotlin)',
        text, re.IGNORECASE
    )
    if lang_match:
        tech['language'] = lang_match.group(1)

    # Frameworks
    fw_match = re.search(
        r'(?:using|with)\s+(React|Vue|Angular|Django|Flask|FastAPI|Express|Next\.?js|Rails|Spring|Svelte)',
        text, re.IGNORECASE
    )
    if fw_match:
        tech['framework'] = fw_match.group(1)

    # Databases
    db_match = re.search(
        r'(?:using|with)\s+(PostgreSQL|MySQL|SQLite|MongoDB|Redis|Supabase|Firebase)',
        text, re.IGNORECASE
    )
    if db_match:
        tech['database'] = db_match.group(1)

    return tech


def extract_constraints(text):
    """Extract constraints mentioned in the text."""
    constraints = []
    patterns = [
        r'(?:must not|cannot|no |don\'t|avoid|without)\s+(.{10,100}?)(?:\.|$)',
        r'(?:constraint|limitation|requirement|must)\s*:?\s*(.{10,100}?)(?:\.|$)',
    ]
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        constraints.extend([m.strip() for m in matches if len(m.strip()) > 5])
    return constraints[:5]


def assess_clarity(extracted):
    """Assess which fields are clear vs. need clarification."""
    gaps = []
    if not extracted.get('goal'):
        gaps.append('goal — what exactly should be built?')
    if not extracted.get('audience'):
        gaps.append('audience — who is this for?')
    if not extracted.get('features'):
        gaps.append('features — what are the key features?')
    if not extracted.get('technical'):
        gaps.append('technical preferences — any language/framework preferences?')
    return gaps


def generate_project_request(extracted):
    """Generate structured PROJECT_REQUEST.md from extracted fields."""
    name = extracted.get('name', 'Untitled Project')
    tag = lambda v: '[extracted]' if v else '[needs_clarification]'

    features_text = ''
    if extracted.get('features'):
        for i, f in enumerate(extracted['features'], 1):
            features_text += f'{i}. {f}\n'
    else:
        features_text = '1. [needs_clarification]\n2. \n3. \n'

    tech = extracted.get('technical', {})
    tech_lang = tech.get('language', '')
    tech_fw = tech.get('framework', '')
    tech_db = tech.get('database', '')

    output = f"""# Project Request

> Auto-generated from RAW_INPUT.txt by normalize_request.py

## Project Name

{name} {tag(name)}

## What do you want to build?

{extracted.get('goal', '[needs_clarification]')} {tag(extracted.get('goal'))}

## Who is this for?

{extracted.get('audience', '[needs_clarification]')} {tag(extracted.get('audience'))}

## What problem does it solve?

{extracted.get('problem', '[needs_clarification]')} {tag(extracted.get('problem'))}

## Key Features

{features_text}
## Technical Preferences (optional)

- Language: {tech_lang or '[no preference stated]'}
- Framework: {tech_fw or '[no preference stated]'}
- Database: {tech_db or '[no preference stated]'}
- Other:

## Priority

{extracted.get('priority', '[needs_clarification]')} {tag(extracted.get('priority'))}

## Deadline or Time Constraints (optional)

{extracted.get('deadline', '[not specified]')}
"""
    return output


def generate_clarification(gaps):
    """Generate CLARIFICATION_QUESTIONS.md if there are gaps."""
    if not gaps:
        return None

    questions = '# Clarification Questions\n\n'
    questions += '> These questions were identified by the intake normalization tool.\n'
    questions += '> Please answer them to help the agent organization understand your project.\n\n'

    for i, gap in enumerate(gaps, 1):
        questions += f'### Q{i}: {gap}\n\n'
        questions += '**Answer:** \n\n'

    return questions


def normalize(raw_text):
    """Main normalization pipeline."""
    extracted = {
        'name': extract_project_name(raw_text),
        'goal': extract_goal(raw_text),
        'audience': extract_audience(raw_text),
        'problem': extract_field(raw_text, [r'(?:problem|issue|pain|challenge|solve)'], 3),
        'features': extract_features(raw_text),
        'technical': extract_technical(raw_text),
        'priority': extract_field(raw_text, [r'(?:priority|important|critical|first|mvp)'], 2),
        'deadline': extract_field(raw_text, [r'(?:deadline|by|before|due|timeline|week|month)'], 2),
    }

    # If nothing could be extracted, fallback
    any_extracted = any(v for v in extracted.values() if v)
    if not any_extracted:
        # Fallback: put everything as goal, mark all fields as needs_clarification
        extracted['goal'] = raw_text.strip()[:1000]

    gaps = assess_clarity(extracted)
    project_request = generate_project_request(extracted)
    clarification = generate_clarification(gaps) if gaps else None

    return project_request, clarification, extracted, gaps


def main():
    parser = argparse.ArgumentParser(description='Normalize free-text project input')
    parser.add_argument('--input', '-i', help='Path to raw input file')
    parser.add_argument('--output', '-o', help='Path to output PROJECT_REQUEST.md')
    parser.add_argument('--json', action='store_true', help='Output extraction results as JSON')
    args = parser.parse_args()

    root = find_project_root()
    input_path = Path(args.input) if args.input else root / 'project_input' / 'RAW_INPUT.txt'
    output_path = Path(args.output) if args.output else root / 'project_input' / 'PROJECT_REQUEST.md'

    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}", file=sys.stderr)
        print(f"Create {input_path} with your project description in free text.", file=sys.stderr)
        sys.exit(1)

    raw_text = input_path.read_text(encoding='utf-8')
    if not raw_text.strip():
        print(f"Error: Input file is empty: {input_path}", file=sys.stderr)
        sys.exit(1)

    project_request, clarification, extracted, gaps = normalize(raw_text)

    if args.json:
        import json
        result = {
            'extracted': {k: v if not isinstance(v, list) else v for k, v in extracted.items()},
            'gaps': gaps,
            'has_clarification_questions': bool(gaps),
        }
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return

    # Write PROJECT_REQUEST.md
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(project_request, encoding='utf-8')
    print(f"✓ Generated: {output_path}")

    # Write CLARIFICATION_QUESTIONS.md if needed
    if clarification:
        clarify_path = output_path.parent / 'CLARIFICATION_QUESTIONS.md'
        clarify_path.write_text(clarification, encoding='utf-8')
        print(f"⚠ Gaps found — generated: {clarify_path}")
        print(f"  Missing: {', '.join(gaps)}")
    else:
        print("✓ All fields extracted successfully — no clarification needed")


if __name__ == '__main__':
    main()
