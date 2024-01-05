
import sys


def calc_tax(saForTax):
    if saForTax <=0:
        tax=0
    elif saForTax <= 36000:
        tax = saForTax * 0.03
    elif saForTax <= 144000:
        tax = saForTax * 0.1 - 2520
    elif saForTax <= 300000:
        tax = saForTax * 0.2 - 16920
    elif saForTax <= 420000:
        tax = saForTax * 0.25 - 31920
    elif saForTax <= 660000:
        tax = saForTax * 0.3 - 52920
    elif saForTax <= 960000:
        tax = saForTax * 0.35 - 85920
    else:
        tax = saForTax * 0.45 - 181920

    return tax

if __name__ == "__main__":
    sa = int(input("请输入月工资："))
    # if sa >= 25000:
    #     print("妈的工资这么高？拜拜")
    #     sys.exit(0)

    sb = int(input("请输入社保基数："))
    sb = sb * 10.5 * 0.01
    gjj = int(input("请输入公积金基数："))
    gjj = gjj * 0.12
    kou = int(input("请输入月度专项扣除金额："))
    bonus = int(input("请输入年终奖金额："))

    sumSa = 0
    sumK = 0
    sumGet = 0
    sumTax = 0
    print("月份\t当月交税\t当月实发\\累计工资")

    # calculate tax for salary of every month
    for i in range(12):
        sumSa += sa
        sumK += sb+gjj+kou+5000
        saForTax = sumSa - sumK
        
        tax = calc_tax(saForTax)
        
        tax = tax - sumTax
        sumTax += tax
        saGet = sa - tax - sb - gjj
        sumGet += saGet
        
        print("{0}月：\t".format(i+1),end="")
        print('{0}\t\t{1}/{2}'.format(round(tax), round(saGet), round(sumGet)))

    # calculate tax for bonus
    tax_for_bonus = calc_tax(saForTax + bonus) - sumTax
    bonus_could_get = bonus - tax_for_bonus
    print("年终奖：{0}\t\t{1}".format(round(tax_for_bonus), round(bonus_could_get)))
    print("=================================================")
    print('月工资: {0}'.format(round(sumGet/12)))
    print('月工资+公积金: {0}'.format(gjj*2+round(sumGet/12)))
    print('年工资: {0}'.format(sumGet+gjj*2*12+bonus_could_get))
    print('年缴税: {0}'.format(tax_for_bonus+sumTax))

    input("press any key to exit...")
