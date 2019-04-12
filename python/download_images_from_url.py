import urllib.request

lines = open('urls.txt').readlines()

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.69 Safari/537.36"
urllib._urlopener = AppURLopener()

urllib._urlopener.retrieve("https://www.hypergridbusiness.com/wp-content/uploads/2015/10/Alian-Cardboard-147x150.jpg", "images/bar.jpg")

for line in lines:
	print("Downloading: images/{} {}".format(line.split('/')[-1].strip(), line))
	urllib._urlopener.retrieve(line, "images/{}".format(line.split('/')[-1].strip()))