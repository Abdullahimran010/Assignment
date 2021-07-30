import math

def manhattan_distance(x1,x2,y1,y2):
	print((x1-x2)+(y1-y2))

def eculidian_distance(x1,x2,y1,y2):
	print(math.sqrt(((x2-x1)**2)+(y2-y1)**2))

def is_pangram(string):

	if 'a' in string and 'b' in string and 'c' in string and 'd' in string and 'e' in string and 'f' in string and 'g' in string and 'h' in string and 'i' in string and 'j' in string and 'k' in string and 'l' in string and 'm' in string and 'n' in string and 'o' in string and 'p' in string and 'q' in string and 'r' in string and 's' in string and 't' in string and 'u' in string and 'v' in string and 'w' in string and 'x' in string and 'y' in string and 'z':
		print("Pangram Sentence Found")

	else:
		print("Pangram Not Found")	

manhattan_distance(1,2,3,4)	
eculidian_distance(1,2,3,4)	
is_pangram("the quick brown fox jumps over the lazy dog")