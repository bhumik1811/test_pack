from test_package import emp_info as info, emp_salary_calculation as empcal

info.emp_name("ananya","trivedi")
info.emp_department("Acounts","jr. Accountant")
netsalary=empcal.calculation_salary(10000)
print("Net salary",netsalary)
print("Petrol Allowance",empcal.calculation_petrolallowance(200))
print("commission", empcal.calculation_commission("jr. accountant", netsalary))
