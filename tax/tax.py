import sys


def calc_tax(salary_without_deduction):
    if salary_without_deduction <=0:
        tax=0
    elif salary_without_deduction <= 36000:
        tax = salary_without_deduction * 0.03
    elif salary_without_deduction <= 144000:
        tax = salary_without_deduction * 0.1 - 2520
    elif salary_without_deduction <= 300000:
        tax = salary_without_deduction * 0.2 - 16920
    elif salary_without_deduction <= 420000:
        tax = salary_without_deduction * 0.25 - 31920
    elif salary_without_deduction <= 660000:
        tax = salary_without_deduction * 0.3 - 52920
    elif salary_without_deduction <= 960000:
        tax = salary_without_deduction * 0.35 - 85920
    else:
        tax = salary_without_deduction * 0.45 - 181920

    return tax

if __name__ == "__main__":
    salary = int(input("请输入月工资："))
    social_security = int(input("请输入社保基数："))
    social_security = social_security * 0.103
    housing_fund = int(input("请输入公积金基数："))
    housing_fund = housing_fund * 0.12
    deductioin = int(input("请输入月度专项扣除金额："))
    annual_bonus = int(input("请输入年终奖系数："))
    annual_bonus = annual_bonus * salary

    sum_of_salary = 0
    sum_of_deduction = 0
    sum_of_money_got = 0
    sum_of_tax = 0
    print("月份\t当月交税\t当月实发\\累计工资")

    # calculate tax for salary of every month
    for i in range(12):
        sum_of_salary += salary
        sum_of_deduction += social_security + housing_fund + deductioin + 5000  # 5000 for base salary no need to pay tax each month
        salary_without_deduction = sum_of_salary - sum_of_deduction
        
        tax = calc_tax(salary_without_deduction)
        
        tax = tax - sum_of_tax
        sum_of_tax += tax
        salary_got = salary - tax - social_security - housing_fund
        sum_of_money_got += salary_got
        
        print("{0}月：\t".format(i+1),end="")
        print('{0}\t\t{1}/{2}/{3}'.format(round(tax), round(salary_got), round(2*housing_fund), round(sum_of_money_got)))

    # calculate tax for annual_bonus
    tax_for_bonus = calc_tax(salary_without_deduction + annual_bonus) - sum_of_tax
    bonus_could_get = annual_bonus - tax_for_bonus
    print("年终奖：{0}\t\t{1}".format(round(tax_for_bonus), round(bonus_could_get)))
    print("=================================================")
    print('月工资: {0}'.format(round(sum_of_money_got/12)))
    print('月工资+公积金: {0}'.format(housing_fund * 2 + round(sum_of_money_got/12)))
    print('年工资: {0}'.format(sum_of_money_got + housing_fund*2*12 + bonus_could_get))
    print('年缴税: {0}'.format(tax_for_bonus + sum_of_tax))

    input("press any key to exit...")
