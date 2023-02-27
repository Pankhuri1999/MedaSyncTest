# importing necessary libraries
import sys
import zulu
from datetime import datetime

# Reding the input file
# python cat.py FilePythonRead.txt --> command used for reading input file in command prompt
# FilePythonRead.txt is the name of the etxt file to be read
with open(sys.argv[1], 'r') as f:
    contents = f.read()

# splitting lines of the file
lines = contents.splitlines()

# checking number of unique patients
patientList = []
for i in lines:
	tmpString = i.split()
	if "Patient" in tmpString:
		patientList.append(tmpString[1])

# iterating over each unique patiend like Joh,n Anne, Polly
for i in patientList:
	cnt = 0
	start = 0
	end = 0
	hour = 0
	diff = 0
	minutes = 0
	# iterating over each lines of file and checing the matching patient
	for j in lines:
		if i in j:
			# cnt  = no. of treatmennts
			cnt = cnt + 1
			# for checking the intake time 
			if "Intake" in j:
				tmpString = j.split()
				start = zulu.parse(tmpString[3])
				start = start.timestamp()
			# checking discharge time
			elif "Discharge" in j:
				tmpString = j.split()
				end = zulu.parse(tmpString[3])
				end = end.timestamp()
		# calculation to find the time difference
		diff = end - start
		hour = diff // 3600
		diff %= 3600
		minutes = diff // 60
	    
	print("Patient" , i , " stayed for" , hour , " hours and" , minutes , " minutes and received" , (cnt-3) , " treatments.")
	
    