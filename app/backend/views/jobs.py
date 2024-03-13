from flask import Blueprint, render_template
from app.database.models import Job
jobs_bp = Blueprint('jobs', __name__)

@jobs_bp.route('/')
def index():
    # Fetch job listings from the database
    jobs = Job.query.all()
    return render_template('index.html', jobs=jobs)

@jobs_bp.route('/job/<int:job_id>')
def job_details(job_id):
    # Fetch job details from the database
    job = Job.query.get_or_404(job_id)
    return render_template('job_details.html', job=job)
