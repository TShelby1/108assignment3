
from flask import Flask
import json
from mock_data import mock_catalog

app = Flask('Server')

# endpoints


@app.route("/")
def root():
    return "Welcome to our Server"

########################
########### API Catalog ###############
# defaults to get route unless specified


@app.route("/api/about", methods=["POST"])
def about():
    me = {
        "first": "Albert",
        "last": "Lara"

    }
    return json.dumps(me)  # parse into json then return


@app.route("/api/catalog")
def get_catalog():
    return json.dumps(mock_catalog)


#/api/catalog/cheapest
# returns the cheapest product in the catalog

@app.route("/api/catalog/cheapest")
def get_cheapest():
    solution = mock_catalog[0]
    for prod in mock_catalog:
        if prod["price"] < solution["price"]:
            solution = prod

    return json.dumps(solution)

@app.route("/api/catalog/total")
def get_sum():
    total = 0
    for total in mock_catalog:
        total+= num

    return json.dumps(total)
    


app.run(debug=True)
