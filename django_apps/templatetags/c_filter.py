from django import template
import re

register = template.Library()

match_pointer_to_char = re.compile("const char\s*\*$")
match_pointer_to_type = re.compile("const [A-Za-z0-9]+\s*\*$")

@register.filter
def to_c(s):
  if s=='void' or s=='int' or s=='bool' or s=='double':
    return s
  if re.match(match_pointer_to_char,s):
    return 'const char*'
  if re.match(match_pointer_to_type,s):
    return 'const void *'
  else:
    error = 'Type {} has no known c equivalent'.format(s)
    raise Exception(error)

