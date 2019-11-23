import flask
from flask import render_template, request
# from flask_sqlalchemy import SQLAlchemy
import json
import sys
import datasource
app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def firstVisit():
    return render_template('homepage.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/aboutthedata')
def aboutTheData():
    return render_template('AboutTheData.html')


@app.route('/search-result', methods=['POST', 'GET'])
def searchResult():
	if request.method == 'POST':
		result = request.form

		ds = datasource.CourseQuery(None, None, result.get("search"), None, None, None)
		result = ds.masterQuery()

		resultList = []
		for item in result:
			print("hit")
			tempList = [item.getCourseDeptTag(), item.getCourseNumber(), item.getCourseName(), 
					item.getCourseTerm(), item.getCourseRequirements(), item.getCoursePeriod(),
					item.getCourseProfessor(), item.getCourseDescription()]
			resultList.append(tempList)

		if (len(resultList) == 0):
			resultList = ["No classes were met the the query criteria"]

		return render_template('result.html', result = resultList)


@app.route('/findaclass')
def findaclass():
    return render_template('findaClass.html')

@app.route('/query-result', methods=['POST', 'GET'])
def queryResult():
	if request.method == 'POST':
		result = request.form

		ds = datasource.CourseQuery(result.get("department"), result.get("courselevel"), result.get("search"), 
									result.get("term"), result.get("requirements"), result.get("period"))
	
		result = ds.masterQuery()

		resultList = []
		for item in result:
			tempList = [item.getCourseDeptTag(), item.getCourseNumber(), item.getCourseName(), 
					item.getCourseTerm(), item.getCourseRequirements(), item.getCoursePeriod(),
					item.getCourseProfessor(), item.getCourseDescription()]
			resultList.append(tempList)

		return render_template('result.html', result = resultList)

'''
@app.route('/result')
def result():
    return render_template('result.html')
'''
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)

    port = sys.argv[2]
    app.run(host=host, port=port)
