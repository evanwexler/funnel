from flask import Blueprint, render_template

main = Blueprint('main', __name__, template_folder='templates')

crap = ['sdhfiosdufhsifuhsfusfhsidjfhsdlfijsndlfjsdfnlskdjfbnsdkjfhsdkljfhsdljkfhsdbkfjsdbfkjsdbfn.ksdjfbnsd.kjfbsd.kjfbsdkjfbsdkf.jbsdfksbdfk.jsdfb.sdkjfbsd.kjfbsdk.fbsdk.fbsd.fbksdbfsdkfb.sd']

@main.route('/')
def home():
    return render_template('home.html', crap=crap*30)

@main.route('/3')
def page3():
    return render_template('/page3.html')

@main.route('/quiz')
def quiz():
    return render_template('/quiz.html')
