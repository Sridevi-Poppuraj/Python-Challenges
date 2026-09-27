# Concept: int, float, str, bool, implicit vs. explicit casting, lossless conversion.
# Challenge: Write a function parse_mixed_input(val) that accepts a string representation of a value (e.g., "42", "3.14", "True", "Hello"). Automatically convert and return it in its narrowest non-lossy primitive type (bool > int > float > str). Note that string "False" must evaluate to bool False, not boolean True.

val = "3.14"

def parse_mixed_input(val):
 if(val == "False"):
   return False
 if (val == "True"):
   return True

 try:
   return int(val)
 except:
   pass

 try:
   return float(val)
 except:
   pass

value = parse_mixed_input(val)
print(value, type(value))
