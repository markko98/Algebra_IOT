from flask import Flask
from flask import jsonify
from flask_mysqldb import MySQL

mysql = MySQL()
app = Flask(__name__)

#mySQL configuration
app.config['MYSQL_USER'] = 'bookuser'
app.config['MYSQL_PASSWORD'] = 'bookuser123'
app.config['MYSQL_DB'] = 'booksDB'
app.config['MYSQL_HOST'] = 'localhost'
mysql.init_app(app)

books = [
    {'name' : 'Snow White', 'author':'Grimm brothers'},
    {'name' : "Alice's adventures in wonderland", 'author':'Lewis Carrol'},
]



@app.route("/", methods=['GET'])
def hello_world():
	return "Hello world"

@app.route("/api/books", methods=['GET'])
def return_all():
    return jsonify({'books': books})


@app.route("/api/books/titles", methods=['GET'])
def return_titles():
    titles=[]
    for book in books:
        titles.append(book['name'])
    
    return jsonify({'books': books})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True);