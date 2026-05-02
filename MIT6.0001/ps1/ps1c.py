annual_salary = float(input("Enter the starting salary: "))
original_annual_salary = annual_salary

total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
r = 0.04

down_payment = total_cost*portion_down_payment

total_months = 36

bisection_steps = 0

high = 10000
low = 0
guess = (high + low) / 2

savings = 0

while(abs(savings-down_payment) >= 100): 
    annual_salary = original_annual_salary
    monthly_salary = annual_salary / 12
    savings = 0

    for i in range(total_months):
        savings += monthly_salary*(guess/10000.0) + savings*r/12
        if((i+1) % 6 == 0):
            annual_salary += annual_salary*semi_annual_raise
            monthly_salary = annual_salary/12
    
    if(savings > down_payment):
        high = guess
    else:
        low = guess
    guess = (high + low) / 2
            
    bisection_steps += 1
    if(bisection_steps > 100):
        break

if(bisection_steps > 100):
    print("It is not possible to pay the down payment in three years")
else:
    print(f"Best savings rate: {round(guess/10000.0, 4)}")
    print(f"Steps in bisection search: {bisection_steps}")
