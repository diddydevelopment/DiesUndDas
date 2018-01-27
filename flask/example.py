from flask import Flask
app = Flask(__name__)

master_html = """
<html>
<head>
<title>Willkommen alter</title>
</head>
<body>
<h1>Meine persöhnliche Homepage</h1>
<ul>
<li><a href="/">Startseite</a></li>
<li><a href="/say_hello">Sage hallo</a></li>
</ul>
%s
</body>
</html>
"""




@app.route("/say_hello")
def hello():
    return master_html % "Hello!"


@app.route("/")
def main():
    return master_html % "Welcome!"

if __name__ == "__main__":
    app.run()