import sqlite3
import pickle
import logging

class Store:

	def __init__(self, dbfile):
		self.dbfile = dbfile
		self.conn = sqlite3.connect (dbfile)
		self.c = self.conn.cursor()
		self.c.execute('CREATE TABLE IF NOT EXISTS scan_results(alias TEXT, url TEXT, timestamp TEXT, tags BLOB )')
		self.conn.commit
    
	def destroy(self):
		self.c.close()
		self.conn.close()

	def save_data(self, alias, url, timestamp, tags ):
		logging.info('Saving results to DB for: ' + alias + ' - ' + url)
		serialized_tags_dict = pickle.dumps(tags)
		self.c.execute('INSERT INTO scan_results(alias, url, timestamp, tags) VALUES (?, ?, ?, ?)',
			(alias, url, timestamp, sqlite3.Binary(serialized_tags_dict)))
		self.conn.commit()

	def load_data (self, url):
		logging.info('Fetching results from DB by: ' + url)
		self.c.execute('SELECT alias, tags FROM scan_results WHERE url="' + url + '"')
		data = self.c.fetchall()
		self.conn.commit()
		logging.debug('DB fetched' + str(data))
		site_name = data[len(data)-1][0]
		tags_pickled = data[len(data)-1][1]
		tags_unpickled = pickle.loads(tags_pickled)
		return tags_unpickled

