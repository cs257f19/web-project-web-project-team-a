import flask
from flask import render_template, request
import json
import sys
import datasource
app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def firstVisit():
	'''
	 Routes and renders to homepage of website
	'''
    return render_template('homepage.html')

@app.route('/aboutthedata')

def aboutTheData():
	'''
	Routes and renders to about the data page of website
	'''
    return render_template('AboutTheData.html')


@app.route('/findaclass')
def findaclass():
	'''
	Routes and renders to find a class page of website
	'''
    return render_template('findaClass.html')

@app.route('/search-result', methods=['POST', 'GET'])
def searchResult():
	'''
	Routes and renders to result page of website from homepage.html. Creates CourseQuery object using result and performs a master query,
	resulting in resultList containing courses that match search criteria

	Parameters:
		result - form pulled from homepage.html 

	Renders:
		result.html if there were classes that match search criteria
		noResult.html if no classes match search criteria

	'''
	if request.method == 'POST':
		result = request.form

		ds = datasource.CourseQuery(None, None, result.get("search"), None, None, None)
		result = ds.masterQuery()

		resultList = []
		for item in result:
			tempList = [item.getCourseDeptTag(), item.getCourseNumber(), item.getCourseName(), 
					item.getCourseTerm(), item.getCourseRequirements(), item.getCoursePeriod(),
					item.getCourseProfessor(), item.getCourseDescription()]
			resultList.append(tempList)

		if len(resultList) != 0:
			return render_template('result.html', result = resultList)
		else:
			return render_template('noResult.html')



@app.route('/query-result', methods=['POST', 'GET'])
def queryResult():
	'''
	Routes and renders to result page of website from findaclass.html. Creates CourseQuery object using result and performs a master query,
	resulting in resultList containing courses that match search criteria

	Parameters:
		result - form pulled from findaClass.html 

	Renders:
		result.html if there were classes that match search criteria
		noResult.html if no classes match search criteria

	'''
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

		if len(resultList) != 0:
			return render_template('result.html', result = resultList)
		else:
			return render_template('noResult.html')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)

    port = sys.argv[2]
    app.run(host=host, port=port)
