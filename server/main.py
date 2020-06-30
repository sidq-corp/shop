from flask import Flask, url_for
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
	return url_for('get_main_api', page = 1) + ' ' + url_for('add_pr', json_data = '[1,1,1]')

@app.route('/add_pr/<json_data>')
def add_pr(json_data):
	data = json.loads(json_data)
	print(data)
	with open('full.json', 'r') as full:
		data = [data]
		data.extend(json.load(full))
	print(data)
	with open('full.json', 'w') as file:
		json.dump(data, file)
	return 'a'

@app.route('/get_main_api/<int:page>')
def get_main_api(page = 1):
	with open('full.json', 'r') as full:
		data = json.load(full)

	data = [data[i:i+10] for i in range(0, len(data), 10)]
	try:
		return json.dumps(data[page - 1])
	except:
		return 'IndexError'
if __name__ == '__main__':
	app.run(debug=True)
"""
А главноей странице
	"Цена", "Название", "Описание", "Рейтинг товара", ["Комментарии"], "Превью", ["Массив картинок"]
"""