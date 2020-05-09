from numpy import reshape

def encrypt (string1,row):
	# Initialize encrypted text	
	string3=""

	# Append plain text in case it does not contain even length
	while len(string1)%row!=0: 
		string1+=" "

	col=round(len(string1)/row)
	
	# Reshape plain text to matrix
	string2=reshape(list(string1),(row,col))

	# Convert matrix to vector
	for j in range(col):	
		for i in range(row):
			string3+=((string2[i,j]))
	return string3

rows=3
text="Hello world"
encrypted_text="Hore llwdlo"
print("Input string: " + text)
print("Encrypted string: " + encrypt(text,rows))

for k in range(len(text)):
	print("Decrypted string: (" + str(k+1) + " rows) " + encrypt(encrypted_text,k+1))











