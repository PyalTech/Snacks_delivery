from flask import Flask, render_template, url_for
app = Flask(__name__)



@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/services")
def services():
    return render_template('services.html', title='Services')

@app.route("/contact")
def contact():
    return render_template('contact.html', title='contact')


@app.route("/blog")
def blog():
    return render_template('blog.html', title='Blog')


if __name__ == '__main__':
    app.run(debug=True)