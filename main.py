from flask import url_for
from flask import Flask,render_template,request,session,redirect,flash
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@127.0.0.1/E_cell"
app.secret_key = 'secret key'

db=SQLAlchemy(app)

from models import Startup, Attendies
from forms import RegistrationForm, AudienceForm


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        entry = Startup(Name=form.name.data,Email=form.email.data,Phone_num=form.phone.data,Startupname=form.startupname.data,Teamnumber=form.teamnumber.data)
        db.session.add(entry)
        db.session.commit()
        flash(f'Registration success for {form.startupname.data}!', 'success')
        return redirect('/')

    return render_template("register.html", form=form)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/attendies", methods=['GET', 'POST'])
def attendies():
    form = AudienceForm()
    if form.validate_on_submit():
        entry = Attendies(Name=form.name.data,Email=form.email.data,Phone_num=form.phone.data,City=form.city.data,College=form.college.data)
        db.session.add(entry)
        db.session.commit()
        flash(f'Entry created for {form.name.data}!', 'success')
        return redirect('/')

    return render_template("attendies.html", form=form)

if __name__ == '__main__':
    app.run(debug = True)



