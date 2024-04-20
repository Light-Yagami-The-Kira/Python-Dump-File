#  FIND THE WORD FOX
import re
pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print(f"Found '{pattern}' in '{text}' from {s} to {e}")
	