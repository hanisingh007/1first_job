import sys

def count_words_in_log(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            words = content.split()
            print(f"Log file: {file_path}")
            print(f"Total words: {len(words)}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_logs.py <log_file>")
    else:
        count_words_in_log(sys.argv[1])
