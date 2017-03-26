# coding:UTF-8
import json
import urllib.request
from urllib.parse import quote


class Youdao:
	def __init__(self):
		self.url = 'http://fanyi.youdao.com/openapi.do'
		self.key = '413978873'  # 有道API key
		self.keyfrom = 'baike-wiki'  # 有道keyfrom

	def get_translation(self, words):
		words = quote(words.encode('utf-8'))
		url = self.url + '?keyfrom=' + self.keyfrom + '&key=' + self.key + '&type=data&doctype=json&version=1.1&q=' + words
		result = urllib.request.urlopen(url).read()
		result = str(result, encoding='utf-8')
		json_result = json.loads(result)
		json_result = json_result["translation"]
		for i in json_result:
			isch = self.checkChinese(i)
			return i,isch

	def checkChinese(self, i):
		for ch in i:
			if u'\u4e00' <= ch <= u'\u9fff':
				return True
		return False

