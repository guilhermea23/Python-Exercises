def age(idade):
    years_alive = 0
    month_alive = 0
    days_alive = 0

    if idade < 30:
        days_alive = idade
    elif idade >= 30:
        month_alive = idade // 30
        days_alive = idade - 30 * month_alive
        if idade < 360:
            years_alive = (idade // 30) // 12

        elif idade >=360:
            years_alive = (idade // 30)//12
            idade = idade - years_alive*360
            month_alive = (idade//30)
            days_alive = idade- 30*month_alive

    return print(years_alive, month_alive, days_alive)


d1, d2, d3 = map(int, input().split())
age(d1)
age(d2)
age(d3)
