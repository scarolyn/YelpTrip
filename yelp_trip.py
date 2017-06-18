from flask import Flask
from flask import render_template
from flask import request
import yelp_api
import pprint
app = Flask(__name__)

@app.route('/')
def yelp_trip():
    return render_template('base.html', api_response=yelp_api.query_api('dinner', 'San Francisco', -1))

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
            coords = last_business['coordinates']
            coordinates_str = ','.join(map(str, (coords['latitude'], coords['longitude'])))
            cur_businesses = yelp_api.query_api(query[x], coordinates_str, distance)
            
            new_cluster.extend(cluster + [business] for business in cur_businesses)
        clusters = new_cluster
    return render_template('base.html', search_response=pprint.pformat(clusters))

if __name__ == '__main__':
    app.run()
