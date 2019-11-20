import flask
from flask import render_template, request
# from flask_sqlalchemy import SQLAlchemy
import json
import sys
import datasource
app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


# db = SQLAlchemy()


@app.route('/')
def hello():
    return render_template('homepage.html')

@app.route('/search-result', methods=['POST', 'GET'])
def searchResult():
	if request.method == 'POST':
		result = request.form

		ds = datasource.CourseQuery(None, None, result.get("search"), None, None, None)
		#result = ds.getCourseByDeptTag()
		result = ds.getCourseByName()
		#result = result.getCourseDeptTag()

<<<<<<< HEAD
        resultList = []
        for item in result:
            tempList = [item.getCourseDeptTag(), item.getCourseNumber(), item.getCourseName(), 
            			item.getCourseTerm(), item.getCourseRequirements(), item.getCoursePeriod(),
            			item.getCourse()]
            # tempList = [1, 2, 3, 4, 5, 6]
            resultList.append(tempList)
=======
		#description = "Showing all classes that have  " + result.get("search") + " sorted alphabetically"
		#result = ds.getCourseByName()
>>>>>>> 4b6e511d0ac409c384a1df01093d84b991ee8526

		resultList= []
		for item in result:
			tempList = [item.getCourseDeptTag(), item.getCourseNumber(), item.getCourseName(), item.getCoursePrerequisites(), item.getCourseRequirements(), item.getCourseTerm()]
			#tempList = [1, 2, 3, 4, 5, 6]
			resultList.append(tempList)


		return render_template('result.html', result = resultList)

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)

    port = sys.argv[2]
    app.run(host=host, port=port)
