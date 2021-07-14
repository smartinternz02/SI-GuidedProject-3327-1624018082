from flask import Flask,render_template,request
#from gevent.pywsgi import WSGIServer
import numpy as np
import re
import requests
import json
import csv
import pandas as pd
#import os

app = Flask(__name__)

def check(output):
    url = "https://twinword-topic-tagging.p.rapidapi.com/generate/"
    payload = {"text": output}
    #print(payload)
    headers = {
    'x-rapidapi-key': "27f0759a6amsh44b4c9e7ea41a96p1b312ejsn57cbda6388ab",
    'x-rapidapi-host': "twinword-topic-tagging.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=payload)
    print(response.text)
    return response.json()["topic"]
    #return var


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/summarizer")
def summarizer():
    return render_template('summarizer.html')

@app.route("/summarize",methods=["POST"])
def summarize():
    output = request.form['output']
    output = re.sub(r'[^a-zA-Z.,]'," ",output)
    print(output)

    essay = check(output) #    API call
    #with open('sample1.json') as json_file:      #Test using sample json
      #  essay = json.load(json_file)

    data_file = open('data_file.csv','w')
    csv_writer = csv.writer(data_file)
    count = 0
    for emp in essay:
        print(essay[emp])
        essay[emp] = round(essay[emp],4)
        if count == 0:
            header = ["Type","Probability"]
            csv_writer.writerow(header)
            count += 1
        d = [emp,essay[emp]]
        print(d)
        csv_writer.writerow(d)
    data_file.close()
    df = pd.read_csv('data_file.csv')
    temp = df.to_dict('records')
    #print(temp)
    colname = df.columns.values
    return render_template('summary.html',records = temp,colnames = colname)

#port = os.getenv('VCAP_APP_PORT','8080')
if __name__=="__main__":
    #app.secret_key = os.urandom(12)
    #app.run(debug=True, host='0.0.0.0', port=port)
    app.run(debug=True)


