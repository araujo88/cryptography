def encrypt (string1,s):
	result=""
	for i in range(len(string1)):
		char=string1[i]	
		if (char==" ")or(char==".")or(char==",")or(char==":")or(char=="(")or(char==")"):
			result+=char
		else:
			if (char.isupper()):
				result+=chr((ord(char)+s-ord("A"))%26+ord("A"))
			else:
				result+=chr((ord(char)+s-ord("a"))%26+ord("a"))
	return result

text="Hello World"
shift=4
print("Input string: " + text)
print("Shift: " + str(shift))
print("Encrypted string: " + encrypt(text,shift))


