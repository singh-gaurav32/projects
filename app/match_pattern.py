



class MatchPattern():

  def is_line_match(self,input_line,parsed_regex):
    is_matched = False
    parser_length = len(parsed_regex)
    for i in range(len(input_line) - parser_length):
      window = input_line[i:i+parser_length+1]
      is_matched |= self.is_window_match(window,parsed_regex)
    return is_matched

  def is_window_match(self,input_line,parsed_regex):
    print(input_line,parsed_regex)
    if len(input_line) != len(parsed_regex):
      return False
    is_matched = True 
    for char,pattern in zip(input_line,parsed_regex):
      if isinstance(pattern,tuple) and len(pattern) == 2:
        if pattern[0] == "positive":
          is_matched &= self.match_pattern(char,pattern[1])
        else:
          is_matched &= self.match_pattern(char,f"^{pattern[1]}")
      else:
        is_matched &= self.match_pattern(char,pattern)
    return is_matched
  

  def match_pattern(self,input_line, pattern):
    if len(pattern) == 1:
        return pattern in input_line
    if pattern == "\\d":
        return input_line.isdigit()
    if pattern == "\\w":
        return input_line.isalnum()
    if pattern[0] == "[" and pattern[-1] == "]":
        chars = pattern[1:-1]
        if chars[0] == "^":
            neg_chars = chars[1:]
            return not any(char in input_line for char in chars)
        return any(char in input_line for char in chars)
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")