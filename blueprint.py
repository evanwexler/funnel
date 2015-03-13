from flask import Blueprint, render_template

main = Blueprint('main', __name__, template_folder='templates')

# @main.route('/')
# def home():
#     return render_template('page1.html')

@main.route('/')
def page2():
    return render_template('page2.html')

@main.route('/3')
def page3():
    return render_template('page3.html')

@main.route('/4')
def page4():
    return render_template('page4.html')
    
@main.route('/5')
def page5():
    return render_template('page5.html')
    
@main.route('/6')
def page6():
    return render_template('page6.html')
    
@main.route('/7')
def page7():
    return render_template('page7.html')

@main.route('/8')
def page8():
    return render_template('page8.html')

@main.route('/9')
def page9():
    return render_template('page9.html')

@main.route('/10')
def page10():
    return render_template('page10.html')
    
@main.route('/quiz')
def quiz():
    return render_template('quiz.html')
