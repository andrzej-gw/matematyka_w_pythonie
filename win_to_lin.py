while True:
	s=input()
	while len(s)>=4 and ord(s[0])==32 and ord(s[1])==32 and ord(s[2])==32 and ord(s[3])==32:
		print("    ",end="")
		s=s[4:]
	print(s)
