# import sys

# def count_words_in_log(file_path):
#     try:
#         with open(file_path, 'r') as f:
#             content = f.read()
#             words = content.split()
#             print(f"Log file: {file_path}")
#             print(f"Total words: {len(words)}")
#     except FileNotFoundError:
#         print(f"File not found: {file_path}")

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: python analyze_logs.py <log_file>")
#     else:
#         count_words_in_log(sys.argv[1])

import sys

def count_words_in_log(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            words = content.split()
            total = len(words)
            return total
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_logs.py <log_file>")
        sys.exit(1)

    logfile = sys.argv[1]
    total = count_words_in_log(logfile)
    if total is None:
        text = f"File not found: {logfile}\n"
    else:
        text = f"Log file: {logfile}\nTotal words: {total}\n"

    # write output to analysis_output.txt
    with open('analysis_output.txt', 'w') as out:
        out.write(text)

    # also print to console (optional)
    print(text)

