from flask import Flask
from flask import jsonify
from flask_mysqldb import MySQL
from flask import request

mysql = MySQL()
app = Flask(__name__)

#mySQL configuration
app.config['MYSQL_USER'] = 'bookUser'
app.config['MYSQL_PASSWORD'] = 'bookUser123'
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
    conn = mysql.connect;
    cursor = conn.cursor()
    
    cursor.execute("SELECT Name, Author FROM book")
    rows = cursor.fetchall()
    return jsonify({'rows': rows})


@app.route("/api/books/titles", methods=['GET'])
def return_titles():
    conn = mysql.connect;
    cursor = conn.cursor()
    
    cursor.execute("SELECT Name FROM book")
    rows = cursor.fetchall()
    return jsonify({'titles': rows})
    
    
@app.route("/api/books", methods=['POST'])
def add_book():
    new_book = request.get_json()
    conn = mysql.connect;
    cursor = conn.cursor()
    
    cmd = "INSERT INTO book (Name, Author) VALUES (%s,%s)"
    params = (new_book['Name'], new_book['Author'])
    
    cursor.execute(cmd, params)
    conn.commit()
    cursor.close()
    conn.close()
    
    return "200"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True);