from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Dhaka, Bangladesh',
  'salary': 'Tk. 100000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Sylhet, Bangladesh',
  'salary': 'Tk. 90000'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Remote',
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'Atalanta, Italy',
  'salary': '$ 150000'
}]


@app.route("/")
def hello_jovian():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
