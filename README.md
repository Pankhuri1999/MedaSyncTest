# MedaSyncTest

So, this code is an implementation of one of the coding tests given by MedaSync LL) 

1) Firstly, it starts with importing necesary libraries ( line 1 - line 3)
2) Then it reads the contents of the input the way it is (line 9). And stores it in the contents variables.
3) Then it separates all the lines and stores it in a array. Every line is a separate element in the arra.y (line 13)
4) Then the code checks for names of unique patients in the lines and stores their names in a separate list (line 16 - line 20)
5) The code then iterates over each of the element in patients list and the it iterates over each of the lines in the lines array.  While iterating it checks for the number of treatements, discharge and intake dates.
6) For number of treatments, it counts the total number of statements and subtracts three from it ( 3 because one line contains the patient name, second one contains the        discharge date and third contains intake date).
7)It then divides each of the sentences into separate words and takes the last word (because the last word contains the date-time).Then it parses the discharge date and intake date separately. The parsed date is then converted into timestamp.
8) Finally, it calculates the difference in between two dates in hours and minutes
9) Lastly, the statment is printed with number of treatements and time difference.

