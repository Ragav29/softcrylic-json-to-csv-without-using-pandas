import json
import csv

with open("studentsperformance.json") as json_file:
	data=json.load(json_file)#fetching the data in json file into dataframe(data)
csv_file = open('output.csv', 'w', newline='') 
csv_writer = csv.writer(csv_file)
header = data.keys()
genderValues=data["gender"]
raceValues=data["race/ethnicity"]
pntEduValues=data["parental level of education"]
lunchValues=data["lunch"]
testValues=data["test preparation course"]
mathValues=data["math score"]
readingValues=data["reading score"]
writingValues=data["writing score"]

totalCount=len(genderValues)
count=0
csv_writer.writerow(header)
while(count<totalCount):
	value=[genderValues[str(count)],raceValues[str(count)],pntEduValues[str(count)],lunchValues[str(count)],testValues[str(count)],mathValues[str(count)],readingValues[str(count)],writingValues[str(count)]]
	csv_writer.writerow(value)
	count += 1
csv_file.close()