name = input('Enter name of the employee: ')
id = int(input('Enter Id of the employee: '))
basic_salary = float(input('Enter monthly basic salary of the employee: '))
allowances = float(input('Enter special allowances of the employee: '))
bonus = float(input('Enter bonus percentage: '))

gross_monthly_salary = basic_salary + allowances 
gross_annual_salary  = (gross_monthly_salary * 12) + (bonus / 100) * (12 * gross_monthly_salary)

print('%-4s %-12s %-14s %-12s %-9s %-14s %-s'%("ID", "NAME", "BASIC-SALARY", "ALLOWANCES","BONUS(%)", "MONTHLY-SALARY", "ANNUAL-SALARY"))
print('-' * 85)
print('%-4d %-12s %-14.2f %-12.2f %-9.2f %-14.2f %-.2f'%(id, name, basic_salary, allowances, bonus, gross_monthly_salary, gross_annual_salary))

std_deduction  = 50000
taxable_salary = gross_annual_salary - std_deduction
print(f'Standard Deduction = {std_deduction}')
print(f'Taxable Salary = {taxable_salary}')

