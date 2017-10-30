from flask import Flask
from flask import render_template
from flask import request
import yelp_api
import pprint
import json
import os
app = Flask(__name__)

@app.route('/')
def yelp_trip():
    return render_template('index.html', api_response=yelp_api.query_api('dinner', 'San Francisco', -1))

@app.route('/search', methods=['POST'])
def search():
    json_final = {}
    query = request.form['search'].split(',')
    # try:
    #     with open("search_response.json", "r") as f:
    #         json_final = json.load(f)
    #         return render_template('search.html', search_response=pprint.pformat(json_final), tabs=query, clusterJSON=json.dumps(json_final))
    # except FileNotFoundError as e:
    #     pass
    distance = request.form['search_distance']
    location = request.form['search_location']
    business_lst = yelp_api.query_api(query[0], location, -1)
    json_businesses = {}
    json_clusters = {}
    def build_clusters(cur_businesses, remaining_queries, json_cluster):
        for business in cur_businesses:
            json_businesses[business['id']] = business
            json_cluster[business['id']] = {}
            if not remaining_queries:
                continue
            coords = business['coordinates']
            coordinates_str = ','.join(map(str, (coords['latitude'], coords['longitude'])))
            next_businesses = yelp_api.query_api(remaining_queries[0], coordinates_str, distance)
            build_clusters(next_businesses, remaining_queries[1:], json_cluster[business['id']])

    build_clusters(business_lst, query[1:], json_clusters)
    json_final['businesses'] = json_businesses
    json_final['clusters'] = json_clusters
    # with open("search_response.json", "w") as f:
    #     json.dump(json_final, f)
        
    return render_template('search.html', search_response=pprint.pformat(json_final), tabs=query, clusterJSON=json.dumps(json_final), searchLimit=yelp_api.SEARCH_LIMIT)

def coord_str(json_business):
    coords = json_business['coordinates']
    return ','.join(map(str, (coords['latitude'], coords['longitude'])))

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)))
