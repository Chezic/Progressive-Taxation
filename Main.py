status=input("Какой у вас статус? ")
taxfree=int(input("Какая сумма не облагается налогом? "))
tax=0
a=[]
b=["январе","феврале","марте","апреле","мае","июне","июле","августе","сентябре","октябре","ноябре","декабре"]
for i in range (0,12):
    a.append(int(input("Сколько вы заработали в "+b[i]+"? ")))
if status=="родитель-одиночка":
    if 0<=revenue<=12950:
        tax = 0.1 * revenue
    elif 12951<=revenue<=49400:
        tax = 0.15 * revenue
    elif 49401<=revenue<=127550:
        tax = 0.25 * revenue
    elif 127551<=revenue<=206600:
        tax = 0.28 * revenue
    elif 206601<=revenue<=405100:
        tax = 0.33 * revenue
    elif 405101<=revenue<=432200:
        tax = 0.35 * revenue
    elif 432201<=revenue:
        tax = 0.396 * revenue
        


for i in range (0,12):
   
    if status=="один субъект":
        if 0<=a[i]-taxfree<=9075:
            tax=tax+(a[i]-taxfree)*0.1
        elif 9076<=a[i]-taxfree<=36900:
            tax=tax+(a[i]-9076-taxfree)*0.15
            tax=tax+(9075)*0.1
        elif 36901 <= a[i]-taxfree <= 89350:
            tax += 0.25 * (a[i]-taxfree-36901)
            tax += (36900-9076)*0.15
            tax += (9075)*0.1
        elif 89351 <= a[i]-taxfree <= 186350:
            tax += 0.28 * (a[i]-taxfree-89351)
            tax += 0.25 * (89350-36901)
            tax += (36900-9076)*0.15
            tax += (9075)*0.1
        elif 186351 <= a[i]-taxfree <= 405100:
            tax += 0.33 * (a[i]-taxfree -186351)
            tax += 0.28 * (186350-89351)
            tax += 0.25 * (89350-36901)
            tax += (36900-9076)*0.15
            tax += (9075)*0.1
        elif 405101 <= a[i]-taxfree <= 406750:
            tax += 0.35 * (a[i]-taxfree-405101)
            tax += 0.33 * (405100-186351)
            tax += 0.28 * (186350-89351)
            tax += 0.25 * (89350-36901)
            tax += (36900-9076)*0.15
            tax += (9075)*0.1
        elif 406751 <= a[i]-taxfree:
            tax += 0.396 * (a[i]-taxfree-406751)
            tax += 0.35 * (406750-405101)
            tax += 0.33 * (405100-186351)
            tax += 0.28 * (186350-89351)
            tax += 0.25 * (89350-36901)
            tax += (36900-9076)*0.15
            tax += (9075)*0.1



        
        
for i in range(0, 12):

    if status == "для супружеской пары":
        if 0 <= a[i] - taxfree <= 18150:
            tax = tax + (a[i] - taxfree) * 0.1
        elif 18151 <= a[i] - taxfree <= 73800:
            tax = tax + (a[i] - 9076 - taxfree) * 0.15
            tax = tax + (18150) * 0.1
        elif 73801 <= a[i] - taxfree <= 148850:
            tax += 0.25 * (a[i] - 73801 - taxfree)
            tax += (73800 - 18151) * 0.15
            tax += (18150) * 0.1
        elif 148851 <= a[i] - taxfree <= 226850:
            tax += 0.28 * (a[i] - 148851 - taxfree)
            tax += 0.25 * (148850 - 73801)
            tax += (73800 - 18151) * 0.15
            tax += (18150) * 0.1
        elif 226851 <= a[i] - taxfree <= 405100:
            tax += 0.33 * (a[i] - 226851 - taxfree)
            tax += 0.28 * (226850 - 148851)
            tax += 0.25 * (148850 - 73801)
            tax += (73800 - 18151) * 0.15
            tax += (18150) * 0.1
        elif 405101 <= a[i] - taxfree <= 457600:
            tax += 0.35 * (a[i] - 405101 - taxfree)
            tax += 0.33 * (405100 - 226851)
            tax += 0.28 * (226850 - 148851)
            tax += 0.25 * (148850 - 73801)
            tax += (73800 - 18151) * 0.15
            tax += (18150) * 0.1
        elif 457601 <= a[i] - taxfree:
            tax += 0.396 * (a[i] - 406751 - taxfree)
            tax += 0.35 * (406750 - 405101)
            tax += 0.33 * (405100 - 226851)
            tax += 0.28 * (226850 - 148851)
            tax += 0.25 * (148850 - 73801)
            tax += (73800 - 18151) * 0.15
            tax += (18150) * 0.1


print(tax)
