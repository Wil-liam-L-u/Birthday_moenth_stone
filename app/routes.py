from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
    # return "We gonna tell u your birthday stone based on your birthday month!"
@app.route('/result', methods = ["get", "post"])
#
def result():
    userinfo= dict(request.form)
    print(userinfo)
    birthday_month = userinfo["birthday_month"]
    print(birthday_month)
    nickname = userinfo["nickname"]
    print(nickname)
    # get the information from the form
    # store month as variable
    # call stone function month as arugment, store output
    output = model.stone(birthday_month)
    print(output)
    # send output


    return render_template("result.html",nickname = nickname, birthday_month = output)

#
