from flask import Flask, render_template
from utils import occupation

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/occupations")
def occupations():
    jobs_table =  occupation.reader()
    occupation.storer(jobs_table)
    occu_dict = occupation.librarian(jobs_table)
    rand_job = occupation.chooser()
    return render_template('occupations_page.html', job_var=rand_job, jobs_dict=occu_dict)
    
app.run()
