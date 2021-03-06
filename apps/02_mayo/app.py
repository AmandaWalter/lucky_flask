# -*- coding: utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    users = [
        {
            'username': "faris",
            'email': "faris@theluckybead.com"
        },
        {
            'username': "Pilot Andy",
            'email': "report_to_faa@faa.gov"
        },
        {
            'username': "David",
            'email': "david@example.com"
        }
    ]

    template_name = "home.html"
    return render_template(template_name, users=users)

if __name__ == "__main__":
    app.static_folder = '../static'
    app.static_url_path = 'static'
    app.debug = True
    app.run()
