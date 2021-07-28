global gross_salary

def calculation_salary(gross_salary):
    return gross_salary - (gross_salary * 0.10)


def calculation_petrolallowance(kmride):
    return kmride * 2


def calculation_commission(grade,salary):
    if grade == "salesman":

        return salary * 0.05
    elif grade =="senior salesman":
        return salary * 0.10
    elif grade =="sales manager":
        return salary * 0.15
    else:
        return 0

