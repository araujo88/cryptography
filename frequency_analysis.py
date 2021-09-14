# Computes letter frequency shart of sample text
# Computes probability of text being of certain language - suggestion

import numpy as np
import matplotlib.pyplot as plt

alphabet = list('abcdefghijklmnopqrstuvwxyz')

text='''
Cryptography, or cryptology (from Ancient Greek: κρυπτός, romanized: kryptós "hidden, secret"; and γράφειν graphein, "to write", or -λογία -logia, "study", respectively[1]), is the practice and study of techniques for secure communication in the presence of adversarial behavior.[2] More generally, cryptography is about constructing and analyzing protocols that prevent third parties or the public from reading private messages;[3] various aspects in information security such as data confidentiality, data integrity, authentication, and non-repudiation[4] are central to modern cryptography. Modern cryptography exists at the intersection of the disciplines of mathematics, computer science, electrical engineering, communication science, and physics. Applications of cryptography include electronic commerce, chip-based payment cards, digital currencies, computer passwords, and military communications.'''

count=np.zeros(26)

for i in range(len(text)):
	for j in range(len(alphabet)):
		if (text[i] == alphabet[j]):
			count[j]=count[j]+1
 

count=100*count/sum(count)

# Y scale in percentage
from matplotlib.ticker import FuncFormatter
formatter = FuncFormatter(lambda y, pos: "%d%%" % (y))
ax = plt.gca()
ax.yaxis.set_major_formatter(formatter)

# Dataset:
height = count
bars = alphabet
y_pos = np.arange(len(bars))
 
# Create bars
plt.bar(y_pos, height)
 
# Create names on the x-axis
plt.xticks(y_pos, bars, rotation=30)

plt.title("Letter frequency analysis of text") 
 
# Show graphic
plt.show()

