from bs4 import BeautifulSoup


class HtmlParser(object):
	def baiduparse(self, chCont):
		try:
			data = {}
			isNone = 0
			soup = BeautifulSoup(chCont, 'html.parser')

			# 获取标题
			title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
			if title_node is not None:
				data['title'] = title_node.get_text()
			else:
				isNone = 1

			# 获取概要
			summary_node = soup.find('div', class_='lemma-summary')
			if summary_node is not None:
				data['summary'] = summary_node.get_text()
			else:
				isNone = 1

			# 如未获取到内容，输出提示
			if isNone == 1:
				data['title'] = 'error'
				data['summary'] = '中文存在同义词，无法获取，请自行获取'
		except:
			data['title'] = 'error'
			data['summary'] = '无法获取词条'

		return data

	def wikiparse(self, enCont):
		try:
			data = {}
			isNone = 0
			soup = BeautifulSoup(enCont, 'html.parser')

			# 获取标题
			title_node = soup.find(id='firstHeading')
			if title_node is not None:
				data['title'] = title_node.get_text()
			else:
				isNone = 1

			# 获取概要
			summary_node = soup.find('div', id='mw-content-text').find('p')
			if summary_node is not None:
				data['summary'] = summary_node.get_text()
			else:
				isNone = 1

			# 如果未获取到内容则输出提示
			if isNone == 1:
				data['title'] = 'error'
				data['summary'] = '英文存在同义词，无法获取，请自行获取'
		except:
			data['title'] = 'error'
			data['summary'] = '无法获取词条'

		return data
