import sys

tax_start_point = 5000
social_insurance_rate = 0.08 + 0.02 + 0.005 + 0 + 0 + 0.06
tax_lookup_table = [
    (80000, 0.40, 15160),
    (55000, 0.35, 7160),
    (35000, 0.30, 4410),
    (25000, 0.25, 2660),
    (12000, 0.20, 1410),
    (3000, 0.10, 210),
    (0, 0.03, 0)
]

def income_calculator(income):
    social_insurance_fee = income * social_insurance_rate
    real_income = income - social_insurance_fee
    taxable_part = real_income - tax_start_point
    if taxable_part <= 0:
        tax = 0
    else:
        for item in tax_lookup_table:
            start_point, tax_rate, quick_subtractor = item
            if taxable_part > start_point:
                tax = taxable_part * tax_rate - quick_subtractor
    return '{:.2f}'.format(real_income - tax)

def main():
#    income_dict = {}
    if len(sys.argv) < 2:
        print('Perameter Error')
        exit(-1)
    for arg in sys.argv[1:]:
        try:
            employee_id, income_string = arg.split(':')
            income = int(income_string)
        except ValueError:
            print('Parameter Error')
            exit(-1)
        remain_income = income_calculator(income)
#    income_dict[employee_id] = remain_income
        print('{}:{}'.format(employee_id, remain_income))

if __name__ == '__main__':
    main()
