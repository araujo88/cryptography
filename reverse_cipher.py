def encrypt (string1):
	string2=""
	for i in range(len(string1)):
		string2+=string1[len(string1)-i-1]
	return string2

text="Hello world"
print("Input string: " + text)
print("Encrypted string: " + encrypt(text))


