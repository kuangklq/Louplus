#!usr/bin/env python3

import sys

tax_start_point = 5000
social_insurance_rate = 0.08 + 0.02 + 0.005 + 0.06
tax_lookup_table = [
        (80000, 0.45, 15160),
        (55000, 0.35, 7160),
        (35000, 0.3, 4410),
        (25000, 0.25, 2660),
        (12000, 0.2, 1410),
        (3000, 0.1, 210),
        (0, 0.03, 0)
]

def handle_data(input_str):
    try:
        id_str, income_str = input_str.split(':')
        id_ = int(id_str)
        income_ = int(income_str)
    except ValueError:
        print('Parameter Error')
        exit()
    return id_, income_

def income_calculator(income_before_tax):
    social_insurance_fee = income_before_tax * social_insurance_rate
    taxable_part = income_before_tax - social_insurance_fee - tax_start_point    
    for tuple_ in tax_lookup_table:
        start_point, tax_rate, quick_sub = tuple_
        if taxable_part > start_point:
            tax = taxable_part * tax_rate - quick_sub
            break
        elif taxable_part <= 0:
            tax = 0
            break
    remain_income = income_before_tax - social_insurance_fee - tax
    return remain_income
#    return tax, remain_income

def main():
    if len(sys.argv) < 2:
        print('Parameter Error')
        exit()
    for arg in sys.argv[1:]:
        employee_id, income = handle_data(arg)
        print('{}:{:.2f}'.format(employee_id, income_calculator(income)))
#        _, remain_income = income_calculator(income)
#        print('{}:{:.2f}'.format(employee_id, remain_income))

if __name__ == '__main__':
    main()
