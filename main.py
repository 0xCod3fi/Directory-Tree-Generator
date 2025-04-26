#!/usr/bin/env python3

import argparse
import os
import sys

def get_size_str(size):
    """Convert file size to human-readable format"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} PB"

def generate_tree(directory, prefix="", show_files=True, show_hidden=False, 
                 max_depth=None, depth=0, show_size=False, patterns=None):
    """Generate a directory tree structure"""
    if max_depth is not None and depth > max_depth:
        return
    
    # Get directory contents
    try:
        entries = sorted(os.listdir(directory))
    except PermissionError:
        print(f"{prefix}└── [Permission denied]")
        return
    except Exception as e:
        print(f"{prefix}└── [Error: {e}]")
        return
    
    # Filter entries
    if not show_hidden:
        entries = [entry for entry in entries if not entry.startswith('.')]
    
    if patterns:
        import fnmatch
        filtered_entries = []
        for entry in entries:
            if any(fnmatch.fnmatch(entry, pattern) for pattern in patterns):
                filtered_entries.append(entry)
        entries = filtered_entries
    
    # Process directories first, then files
    dirs = []
    files = []
    for entry in entries:
        path = os.path.join(directory, entry)
        if os.path.isdir(path):
            dirs.append(entry)
        elif show_files:
            files.append(entry)
    
    # Process entries
    count = len(dirs) + (len(files) if show_files else 0)
    entry_index = 0
    
    # Process directories
    for entry in dirs:
        entry_index += 1
        path = os.path.join(directory, entry)
        
        # Determine connector type
        if entry_index == count:
            connector = "└── "
            next_prefix = prefix + "    "
        else:
            connector = "├── "
            next_prefix = prefix + "│   "
        
        # Print directory name
        print(f"{prefix}{connector}{entry}/")
        
        # Recursively process subdirectory
        generate_tree(path, next_prefix, show_files, show_hidden, 
                      max_depth, depth + 1, show_size, patterns)
    
    # Process files
    if show_files:
        for entry in files:
            entry_index += 1
            path = os.path.join(directory, entry)
            
            # Determine connector type
            if entry_index == count:
                connector = "└── "
            else:
                connector = "├── "
            
            # Get file size if requested
            size_info = ""
            if show_size:
                try:
                    size = os.path.getsize(path)
                    size_info = f" ({get_size_str(size)})"
                except:
                    size_info = " (unknown size)"
            
            # Print file name
            print(f"{prefix}{connector}{entry}{size_info}")

def main():
    parser = argparse.ArgumentParser(description="Generate a directory tree")
    parser.add_argument("directory", nargs="?", default=".", help="Directory to process (default: current directory)")
    parser.add_argument("-a", "--all", action="store_true", help="Show hidden files and directories")
    parser.add_argument("-d", "--max-depth", type=int, help="Maximum depth of directories to display")
    parser.add_argument("-f", "--files-only", action="store_true", help="Show only files, not directories")
    parser.add_argument("-D", "--dirs-only", action="store_true", help="Show only directories, not files")
    parser.add_argument("-s", "--size", action="store_true", help="Show file sizes")
    parser.add_argument("-p", "--pattern", action="append", help="Include only entries that match the pattern (can specify multiple patterns)")
    
    args = parser.parse_args()
    
    # Validate directory
    if not os.path.exists(args.directory):
        print(f"Error: Directory '{args.directory}' does not exist")
        sys.exit(1)
    
    if not os.path.isdir(args.directory):
        print(f"Error: '{args.directory}' is not a directory")
        sys.exit(1)
    
    # Print initial directory
    print(f"{os.path.basename(os.path.abspath(args.directory))}/")
    
    # Generate tree
    generate_tree(
        args.directory,
        show_files=not args.dirs_only,
        show_hidden=args.all,
        max_depth=args.max_depth,
        show_size=args.size,
        patterns=args.pattern
    )

if __name__ == "__main__":
    main()
