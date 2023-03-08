from flask import Flask, render_template, jsonify

app = Flask(__name__)

PerformanceStatistics = [
  {
    'id' : 1,
    'title' : 'Root Cause Analysis',
    'subject' : 'One important piece of data related to performance-related failures is the root cause of the failure. Understanding the underlying cause of a performance issue can help prevent similar failures from occurring in the future. This information can be gathered through thorough investigation and analysis of the failure, including data on system logs, error messages, and performance metrics.'
  },
  {
    'id' : 2,
    'title' : 'Impact Assessment',
    'subject' : 'Another important piece of data related to performance-related failures is the impact of the failure on the organization. This can include data on lost revenue, productivity, or customer satisfaction. Understanding the impact of a performance issue can help prioritize remediation efforts and allocate resources appropriately'
    
  },
  {
      'id' : 3,
      'title' : 'Response Time',
      'subject' : 'Response time is a critical metric for measuring the performance of applications and systems. Monitoring response times can help identify performance issues and provide insights into potential bottlenecks. Data on response times can be gathered through performance testing and monitoring tools, and can help inform performance tuning efforts.'
  }
]

@app.route("/")
def hello_world():
    return render_template("home.html", data=PerformanceStatistics)

@app.route("/assessment.html")
def assessment():
    return render_template("assessment.html", data=PerformanceStatistics)

@app.route("/performancestatistics")
def list_data():
  return jsonify(PerformanceStatistics)

if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug=True)
