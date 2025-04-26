# 🌲 Directory Tree Generator

A simple command-line tool that generates a visual representation of directory structures.

## ✨ Features

- 📂 Visualize directory structures in a tree format
- 🔍 Control visualization depth for nested directories
- 🔄 Filter files and directories with patterns
- 📊 Display file sizes in human-readable format
- 🙈 Option to hide or show hidden files
- 🗃️ Show only files or only directories

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/0xCod3fi/directory-tree.git
cd directory-tree
```

2. Make the script executable (Unix/Linux/macOS):
```bash
chmod +x main.py
```

## 🔍 Usage

```bash
python main.py [directory] [options]
```

## ⚙️ Options

- `directory`: Directory to process (default: current directory)
- `-a, --all`: Show hidden files and directories
- `-d, --max-depth`: Maximum depth of directories to display
- `-f, --files-only`: Show only files, not directories
- `-D, --dirs-only`: Show only directories, not files
- `-s, --size`: Show file sizes
- `-p, --pattern`: Include only entries that match the pattern (can specify multiple patterns)

## 📝 Examples

### Display the tree of the current directory:
```bash
python main.py
```

### Display a specific directory:
```bash
python main.py /path/to/directory
```

### Show hidden files and directories:
```bash
python main.py -a
```

### Limit the depth of directories:
```bash
python main.py -d 2
```

### Show only directories:
```bash
python main.py -D
```

### Show file sizes:
```bash
python main.py -s
```

### Filter entries by pattern:
```bash
python main.py -p "*.py" -p "*.txt"
```

### Combine multiple options:
```bash
python main.py ~/projects -a -d 3 -s -p "*.py"
```


