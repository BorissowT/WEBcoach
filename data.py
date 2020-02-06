from wtforms import StringField, BooleanField, PasswordField, RadioField
from wtforms.validators import NumberRange, DataRequired, Email, NumberRange
from flask_wtf import FlaskForm
days={"mon":"Понедельник","tue":"Вторник","wed":"Среда","thu":"Четверг","fri":"Пятница","sat":"Суббота","sun":"Воскресенье"}
goals={
  "travel": "Для путешествий",
  "study": "Для учебы",
  "work": "Для работы",
  "relocate": "Для переезда"
}


class USER(FlaskForm):
  name = StringField('Name', description='Введите ваше имя', validators=[DataRequired()])
  number = StringField('Number', description='Введите ваш номер телефона', validators=[DataRequired()])

class REQUEST(FlaskForm):
    name = StringField('Name', description='Введите ваше имя', validators=[DataRequired()])
    number = StringField('Number', description='Введите ваш номер телефона', validators=[DataRequired()])
    goal = RadioField("goal", choices=[("travel", "Для путешествий"), ("study", "Для учебы"), ("work", "Для работы"),
                                       ("relocate", "Для переезда")], validators=[DataRequired()])
    free_time = RadioField("free_time", choices=[("1-2", "1-2 часа в неделю"), ("3-5", "3-5 часа в неделю"),
                                                 ("5-7", "5-7 часов в неделю"), ("7-10", "7-10 часов в неделю")],
                           validators=[DataRequired()])