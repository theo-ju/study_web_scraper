from flask import Flask, render_template, request, redirect
from scrapper import run_scrapper

app = Flask('SuperScrapper')


# Decorator - 바로 아래의 있는 함수를 찾음.
@app.route('/')
def home():
	return 'Hello! welcome to my page'


# @app.route('/<username>')
# def userpage(username):
# 	return f'hello {username}, how are you!'


@app.route('/job_search')
def job_search():
	return render_template('job_search.html')


@app.route('/report')
def report():
	word = request.args.get('word')
	if word:
		word = word.lower()
		jobs = run_scrapper(word=word, last_page=1)
		count_result = len(jobs)

	else:
		return redirect('/')

	for i in jobs:
		print(i)

	return render_template(
		'report.html',
		searchingBy=word,
		countResult=count_result,
		Jobs=jobs
	)


# @app.route('/export')
# def export():
# 	try:
# 		word = request.args.get('word')
# 		if not word:
# 			raise Exception()
# 	except:
# 		return redirect('/')
#

app.run(host='0.0.0.0', debug=True)

