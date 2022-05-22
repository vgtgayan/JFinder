
from flask import Flask, jsonify, request, redirect
from JfinderModelTfid import JfinderModel
from flask_cors import CORS, cross_origin

app = Flask(__name__)

jfmodel= JfinderModel("test-data-54000")


@app.route('/get_jira/<sstr>', defaults={'mr' : '10'})
@app.route('/get_jira/<sstr>/<mr>')
@cross_origin()
def get_jira(sstr,mr):
    jiraList = jfmodel.getresult(int(mr), sstr)
    return jsonify(jiraList)

@app.route('/go_to/<sstr>', defaults={'mr' : '10'})
@app.route('/go_to/<sstr>/<mr>')
def go_to(sstr,mr):
    results = jfmodel.getresult(int(mr), sstr)
    jiraList = [x['key'] for x in results]
    link = "https://jira.internal.synopsys.com/issues/?jql=key%20in%20("+"%2C%20".join(jiraList) +")"
    return redirect(link)


