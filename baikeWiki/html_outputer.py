class HtmlOutputer(object):
	def print(self, chData, enData):
		try:
			print('')
			print('======================')
			print('百度百科：')
			print(chData['title'])
			print(chData['summary'])
			print('----------------------')
			print('wikipedia')
			print(enData['title'])
			print(enData['summary'])
			print('======================')
		except:
			print('print error')