import pdfkit

from flask import (
    Flask,
    render_template,
    make_response,
    request
)


app = Flask(__name__, template_folder="templates")


@app.route('/')
def home():
    return render_template("home.html")


@app.route("/demo")
def demo():
    title = request.args.get("title")
    article = request.args.get("article")
    html_text = render_template("demo.html", title=title, article=article)
    print(html_text)

    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
    }

    pdf = pdfkit.from_string(html_text, False, options=options)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filenam=export.pdf'

    return response


if __name__ == '__main__':
    app.run(debug=True)
