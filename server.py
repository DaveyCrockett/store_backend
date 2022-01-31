import random
from flask import Flask, request, abort
from mock_data import catalog
import json
from config import db
from flask_cors import CORS
from bson import ObjectId

app = Flask(__name__)
CORS(app)  # DANGER!! Anyone can connect to this server
me = {
    "name": "David",
    "last": "Paredes",
    "age": 33,
    "occupation": "Package Handler",
    "hobbies": [],
    "address": {
        "street": "Walker",
        "number": 2345,
        "city": "Ranger"
    }
}


@app.route("/")
def home():
    return "Hello from Python!"


@app.route("/test")
def any_name():
    return "I'm a test function"


@app.route("/about")
def about_me():
    return me["name"] + " " + me["last"]


# ********************************************
# **********API ENDPOINTS*********************
# ********************************************

@app.route("/api/catalog")
def get_catalog():
    cursor = db.products.find({})
    results = []
    for product in cursor:
        product["_id"] = str(product["_id"])
        results.append(product)
    return json.dumps(results)


@app.route("/api/catalog", methods=["post"])
def save_product():
    product = request.get_json()
    print(product)
    # data validations
    if not "title" in product or len(product["title"]) < 5:
        return abort(400, "Title is required and should be at least 5 characters long.")
    if not "price" in product:
        return abort(400, "Price is required")
    if not (isinstance(product["price"], float) and not isinstance(product["price"], int)):
        return abort(400, "Price should be a valid number.")
    if product["price"] <= 0:
        return abort(400, "The price must be greater than 0.")

    db.products.insert_one(product)
    product["_id"] = str(product["_id"])
    return json.dumps(product)


@app.route("/api/cheapest")
def get_cheapest():
    # find the cheapest product on the catalog list
    cursor = db.products.find({})
    cheapest = cursor[0]
    for product in cursor:
        if product["price"] < cheapest["price"]:
            cheapest = product

    cheapest["_id"] = str(cheapest["_id"])
    # return json
    return json.dumps(cheapest)


@app.route("/api/product/<id>")
def get_product(id):
    #  find the product whose _id is equal to id
    if (not ObjectId.is_valid(id)):
        return abort(400, "Id is not a valid ObjectID")

    result = db.products.find_one({"_id": ObjectId(id)})
    if not result:
        return abort(404)
    result["_id"] = str(result["_id"])
    return json.dumps(result)


@app.route("/api/catalog/<category>")
def get_by_category(category):
    result = []
    cursor = db.products.find({"category": category})
    for prod in cursor:
        prod["_id"] = str(prod["_id"])
        result.append(prod)

    return json.dumps(result)


@app.route("/api/categories")
def get_categories():
    categories = []
    for product in catalog:
        if product["category"] not in categories:
            categories.append(product["category"])
    return json.dumps(categories)


@app.route("/api/reports/prodCount")
def get_prod_count():
    count = len(catalog)
    return json.dumps(count)


@app.route("/api/reports/total")
def get_total():
    total = 0
    for product in catalog:
        total += product["price"] * product["stock"]
    return json.dumps(total)


@app.route("/api/reports/highestInvested")
def highest_invested():
    highest = catalog[0]
    for product in catalog:
        prod_invest = product["price"] * product["stock"]
        high_invest = highest["price"] * highest["stock"]
        if prod_invest > high_invest:
            highest = product
    # return json
    return json.dumps(highest)


####################################################
##############Coupon Codes endpoints################
####################################################

# GET


@app.route("/api/couponCodes")
def get_couponCodes():
    cursor = db.couponCodes.find({})
    result = []

    for coupon in cursor:
        coupon["_id"] = str(coupon["_id"])
        result.append(coupon)

    return json.dumps(result)


# Post /api/couponCodes
# 1 - create the end point
# 2 - get the json from the reqs
#   - validate (code, discount)
# 3 - save the couponCode to db.couponCodes
# 4 - return the saved object as json
# 5 - test it


@app.route("/api/couponCodes", methods=["POST"])
def save_coupon():
    couponCode = request.get_json()

    if not "code" in couponCode:
        return abort(400, "Code is required")

    if not "discount" in couponCode:
        return abort(400, "Discount is required")

    db.couponCodes.insert_one(couponCode)

    couponCode["_id"] = str(couponCode["_id"])
    return json.dumps(couponCode)


# retrieve specific couponCodes by its code
@app.route("/api/couponCodes/<code>")
def valid_code(code):
    coupon = db.couponCodes.find_one({"code": code})
    if not coupon:
        return abort(404)

    coupon["_id"] = str(coupon["_id"])

    return json.dumps(coupon)


# start the server


app.run(debug=True)
