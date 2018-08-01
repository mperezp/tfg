import requests
import hashlib
from models import SGV

class Api(object):

	def __init__(self, site_url):
		self.site_url = site_url

	def getCurrentSgv(self):
		r = requests.get(self.site_url + 'api/v1/entries/current.json')