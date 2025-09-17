from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Home Page!"

app.run()

@app.route('/')
def about():
    # return "About Page!"
    return """<h1>Welcome<h1>
                    <p>This is my first website<p>
            """


@app.route('/contact')
def contact():
    return "Contact Page"
app.run(delog=True)


if __name__ == '__main__':
    app.run(debug=true)