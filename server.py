from flask import Flask, request
from request_helper import RequestHelper
from definitions import SAMPLES_DIR
import os


app = Flask(__name__)
rh = RequestHelper(app)


def handle_file(action):
	data = dict(request.args.items())
	file_path = data.get('filePath')
	
	if not file_path or not os.path.exists(file_path):
		raise BaseException('File doesn\'t exist at path: {}'.format(file_path))
	
	if not file_path.startswith(SAMPLES_DIR):
		raise BaseException('File not in samples dir')
	
	if '/pending/' not in file_path:
		raise BaseException('HTML file being evaluated isn\'t a pending file.')
	
	if action == 'keep' or action == 'discard':
		new_file_path = file_path.replace('/pending/', '/{}/'.format(action))
		os.system('mv {} {}'.format(file_path, new_file_path))


@app.route('/discard_file', methods=['GET'])
def discard_file():
	handle_file('keep')
	return rh.json_response()


@app.route('/keep_file', methods=['GET'])
def keep_file():
	handle_file('keep')
	return rh.json_response()


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000, debug=True, use_reloader=True)