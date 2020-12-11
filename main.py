# -*- coding: UTF-8 -*-
__author__ = 'Alleria'
BASE_EXCEPT = 60000
BASE_INSURANCE = 25401
WAN = 10000

step_tex = {
    0: (BASE_EXCEPT, 0.00, 0),
    1: (BASE_EXCEPT+36000, 0.00, 0),
    2: (BASE_EXCEPT+144000, 0.10, 2520),
    3: (BASE_EXCEPT+300000, 0.20, 16920),
    4: (BASE_EXCEPT+420000, 0.25, 31920),
    5: (BASE_EXCEPT+660000, 0.30, 52920),
    6: (BASE_EXCEPT+960000, 0.35, 85920),
    7: (float('inf'), 45, 181920)
}

add_work = {
    0: 0,
    0.5: 24,
    1: 48
}

base = float(input("月基本工资/k：")) * 1000
month = float(input("年终奖月数：") or 0)
is_renting = int(input("是否租房(1 or 0)：") or 0)
parent = int(input("60岁以上老人数量：") or 0)
renting = int(input("月房补(可不填)：") or 0)
overtime = float(input("每周加班天数(可不填)：") or 0)
overtime_rate = float(input("加班费倍率(可不填)：") or 0)


def get_tex_by_annual_income(income):
    step_current = 0
    for step in step_tex.keys():
        if income < step_tex[step][0]:
            step_current = step
            break
    return income * step_tex[step_current][1] - step_tex[step_current][2]


def get_insurance_by_base():
    base_limited = base if base < BASE_INSURANCE else BASE_INSURANCE
    return base_limited * (0.08 + 0.02 + 0.002 + 0.12) * 12


def get_other_income():
    overtime_money = base/21.75 * overtime_rate * add_work[overtime]
    other_income = renting * 12 + overtime_money
    return other_income


def get_not_need_tex_income():
    total = 0
    if is_renting:
        total = total + 1500 * 12
    total = total + 60000
    total = total + get_insurance_by_base()
    return total


total_money = base * (12+month) + get_other_income()
not_need_tex_money = get_not_need_tex_income()
need_tex = total_money - not_need_tex_money
tex = get_tex_by_annual_income(need_tex)
housing_found = base * 0.24 * 12 if base < BASE_INSURANCE else BASE_INSURANCE * 0.24 * 12
ture_get = total_money - tex - get_insurance_by_base()

print("\n===============================\n")

print("{0:{2}<15}{1:>5}天".format("年加班天数",24,chr(12288)))
str = "{0:{2}<15}{1:>5.2f}万"
print(str.format("年总收入",total_money/WAN, chr(12288)))
print(str.format("年豁免收入",not_need_tex_money/WAN, chr(12288)))
print(str.format("年需缴个人所得税收入",need_tex/WAN, chr(12288)))
print(str.format("年个人所得税",tex/WAN, chr(12288)))
print(str.format("年实际到手",ture_get/WAN, chr(12288)))
print(str.format("年住房公积金",housing_found/WAN, chr(12288)))
print(str.format("年实际到手加住房公积金",(housing_found+ture_get)/WAN, chr(12288)))