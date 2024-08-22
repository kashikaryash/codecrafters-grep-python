import sys
import re

def match_pattern(input_line, pattern):
    # Use regex to handle the \d pattern
    if pattern == r'\d':
        return bool(re.search(r'\d', input_line))
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")

def main():
    if len(sys.argv) != 3 or sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    print("Logs from your program will appear here!")

    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)

if __name__ == "__main__":
    main()
