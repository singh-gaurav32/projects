from pyparsing import Word, alphas, nums, oneOf, Literal, Suppress, Group, ZeroOrMore, Forward, Combine, Optional, alphanums
from pyparsing import Literal

class RegexParser():
  def __init__(self,pattern):
    self.pattern = pattern
  
  def parsed_regex(self):
    print(self.pattern)
    space = Literal(" ")
    literal = Word(alphanums + " ").setParseAction(lambda t: list(t[0]))

    character_class = Combine(Literal("\\") + oneOf("d w D W ."))

    char_group = Group(Suppress("[") + Word(alphas + nums + "-") + Suppress("]")).setParseAction(lambda t: ("positive", list(t[0])))
    neg_char_group = Group(Suppress("[^") + Word(alphas + nums + "-") + Suppress("]")).setParseAction(lambda t: ("negative", list(t[0])))

    regex_expr = ZeroOrMore(character_class | literal | char_group | neg_char_group | space)
    # sample_regex = "\dabc\d[def][^defg]"

    result = regex_expr.parse_string(self.pattern)
    print(result)
    return result