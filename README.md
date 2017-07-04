# YelpTrip
Plan a trip by finding different kinds of destinations in the same area through Yelp.

## To run:

Clone repo

Virtualenv is recommended. In virtualenv, install dependencies with ```pip install -r requirements.txt```

Get a client ID and secret for access to the Yelp API. Put the id and secret into your environment variables.

```
CLIENT_ID={your Yelp client ID}
CLIENT_SECRET={your Yelp client secret}
```



```export FLASK_APP=yelp_trip.py```

```flask run```
