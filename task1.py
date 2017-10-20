import string
import csv
with open('Book1.txt','r') as a, open('Book2.txt','r') as b, open('Book3.txt', 'r') as c :
	longest=0
	for line in a,b,c:
		print (line)
		for word in line:
			print (word)
			if len(word) > longest:
				longest=len(word)
				longest_word = word
				print (longest_word)

