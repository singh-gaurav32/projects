import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!
class Pattern:
    DIGIT = "\\d"
    ALNUM = "\\w"


def match_pattern(input_line, pattern):
    if not pattern:
        return True
    if not input_line:
        return False
    if pattern[0] == input_line[0]:
        return match_pattern(input_line[1:],pattern[1:])
    elif pattern[:2] == Pattern.DIGIT:
        if input_line[0].isdigit():
            return match_pattern(input_line[1:],pattern[2:])
    elif pattern[:2] == Pattern.ALNUM:
        if input_line[0].isalnum():
            return match_pattern(input_line[1:],pattern[2:])
    elif pattern[0] == "[" and pattern[-1] == "]":
        chars = pattern[1:-1]
        if chars[0] == "^":
            neg_chars = chars[1:]
            return not any(char in input_line for char in chars)
        return any(char in input_line for char in chars)
    return match_pattern(input_line[1:],pattern)



def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")
    # Uncomment this block to pass the first stage
    is_matched = match_pattern(input_line,pattern)
    print(f"is_matched: {is_matched}")
    if is_matched:
        exit(0)
    exit(1)

if __name__ == "__main__":
    main()
