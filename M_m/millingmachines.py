def findRemaining(lin, cut, wh):
	width = len(lin)
	height = int(wh[2])
	final = ""
	for elem in range(width):
		if(lin[elem] == " " or cut[elem] == " "): final += " "
		else: 
			ans = min(height - int(cut[elem]), int(lin[elem]))
			final += str(ans)
	return final

sdi = raw_input().split("\n")
cut = sdi[-1].strip()
wh = sdi[1].strip()
sdi = sdi[2:len(sdi)-2]
for lin in sdi:
	lin = lin.strip()
	print(findRemaining(lin, cut, wh))



