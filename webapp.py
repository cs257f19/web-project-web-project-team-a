import flask
from flask import render_template, request
# from flask_sqlalchemy import SQLAlchemy
import json
import sys

app = flask.Flask(__name__)


# db = SQLAlchemy()


@app.route('/')
def hello():
    return render_template('homepage.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = request.form
		ds = datasource.DataSource()
		description = "Showing all names beginning with " + result.get("Letter") + " sorted alphabetically"
		result = ds.getCourseName(result.get("Letter"))
		return render_template('result.html', result = result, description = description)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
