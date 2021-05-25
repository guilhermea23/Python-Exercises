def leapYear(a):
    if a%400==0 or a%4==0 and a%100!=0:
        return "Yes"
    else:
        return "No"

year = int(input())
print(leapYear(year))
