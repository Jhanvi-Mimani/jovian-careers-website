from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Chennai, India',
  'salary': 'INR 10,00,000'
    
}, {
    'id': 2,
    'title': 'Frontend Engineer',
    'location': 'Pune, India',
    'salary': 'INR 8,00,000'
}, {
    'id': 3,
    'title': 'Backend Engineer',
    'location': 'Hyderabad, India',
    'salary': 'INR 15,00,000'
}]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Jovian')

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
