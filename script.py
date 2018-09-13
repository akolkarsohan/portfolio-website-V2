from flask import Flask, render_template

app=Flask(__name__)

# Home Page
@app.route('/')
def home():
  return render_template("homepage.html")

# Portfolio Page
@app.route('/portfolio/')
def portfolio():
  return render_template("portfolio.html")

# Architecture Page
@app.route('/architecture/')
def architecture():
  return render_template("architecture.html")

# Serverless Section
# Serverless Main Page
@app.route('/serverless/')
def serverless():
  return render_template("serverless/serverless-main-page.html")

# Serverless SQS SNS Page
@app.route('/serverless/autoscaling-sqs-sns')
def serverless_autoscaling_sqs_sns():
  return render_template("serverless/autoscaling-sqs-sns.html")

# DevOps Section
# DevOps Main Page
@app.route('/devops/')
def devops():
  return render_template("devops/devops-main-page.html")

# DevOps ElasticSearch Page
@app.route('/devops/elasticsearch')
def devops_elasticsearch():
  return render_template("devops/elasticsearch/elasticsearch-page.html")

# About Me Section
@app.route('/aboutme/')
def aboutme():
  return render_template("aboutme.html")

# Linux Section
# Linux Main Page
@app.route('/linux/')
def linux():
  return render_template("linux/linux-main-page.html")

# Linux Bash Scripts Page 
@app.route('/linux/linux_bash_scripts')
def linux_bash_scripts():
  return render_template("linux/linux-bash-scripts-page.html")

# Linux User and Grous Mgmt Page 
@app.route('/linux/linux_user_group_mgmt')
def linux_user_group_mgmt():
  return render_template("linux/linux-user-and-groups-page.html")


if __name__=="__main__":
  app.run(debug=True,host='0.0.0.0',port=8080)
