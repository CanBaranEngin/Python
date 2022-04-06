def QuestionsMarks(strParam):
  question_marks_count=0
  int_count=0
  for string in list(strParam):
    if string == '?':
      question_marks_count+=1
    elif string.isdigit():
      int_count+=1
      question_marks_count=0 
    if question_marks_count==3:
      break        
  if question_marks_count==3 and int_count!=0:
    return("true")
  else:
    return("false")

  

# keep this function call here 
print(QuestionsMarks(input()))