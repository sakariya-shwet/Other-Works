# Salary Increment

salary = int(input("Enter your salary: "))
increment_percent = int(input("Enter increment %: "))

increment_amount = (salary * increment_percent) / 100
new_salary = salary + increment_amount

print("Increment Amount:", increment_amount)
print("New Salary:", new_salary)
