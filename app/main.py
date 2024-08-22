import sys

def matcher(input_line, pattern):
    if not pattern:
        return True
    if not input_line and pattern:
        return False

    if pattern.startswith("\\d"):
        if input_line[0].isdigit():
            return matcher(input_line[1:], pattern[2:])
        else:
            return matcher(input_line[1:], pattern)
    
    elif pattern.startswith("\\w"):
        if input_line[0].isalnum():
            return matcher(input_line[1:], pattern[2:])
        else:
            return matcher(input_line[1:], pattern)
    
    else:
        if input_line[0] == pattern[0]:
            return matcher(input_line[1:], pattern[1:])
        else:
            return matcher(input_line[1:], pattern)

def match_pattern(input_line, pattern):
    if pattern.startswith("\\d"):
        if input_line and input_line[0].isdigit():
            # Continue matching after the digit
            return match_pattern(input_line[1:], pattern[2:])
    elif pattern.startswith("\\w"):
        if input_line and input_line[0].isalnum():
            # Continue matching after the alphanumeric character
            return match_pattern(input_line[1:], pattern[2:])
    elif pattern.startswith("[^") and "]" in pattern:
        excluded_chars = pattern[2:pattern.index("]")]
        if input_line and input_line[0] not in excluded_chars:
            return match_pattern(input_line[1:], pattern[pattern.index("]")+1:])
    elif pattern.startswith("[") and "]" in pattern:
        allowed_chars = pattern[1:pattern.index("]")]
        if input_line and input_line[0] in allowed_chars:
            return match_pattern(input_line[1:], pattern[pattern.index("]")+1:])
    elif input_line.startswith(pattern):
        return True
    elif len(input_line) > 1:
        return match_pattern(input_line[1:], pattern)
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")

    return False



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
