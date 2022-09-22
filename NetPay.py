import EmployeeClass as emp
import PayrollDeductionsClass as pd


jimmys_record = emp.Employee("Jimmy Smith", 58475, "IT", "Developer", 6800.00)

transaction_1 = pd.PayrollDeductions("food court", "8/14/2022", 22.50, 39119)
transaction_2 = pd.PayrollDeductions("gift contribution", "8/12/2022", 25.00, 58475)
transaction_3 = pd.PayrollDeductions("food court", "8/17/2022", 15.25, 21547)
transaction_4 = pd.PayrollDeductions("vending machine", "8/22/2022", 3.00, 58475)
transaction_5 = pd.PayrollDeductions("vending machine", "8/5/2022", 2.75, 58475)

transactions = [transaction_1, transaction_2, transaction_3, transaction_4, transaction_5]

jimmys_bill_total = 0

for transaction in transactions:
    if transaction.get_employee_ID() == jimmys_record.get_ID_number():
        jimmys_bill_total += transaction.get_charge()


print(
    f'''** Employee Pay **
Name: {jimmys_record.get_name()}
ID Number: {jimmys_record.get_ID_number()}
Department: {jimmys_record.get_department()}
Gross Pay: ${jimmys_record.get_monthly_salary()}
Net Pay ${float(jimmys_record.get_monthly_salary() - jimmys_bill_total)}''')
