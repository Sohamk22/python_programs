#employee_salary

name = input("Please enter the employee's name: ").strip().title()
hourly_wage = input("What is their hourly wage? ")
hours_worked = int(input("How many hours have they worked this week? "))

earnings = float(hourly_wage) * float(hours_worked)

print(f"{name} earned {earnings:.2f} rupees this week")

print("Overtime Status:")

if hours_worked > 40:
        print(f"{name} has worked overtime this week.")
else:
        print(f"{name} has not worked overtime this week.")


