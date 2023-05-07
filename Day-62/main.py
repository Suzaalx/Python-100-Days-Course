from flask import Flask, render_template
from flask_bootstrap import Bootstrap4
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap4(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    # only accept a URL
    location = StringField('Location URL', validators=[DataRequired(), URL(message='Please enter a valid URL.')])
    open_time = StringField('Open Time', validators=[DataRequired()])
    close_time = StringField('Close Time', validators=[DataRequired()])
    coffee = SelectField('Coffee Rating', choices=[('☕'), ('☕☕'), ('☕☕☕'), ('☕☕☕☕'), ('☕☕☕☕☕')], validators=[DataRequired()])
    wifi = SelectField('Wifi Strength Rating', choices=[('✘'), ('💪'), ('💪💪'), ('💪💪💪'), ('💪💪💪💪'), ('💪💪💪💪💪')], validators=[DataRequired()])
    power = SelectField('Power Socket Availability', choices=[('✘'), ('🔌'), ('🔌🔌'), ('🔌🔌🔌'), ('🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌')], validators=[DataRequired()])
    submit = SubmitField('Submit')



# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
    
        data= form.data
       
        datas=[]
        aa=[]
        # only get first 7 data
        for i in range(7):
            answer= list(data.keys())[i]
            print(answer)
            datas.append(data[answer])
            
        
        print(datas)
        with open('cafe-data.csv', 'a', newline='', encoding='utf8') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            # create a new row
            csv_writer.writerow(datas)
            
            
            
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


# delete the specific row in csv file
@app.route('/delete/<int:cafe_id>')
def delete():
    
    with open('cafe-data.csv', newline='', encoding='utf8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        print (csv_data[1])
        
    


if __name__ == '__main__':
    app.run(debug=True)
