from flask import Flask, jsonify,request
# app n ame
app = Flask(__name__)
# Data Store
books = [{
"name":"bbbbbb",
"price" : 35,
"isbn" : 1234
},
{
"name" : "cccccc",
"price" : 40,
"isbn" : 1235
}]
# Validate book object

# route to Home directory
@app.route('/')
def hello():
    return "Hello welcome to the books website"
# route to data store
@app.route('/books')
def get_book():
    return jsonify({"books" : books})

# Route to querry book using Isbn of the book
@app.route('/books/<int:isbn>')
def get_book_info(isbn):
    return_val = {}
    for book in books:
        if book["isbn"] == isbn:
            return_val= {
            'name':book["name"],
            'price':book["price"]
            }
    return jsonify(return_val)
@app.route("/books", methods=["POST"])
def add_book():
    return jsonify(request.get_json())

app.run(port=5000)
