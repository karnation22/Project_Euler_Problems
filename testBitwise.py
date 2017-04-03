def makePixel(a, r, g, b): #returns int type
	p = 0
	p += a << 24
	p += r << 16
	p += g << 8
	p += b
	return p
def getAlpha(pixel):
	pixel = pixel >> 24
	return pixel
def getRed(pixel):
	pixel = pixel >> 16 #xxAR(GB gone)
	pixel = pixel & 255
	return pixel
def getGreen(pixel): #takes int input, returns green value
	pixel = pixel >>8 #xARG (B gone)
	pixel = pixel & 255
	return pixel
def getBlue(pixel):
	pixel = pixel & 255
	return pixel

def getBadRed(pixel):
	pixel = pixel >> 16
	return pixel

def getBadGreen(pixel):
	pixel = pixel >> 8
	return pixel



print(1<<1)




	


