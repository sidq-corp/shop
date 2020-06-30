from flask import Flask, url_for

import json


app = Flask(__name__)

@app.route('/')
def main():
	return url_for('get_main_api', page = 1) + ' ' + url_for('add_pr', json_data = 'ss')

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

	return json.dumps(data[page - 1 if page <= len(data) else len(data) - 1])

if __name__ == '__main__':
	app.run(debug=True)
"""
А главноей странице
	Цена
	Название
	Краткое описание
	Картинка
	Оценка
"""