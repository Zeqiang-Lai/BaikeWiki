import requests


class HtmlDownloader(object):
	def download(self, url):
		try:
			r = requests.get(url, timeout=30)
			r.raise_for_status()
			r.encoding = 'utf-8'
			return r.text
		except:
			print('fail to get Html')
