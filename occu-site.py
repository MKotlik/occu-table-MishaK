from flask import Flask, render_template
import occupation

app = Flask(__name__)

@app.route("/")
def index():
    return 'Just go to <a href="/occupations">occupations</a>.'

@app.route("/occupations")
def occupations():
    jobs_table =  occupation.reader()
    occupation.storer(jobs_table)
    occu_dict = occupation.libraran(jobs_table)
    rand_job = occupation.chooser()
    return render_template('occupations_page.html', job_var=rand_job, jobs_dict=occu_dict)
    
