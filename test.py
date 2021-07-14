import json 
import csv 
  
  
# Opening JSON file and loading the data 
# into the variable data 
with open('sample.json') as json_file: 
    data = json.load(json_file) 
  

data_file = open('data_file.csv', 'w') 
  
# create the csv writer object 
csv_writer = csv.writer(data_file) 
 
count = 0
  
for emp in data: 
    print(data[emp])
    if count == 0: 
        
        # Writing headers of CSV file 
        header = ['Type','Probability']
        csv_writer.writerow(header) 
        count += 1
  
    # Writing data of CSV file 
    d = [emp,data[emp]]
    print(d)
    csv_writer.writerow(d) 
  
data_file.close() 