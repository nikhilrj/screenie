import urllib, urllib2, cookielib
from BeautifulSoup import BeautifulSoup
from PIL import Image


def getImgCodes(url):
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

	html_dump = opener.open(url)

	imgCodes = []
	tree = BeautifulSoup(html_dump.read())
	for link in tree.findAll('a'):
		view = str(link.get('href'))
		if 'Packages' in view and not 'GroupImage=True' in view and view[14:39] not in imgCodes:
			imgCodes.append(view[14:39])

	return imgCodes

def cropImg(imgCode):
	canvas = Image.new('RGB', (481,628))
	for x in xrange(56, 550, 113):
		for y in xrange(56, 700, 113):
			target = 'http://images1.flashphotography.com/Magnifier/MagnifyRender.ashx?' + 'X=' + str(x) + '&Y=' + str(y) + '&' + imgCode + '&A=0'
			
			image = urllib.urlopen(target)
			im = Image.open(image)
			im = im.crop((37,37,152,152))
			
			canvas.paste(im, (x-56,y-56))

	canvas.save(str(imgCode) + '.jpg')

if __name__ == '__main__':
	userURL = raw_input('Please paste in your proof link from your e-mail\n Example: http://orders.flashphotography.com/Track/C.aspx?c=######&q=#######&n=######&l=*******&a=######&e=######&t=g\n\nInput > ')
	imgCodes = getImgCodes(userURL)

	for img in imgCodes:
		cropImg(img)
		print 'Finished Image ' + str(img)