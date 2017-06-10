from flask import Flask, request
from request_helper import RequestHelper
import os


app = Flask(__name__)
rh = RequestHelper(app)


@app.route('/remove_file', methods=['GET'])
def remove_file():
	data = dict(request.args.items())
	file_path = data.get('filePath')
	
	if not file_path:
		return rh.error('No filePath param provided in request')
		
	if not os.path.exists(file_path):
		return rh.error('File does not exist')
	
	try:
		os.remove(file_path)
	except:
		print 'Error removing file at {}'.format(file_path)
		return rh.error(message='Error removing file')
	
	return rh.json_response({'message': 'Successfully removed file'})


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000, debug=True, use_reloader=True)