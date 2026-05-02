annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as decimal: "))
total_cost = float(input("Enter the cost of your dream house: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25
r = 0.04

current_savings = 0
down_payment = total_cost*portion_down_payment
monthly_salary = annual_salary/12
months = 0
while(current_savings < down_payment):    
    months += 1
    current_savings += monthly_salary*portion_saved + current_savings*r/12
    if(months % 6 == 0):
        annual_salary += annual_salary*semi_annual_raise
        monthly_salary = annual_salary/12
print(f"Number of months: {months}")   