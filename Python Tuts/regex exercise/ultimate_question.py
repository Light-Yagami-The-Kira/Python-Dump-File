import re
def test(text):
	# pattern = r'^[AEIOUaeiou].*[AEIOUaeiou]$'
	pattern = r'^[AEIOUaeiou][A-Za-z ]*[AEIOUaeiou]$'
	return bool(re.findall(pattern, text))

text ="Red Orange White"
print("Original string:", text)
print("Check beginning and end of a word in the said string with a vowel:")
print(test(text))
text ="Red White Black"
print("\nOriginal string:", text)
print("Check beginning and end of a word in the said string with a vowel:")
print(test(text))
text ="ibcd dkise eosksa"
print("\nOriginal string:", text)
print("Check beginning and end of a word in the said string with a vowel:")
print(test(text))
