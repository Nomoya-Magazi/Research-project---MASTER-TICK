from flask import Flask, jsonify
from flask_mysql_connector import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'username'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'database_name'

# Create a MySQL object and pass my Flask app instance to it.
mysql = MySQL(app)

@app.route('/users')
def get_users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM users''')
    results = cur.fetchall()
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)