import urllib, urllib2, cookielib
from BeautifulSoup import BeautifulSoup
from PIL import Image

#im = Image.open(image)
#im.show()

def getImgCodes(url):
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

	html_dump = opener.open(url)

	imgCodes = []
	tree = BeautifulSoup(html_dump.read())
	for link in tree.findAll('a'):
		view = str(link.get('href'))
		if 'Packages' in view and not 'GroupImage=True' in view:
			imgCodes.append(view[14:39])

	return imgCodes

def cropImg(url):
	return

if __name__ == '__main__':
	print imgCodes