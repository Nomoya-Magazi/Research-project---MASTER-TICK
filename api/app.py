from flask import Flask, jsonify
from flask_mysql_connector import MySQL
from flask_mail import Mail, Message

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

# My SMTP configuration
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'

#create a Mail object and pass it to my Flask to instance it
mail = Mail(app)

@app.route('/send_email')
def send_email():
    msg = Message('Hello', sender='your-email@example.com', recipients=['recipient@example.com'])
    msg.body = "This is a test email sent from Flask using SMTP"
    mail.send(msg)
    return "Email sent"

if __name__ == '__main__':
    app.run(debug=True)