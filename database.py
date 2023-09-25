from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    id_value = {'id_val': id}
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :id_val"),
                          id_value)

    rows = result.all()
    if len(rows) == 0:
      return
    else:
      return rows[0]._asdict()


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text(
      "Insert into applications (job_id, full_name, email, linkedin_url, education, Work_experience, resume_url)Values(:job_id, :full_name, :email, :linkedin_url, :education, :Work_experience, :resume_url)"
    )

    all_data = {
      'job_id': job_id,
      'full_name': data['full_name'],
      'email': data['email'],
      'linkedin_url': data['linkedid'],
      'education': data['education'],
      'Work_experience': data['Work_experience'],
      'resume_url': data['resume_url']
    }

    conn.execute(query, all_data)
