

def performance_cal(score):
  if(score>=90):
    performance="Excellent"
  elif(score>=75 and score<90):
    performance="Good"
  elif(score>=50 and score<75):
    performance="Average"
  else:
    performance="Needs Improvement"

  return performance