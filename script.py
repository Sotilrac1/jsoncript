try: 

    from flask import Flask, redirect, url_for, request, render_template
    import pandas as pd
    from flask_wtf.file import FileField
    from wtforms import SubmitField
    from flask_wtf import Form
    import sqlite3
    print(" All Modules loaded......")

except:
    print(" Some modules are missing.......")


app =Flask(__name__)
app.config["SECRET_KEY"] = "secret"


@app.route('/', methods=['POST','GET'])
def index():
    form = Upload_Form()
    return render_template("home.html",form=form)

class Upload_Form(Form):
    file = FileField()
    submit = SubmitField("submit")

            
if __name__ == '__main__':
    app.run(debug=True)