from flask import Flask
from flask import render_template
from extensions import db
from extensions import mail
import base64
import os
from flask import request
from flask import redirect
import datetime

from models.employee import Employee
from models.manager import Manager
import utils

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/aig_prd_form'
app.config['SQLALCHEMY_POOL_SIZE'] = 5
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 120
app.config['SQLALCHEMY_POOL_RECYCLE'] = 280

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = r'kmt.aigbusiness@gmail.com'
app.config['MAIL_PASSWORD'] = r'atul123@#'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

db.init_app(app)
mail.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/employee" , methods=['POST'])
def save_data():
    emp_name = request.form.get('emp_name')
    emp_code = request.form.get('emp_code')
    emp_email= request.form.get('emp_email')
    job_function = request.form.get('job_function')
    date = request.form.get('date')
    reviewer_name = request.form.get('reviewer_name')
    reviewer_code = request.form.get('reviewer_code')
    self_assessment1 = request.form.get('self_assessment1')
    self_assessment1_comment1 = request.form.get('self_assessment1_comment1')
    self_assessment2 = request.form.get('self_assessment2')
    self_assessment2_comment2 = request.form.get('self_assessment2_comment2')
    self_assessment3 = request.form.get('self_assessment3')
    self_assessment3_comment3 = request.form.get('self_assessment3_comment3')
    self_assessment4 = request.form.get('self_assessment4')
    self_assessment4_comment4 = request.form.get('self_assessment4_comment4')
    self_assessment5 = request.form.get('self_assessment5')
    self_assessment5_comment5 = request.form.get('self_assessment5_comment5')
    self_assessment6 = request.form.get('self_assessment6')
    self_assessment6_comment6 = request.form.get('self_assessment6_comment6')
    rev_email = request.form.get('rev_email')


    employee_form = Employee(
        emp_code=emp_code,
        emp_name=emp_name,
        emp_email=emp_email,
        job_function=job_function,
        date=date,
        reviewer_name=reviewer_name,
        reviewer_code=reviewer_code,
        self_assessment1=self_assessment1,
        self_assessment1_comment1=self_assessment1_comment1,
        self_assessment2=self_assessment2,
        self_assessment2_comment2=self_assessment2_comment2,
        self_assessment3=self_assessment3,
        self_assessment3_comment3=self_assessment3_comment3,
        self_assessment4=self_assessment4,
        self_assessment4_comment4=self_assessment4_comment4,
        self_assessment5=self_assessment5,
        self_assessment5_comment5=self_assessment5_comment5,
        self_assessment6=self_assessment6,
        self_assessment6_comment6=self_assessment6_comment6,
        rev_email = rev_email,

        IP_addr=request.remote_addr,
        Location=request.form.get('location'),
        UserAgent=request.user_agent.browser,
        OperatingSystem=request.user_agent.platform,
        Time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

    )

    db.session.add(employee_form)
    db.session.commit()
    utils.send_link_as_mail(
        emp_name=emp_name,
        # emp_email=emp_email,
        rev_email=rev_email,
        reviewer_code=reviewer_code,
        emp_code=emp_code,

    )
    return redirect('/success')

@app.route("/success")
def success():
    return render_template('thankyou.html')

@app.route("/document/<string:emp_code>/<string:reviewer_code>")
def document(emp_code,reviewer_code):
    the_document = Employee.query.filter(Employee.emp_code == emp_code,Employee.reviewer_code==reviewer_code).order_by("id desc").first()

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    #return str(BASE_DIR)

    return render_template('document.html', the_document=the_document, base_dir=BASE_DIR)


@app.route("/manager",methods=['POST'])
def save_managerdata():

    emp_code1 = request.form.get('emp_code1')
    reviewer_name1 = request.form.get('reviewer_name1')
    reviewer_code1 = request.form.get('reviewer_code1')

    manager_assessment1 = request.form.get('manager_assessment1')
    manager_assessment1_comment1 = request.form.get('manager_assessment1_comment1')
    total_score1 = request.form.get('total_score1')
    achieved_score1 = request.form.get('achieved_score1')

    manager_assessment2 = request.form.get('manager_assessment2')
    manager_assessment2_comment2 = request.form.get('manager_assessment2_comment2')
    total_score2 = request.form.get('total_score2')
    achieved_score2 = request.form.get('achieved_score2')

    manager_assessment3 = request.form.get('manager_assessment3')
    manager_assessment3_comment3 = request.form.get('manager_assessment3_comment3')
    total_score3 = request.form.get('total_score3')
    achieved_score3 = request.form.get('achieved_score3')

    manager_assessment4 = request.form.get('manager_assessment4')
    manager_assessment4_comment4 = request.form.get('manager_assessment4_comment4')
    total_score4 = request.form.get('total_score4')
    achieved_score4 = request.form.get('achieved_score4')

    manager_assessment5 = request.form.get('manager_assessment5')
    manager_assessment5_comment5 = request.form.get('manager_assessment5_comment5')
    total_score5 = request.form.get('total_score5')
    achieved_score5 = request.form.get('achieved_score5')

    manager_assessment6 = request.form.get('manager_assessment6')
    manager_assessment6_comment6 = request.form.get('manager_assessment6_comment6')
    total_score6 = request.form.get('total_score6')
    achieved_score6 = request.form.get('achieved_score6')

    rev_email1 = request.form.get('rev_email1')

    manager_form = Manager(

        emp_code1 = emp_code1,
        reviewer_name1 = reviewer_name1,
        reviewer_code1 = reviewer_code1,
        manager_assessment1 = manager_assessment1,
        manager_assessment1_comment1 = manager_assessment1_comment1,
        total_score1 = total_score1,
        achieved_score1 = achieved_score1,

        manager_assessment2=manager_assessment2,
        manager_assessment2_comment2=manager_assessment2_comment2,
        total_score2=total_score2,
        achieved_score2=achieved_score2,

        manager_assessment3=manager_assessment3,
        manager_assessment3_comment3=manager_assessment3_comment3,
        total_score3=total_score3,
        achieved_score3=achieved_score3,

        manager_assessment4=manager_assessment4,
        manager_assessment4_comment4=manager_assessment4_comment4,
        total_score4=total_score4,
        achieved_score4=achieved_score4,

        manager_assessment5=manager_assessment5,
        manager_assessment5_comment5=manager_assessment5_comment5,
        total_score5=total_score5,
        achieved_score5=achieved_score5,

        manager_assessment6=manager_assessment6,
        manager_assessment6_comment6=manager_assessment6_comment6,
        total_score6=total_score6,
        achieved_score6=achieved_score6,



        IP_addr=request.remote_addr,
        Location=request.form.get('location'),
        UserAgent=request.user_agent.browser,
        OperatingSystem=request.user_agent.platform,
        Time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

    )


    db.session.add(manager_form)
    db.session.commit()
    utils.send_manager_link_as_mail(

        rev_email1=rev_email1,
        reviewer_code1=reviewer_code1,
        emp_code1=emp_code1,

    )
    return redirect('/success')

@app.route("/final_form/<string:emp_code1>/<string:reviewer_code1>")
def final_document(emp_code1,reviewer_code1):
    the_final_document = Manager.query.filter(Manager.emp_code1 == emp_code1,Manager.reviewer_code1==reviewer_code1).order_by("id desc").first()
    the_document = Employee.query.filter(Employee.emp_code == emp_code1,Employee.reviewer_code == reviewer_code1).order_by("id desc").first()

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    #return str(BASE_DIR)

    return render_template('finaldocument.html', the_document=the_document,the_final_document=the_final_document, base_dir=BASE_DIR)
