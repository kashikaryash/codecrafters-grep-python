import sys
import re

def match_pattern(input_line: str, pattern: str) -> bool:
    """
    Match the input line with the given pattern.
    This function assumes that the pattern is a valid regex pattern.
    """
    # Translate common regex patterns to Python's regex format
    translated_pattern = pattern
    translated_pattern = translated_pattern.replace(r"\d", r"\d")
    translated_pattern = translated_pattern.replace(r"\w", r"\w")
    
    # Compile regex pattern
    try:
        regex = re.compile(translated_pattern)
    except re.error as e:
        print(f"Regex compilation error: {e}")
        sys.exit(1)
    
    # Match the pattern against the input line
    return bool(regex.fullmatch(input_line))

def main():
    """Main."""
    if len(sys.argv) != 3 or sys.argv[1] != "-E":
        print("Usage: ./your_program.sh -E <pattern>")
        sys.exit(1)

    pattern = sys.argv[2]
    input_line = sys.stdin.read().strip()
    
    # Debugging output
    print(f"Pattern: {pattern}")
    print(f"Input line: {input_line}")
    
    # Check for matches
    result = match_pattern(input_line, pattern)
    
    # Print result and exit with status code
    if result:
        print("Match found")
        sys.exit(0)
    else:
        print("No match found")
        sys.exit(1)

if __name__ == "__main__":
    main()
