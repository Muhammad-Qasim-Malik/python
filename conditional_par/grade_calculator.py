total_marks = 600
obtained_marks = 200
percentage = round(obtained_marks / (total_marks / 100),2) 
print(percentage)
if percentage > 100:
    print("Please Enter valid Obtained Marks.")
elif percentage >= 90:
    print("You've passed the exams with A Grade")
elif percentage >= 80:
    print("You've passed the exams with B Grade")
elif percentage >= 70:
    print("You've passed the exams with C Grade")
elif percentage >= 60:
    print("You've passed the exams with D Grade")
else:
    print("You got F Grade in your exams")
