
import sys

sa = int(input("请输入月工资："))
if sa >= 25000:
    print("妈的工资这么高？拜拜")
    sys.exit(0)

sb = int(input("请输入社保基数："))
sb = sb * 10.5 * 0.01
gjj = int(input("请输入公积金基数："))
gjj = gjj * 0.12
kou = int(input("请输入专项扣除金额："))

sumSa = 0
sumK = 0
sumGet = 0
sumTax = 0
print("月份\t当月交税\t当月实发\\累计工资")

for i in range(12):
    sumSa += sa
    sumK += sb+gjj+kou+5000
    saForTax = sumSa - sumK
    
    if saForTax <=0:
        tax=0
    elif saForTax <= 36000:
        tax = saForTax * 0.03
    elif saForTax <= 144000:
        tax = 36000*0.03 + (saForTax - 36000) * 0.1
    else:
        tax = 36000*0.03 + (144000 - 36000)*0.1 + (saForTax - 144000) * 0.2
    
    tax = tax - sumTax
    sumTax += tax
    saGet = sa - tax - sb - gjj
    sumGet += saGet
    
    print("{0}月：\t".format(i+1),end="")
    print('{0}\t\t{1}/{2}'.format(round(tax), round(saGet), round(sumGet)))

print('平均月工资: {0}'.format(round(sumGet/12)))


input("press any key to exit...")
