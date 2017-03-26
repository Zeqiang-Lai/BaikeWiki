from baikeWiki import html_downloader
from baikeWiki import html_outputer
from baikeWiki import html_parser
from baikeWiki.translator import Youdao


class spiderMain(object):
	def __init__(self):
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()
		self.downloader = html_downloader.HtmlDownloader()

	def getUrl(self, lan, word):
		if lan == 'ch':
			rootUrl = 'http://baike.baidu.com/item/'
			return rootUrl + word
		elif lan == 'en':
			rootUrl = 'https://en.wikipedia.org/wiki/'
			return rootUrl + word

	def craw(self, ch, en):
		chUrl = self.getUrl('ch', ch)
		print(chUrl)
		chCont = self.downloader.download(chUrl)
		chData = self.parser.baiduparse(chCont)

		enUrl = self.getUrl('en', en)
		print(enUrl)
		enCont = self.downloader.download(enUrl)
		enData = self.parser.wikiparse(enCont)

		self.outputer.print(chData, enData)


def main():
	while True:
		spider = spiderMain()
		youdao = Youdao()
		ch = input()
		try:
			en, isCh = youdao.get_translation(ch)
		except:
			print('please check the internet')
		print(en)
		if isCh == True:
			en, ch = ch, en
		spider.craw(ch, en)


if __name__ == '__main__':
	main()

# class en,msg is str
