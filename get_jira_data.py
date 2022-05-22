#!/depot/Python-3.6.2/bin/python
import os
import getpass
import sys
import re
from jira import JIRA
from jira.exceptions import JIRAError
import argparse


mn = 1000
delimiter = ","


#pass commandlne arguments
parser = argparse.ArgumentParser()
parser.add_argument('-jql', help='jql')
parser.add_argument('-o','--out', help='output name without file extension')
args = parser.parse_args()

#get username and password
usr = getpass.getuser()
filepath = os.path.expanduser("~/.jira_password")
try:
    with open(filepath, 'r') as file:
        pwd = file.read().rstrip("\n")
except:
    print("Cani't open password file in ~/.jira_password \nEnter your password:")
    pwd = getpass.getpass()

try:
  #create jira object
  jira_options = {'server': 'https://jira.internal.synopsys.com','verify':'/etc/ssl/certs/ca-bundle.crt'}
  jira = JIRA(options=jira_options, basic_auth=(usr,pwd),max_retries=0)
except JIRAError as e:
  if e.status_code == 401:
    print ("Login Failed check your password")
  sys.exit()

#read by jql
issues_tmp = jira.search_issues(args.jql, maxResults=1,startAt=0)
total = issues_tmp.total

csv_file = open(args.out+".csv","w")
header = "key,product_l1,summary,description"
csv_file.write(header+"\n")

def writetocsv(data):
    csv_file.write(delimiter)

    if data != None:
        data = re.sub(r",|\r|\n"," ", data)
        csv_file.write(data)



for i in range(0,total,mn):
    issues = jira.search_issues(args.jql, maxResults=mn,startAt=i)
    for issue in issues:
        #get fields  
        key = issue.key 
        fields = issue.fields
    
        #key ------------------------------------------------
        csv_file.write(key) 
     
        #product l1 -----------------------------------------
        writetocsv(fields.customfield_11501)
    
        #summary --------------------------------------------
        writetocsv(fields.summary)
     
        #description ----------------------------------------
        writetocsv(fields.description)
     
        #end data write new line -----------------------------
        csv_file.write("\n") 




csv_file.close()



