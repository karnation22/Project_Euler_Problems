def encode(code_table, msg):
	codeStr = ""
	for letter in msg: #terates through all of the letters in string
		if letter not in code_table: return None
		else: codeStr += code_table[letter]
	return codeStr

print encode({'a': '0', 'b':'10','c':'1110', 'd':'111'}, 'dadabbac')
