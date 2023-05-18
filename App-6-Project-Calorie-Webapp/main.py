from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from calorie import Calorie
from temperature import Temperature

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class CalorieFormPage(MethodView):
    def get(self):
        calorie_form = CalorieForm()
        return render_template('calories_form_page.html',
                               caloriesform=calorie_form)

    def post(self):
        calorie_form = CalorieForm(request.form)
        temperature = Temperature(country=calorie_form.country.data,
                                  city=calorie_form.city.data).get()
        calorie = Calorie(float(calorie_form.weight.data),
                          float(calorie_form.height.data),
                          float(calorie_form.age.data),
                          temperature=temperature)
        calories = calorie.calculate()
        return render_template('calories_form_page.html',
                               caloriesform=calorie_form,
                               calories=calories,
                               result=True)


class CalorieForm(Form):
    weight = StringField("Weight: ", default=70)
    height = StringField("Height: ", default=170)
    age = StringField("Age: ", default=30)
    country = StringField("Country: ", default="USA")
    city = StringField("City: ", default="New York")
    button = SubmitField("Calculate")


app.add_url_rule('/',
                 view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories_form',
                 view_func=CalorieFormPage.as_view('calories_form_page'))
Temperature(country="USA", city='New York').get()
app.run(debug=True)
