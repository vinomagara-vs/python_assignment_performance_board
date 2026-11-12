import performance
import bonus
import appraisal_print

Emp_name= input("Enter the Employee Name")
Emp_salary =int(input("Enter the Salary"))
Performance_score=int(input("Enter the score"))

Feedback=performance.performance_cal(Performance_score)

Bonus=bonus.bonus_cal(Emp_salary,Feedback)

#Revised_salary=Emp_salary+Bonus
total_salary= lambda a, b: a + b
Revised_salary=total_salary(Emp_salary,Bonus)


appraisal_print.print_details(Emp_name,Emp_salary,Feedback,Bonus,Revised_salary)