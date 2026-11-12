

def bonus_cal(salary,level):
  if(level=="Excellent"):
    Bonus=0.20*salary
  elif(level=="Good"):
    Bonus=0.10*salary
  elif(level=="Average"):
    Bonus=0.05*salary
  else:
    Bonus=0
    print("No Bonus")

  return Bonus