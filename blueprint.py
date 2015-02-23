from flask import Blueprint, render_template

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def home():
    return render_template('page2.html')

@main.route('/2')
def page2():
    return render_template('page2.html')

@main.route('/3')
def page3():
    return render_template('page3.html')

@main.route('/4')
def page4():
    return render_template('page4.html')

@main.route('/quiz')
def quiz():
    return render_template('quiz.html')
