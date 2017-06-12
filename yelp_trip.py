from flask import Flask
from flask import render_template
from flask import request
import yelp_api
app = Flask(__name__)

@app.route('/')
def yelp_trip():
    return render_template('base.html', api_response = yelp_api.query_api('dinner', 'San Francisco'))

@app.route('/search', methods=['POST'])
def search():
    query = request.form['search']
    return render_template('base.html', search_response = query)

if __name__ == '__main__':
    app.run()
