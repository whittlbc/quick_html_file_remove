import json


class RequestHelper(object):
	
	def __init__(self, app):
		self.app = app
	
	def json_response(self, data=None, status=200):
		resp_data = json.dumps(data or {})
		response = self.app.make_response(resp_data)
		return response, status
	
	def error(self, message='', status=500):
		return self.json_response({'error': message}, status=status)
