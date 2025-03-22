#!/usr/bin/env python3
"""
Script to organize OpenWebUI API schema exports by file type.

This script organizes JSON and Markdown files into separate subdirectories
within each API endpoint category directory.
"""

import os
import shutil
import glob
from pathlib import Path

def organize_files(base_dir):
    """
    Organize files by creating 'json' and 'markdown' subdirectories in each API endpoint directory
    and moving the respective files into them.
    
    Args:
        base_dir (str): The base directory containing the API endpoint directories
    """
    # Get all API endpoint directories
    endpoint_dirs = [d for d in glob.glob(os.path.join(base_dir, '*')) if os.path.isdir(d)]
    
    for endpoint_dir in endpoint_dirs:
        print(f"Processing directory: {endpoint_dir}")
        
        # Create json and markdown subdirectories if they don't exist
        json_dir = os.path.join(endpoint_dir, 'json')
        markdown_dir = os.path.join(endpoint_dir, 'markdown')
        
        os.makedirs(json_dir, exist_ok=True)
        os.makedirs(markdown_dir, exist_ok=True)
        
        # Move JSON files to json directory
        json_files = glob.glob(os.path.join(endpoint_dir, '*.json'))
        for json_file in json_files:
            filename = os.path.basename(json_file)
            destination = os.path.join(json_dir, filename)
            print(f"  Moving {filename} to json directory")
            shutil.move(json_file, destination)
        
        # Move Markdown files to markdown directory
        md_files = glob.glob(os.path.join(endpoint_dir, '*.md'))
        for md_file in md_files:
            filename = os.path.basename(md_file)
            destination = os.path.join(markdown_dir, filename)
            print(f"  Moving {filename} to markdown directory")
            shutil.move(md_file, destination)

def main():
    # Base directory containing all the API endpoint directories
    base_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "220325", "full-definition", "by-api-endpoint"
    )
    
    if not os.path.exists(base_dir):
        print(f"Error: Directory not found: {base_dir}")
        return
    
    print(f"Starting organization of files in: {base_dir}")
    organize_files(base_dir)
    print("File organization complete!")

if __name__ == "__main__":
    main()
