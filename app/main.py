import sys

def matcher(input_line, pattern):
    if not pattern:
        return True
    if not input_line and pattern:
        return False

    if pattern.startswith("\\d"):
        if input_line and input_line[0].isdigit():
            return matcher(input_line[1:], pattern[2:])
        else:
            return False
    
    elif pattern.startswith("\\w"):
        if input_line and input_line[0].isalnum():
            return matcher(input_line[1:], pattern[2:])
        else:
            return False
    
    else:
        if input_line and input_line[0] == pattern[0]:
            return matcher(input_line[1:], pattern[1:])
        else:
            return False

def match_pattern(input_line, pattern):
    for i in range(len(input_line)):
        if matcher(input_line[i:], pattern):
            return True
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
