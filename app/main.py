import sys

# Capture command-line arguments
args = sys.argv
pattern = args[3] if len(args) > 3 else ""

# Capture the input string
input_line = sys.stdin.read().strip()

# Function to check if a character is a digit
def is_digit(ascii_val):
    return 48 <= ascii_val <= 57

# Function to check if a character is a word character (alphanumeric or underscore)
def is_word_char(ascii_val):
    return (48 <= ascii_val <= 57) or (65 <= ascii_val <= 90) or (97 <= ascii_val <= 122) or ascii_val == 95

# Function to match the pattern against the input line
def match_pattern(input_line, pattern):
    # Match \d for digits
    if pattern == "\\d":
        return any(is_digit(ord(char)) for char in input_line)
    
    # Match \w for word characters
    elif pattern == "\\w":
        return any(is_word_char(ord(char)) for char in input_line)
    
    # Match [abc] or [^abc]
    elif pattern.startswith("[") and pattern.endswith("]"):
        negate = pattern[1] == "^"
        chars = pattern[2:-1] if negate else pattern[1:-1]
        char_set = set(chars)
        
        if negate:
            return any(char not in char_set for char in input_line)
        else:
            return any(char in char_set for char in input_line)
    
    # Match a simple literal pattern
    elif len(pattern) == 1:
        return pattern in input_line
    
    # Complex patterns (e.g., \d apple)
    else:
        compare = []
        i = 0
        
        while i < len(pattern):
            if pattern[i] == '\\':
                if i + 1 < len(pattern):
                    if pattern[i + 1] == 'd':
                        compare.append('\\d')
                    elif pattern[i + 1] == 'w':
                        compare.append('\\w')
                    i += 1
            else:
                compare.append(pattern[i])
            i += 1
        
        compare_index = 0
        for i in range(len(input_line)):
            if compare_index == len(compare):
                break
            
            current_char = input_line[i]
            current_pattern = compare[compare_index]
            
            if current_pattern == '\\w' and is_word_char(ord(current_char)):
                compare_index += 1
            elif current_pattern == '\\d' and is_digit(ord(current_char)):
                compare_index += 1
            elif current_pattern == current_char:
                compare_index += 1
            else:
                compare_index = 0
        
        return compare_index == len(compare)
    
    return False

# Ensure the first argument is "-E"
if args[2] != "-E":
    print("Expected first argument to be '-E'")
    sys.exit(1)

# Debugging output
print("Logs from your program will appear here!")

# Check if the input line matches the pattern
if match_pattern(input_line, pattern):
    sys.exit(0)  # Success, pattern matches
else:
    sys.exit(1)  # Failure, pattern does not match
