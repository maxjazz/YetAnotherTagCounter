import yaml
import logging
import time
from bs4 import BeautifulSoup as BS
from tabulate import tabulate as tb
import requests
from store import Store


class TC:

	def get_alias(self, alias):
		with open("config.yml", 'r') as stream:
			data_loaded = yaml.load(stream)
			if alias in data_loaded:
				return data_loaded[alias]
			else:
				return None

	def table(self, items):
		sort = sorted(items, key = lambda x: (x[1],x[0]))
		return tb (sort, headers = ['Tags', 'Numbers'], tablefmt='psql')

	def counter(self, html):
		tags = []
		res = {}
		soup = BS(html, 'html.parser')
		for tag in soup.findAll():
			tags.append(tag.name)
		uniq = list(set(tags))
		for tag in uniq:
			res[tag] = tags.count(tag)
		return res

	def http_get(self, url: str):
		logging.info('HTTP: GET ' + url)
		response = requests.get(url)
		if response.status_code is not 200:
			raise RuntimeError('HTTP Error. Response status code is: ' + response.status_code)
		return response.content


	def run(self, action):
		db = Store('store.db')
		if action.view:
			data = db.load_data(action.view)
			print (self.table(data.items()))
		if action.get:
			if self.get_alias(action.get) is not None:
				alias = action.get
				url = self.get_alias(action.get)
			else:
				url = action.get
				alias = action.get
			res = self.counter(self.http_get(url))
			print (self.table(res.items()))
			db.save_data(alias,url,time.time(),res)

