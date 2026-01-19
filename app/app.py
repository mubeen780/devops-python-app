from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="db",
    database="devopsdb",
    user="devops",
    password="devops"
)

@app.route("/", methods=["GET", "POST"])
def index():
    cur = conn.cursor()
    if request.method == "POST":
        name = request.form["name"]
        cur.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        conn.commit()

    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    return render_template("index.html", users=users)

app.run(host="0.0.0.0", port=5000)
