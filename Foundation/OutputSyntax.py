# Concept: Console output, escaping characters, formatting basic multiline output.
# Challenge: Write a single print() statement that outputs a dynamic ASCII art box containing two lines of text. You cannot use multiple print() calls, multiline string literals ("""), or external modules.
# Expected Output:
# +------------------+
# |  Hello, Python!  |
# |  Line 2 Here!    |
# +------------------+


line1, line2 = "Hello, World!", "Python Rocks!"
w = max(len(line1), len(line2)) + 4
print("+" + "-"*w + "+"  + "\n" + "|" +  line1.ljust(w-4)  + "|"+ "\n" + "|" + line2.ljust(w-4) + "|" + "\n" + "+" + "-"*w + "+")

