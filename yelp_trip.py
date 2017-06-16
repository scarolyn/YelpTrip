from flask import Flask
from flask import render_template
from flask import request
import yelp_api
app = Flask(__name__)

@app.route('/')
def yelp_trip():
    return render_template('base.html', api_response = yelp_api.query_api('dinner', 'San Francisco', -1))

@app.route('/search', methods=['POST'])
def search():
    query = request.form['search'].split(',')
    distance = request.form['search_distance']
    location = request.form['search_location']
    clusters = [[i] for i in yelp_api.query_api(query[0], location, -1)]
    for x in range(1, len(query)):
        new_cluster = []
        for cluster in clusters:
            last_business = cluster[-1]
            cur_businesses = yelp_api.query_api(query[x], last_business['coordinates'], distance)
            new_cluster.append([cluster.append(cur_business)] for cur_business in cur_businesses)
        clusters = new_cluster

    # return render_template('base.html', clusters)
    return print(clusters)

if __name__ == '__main__':
    app.run()
