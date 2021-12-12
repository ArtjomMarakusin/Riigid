from random import *
Capitals=dict()
Countries=["Estonia","Latvia","Albania","Belgium","Czechia","Poland","Portugal","Finland","France","Lithuania","Germany","Sweden","Spain","Serbia","Norway","Moldova","Greece","Bulgaria","Austria","Switzerland"]
Capitals["Estonia"]="Tallinn"
Capitals["Latvia"]="Riga"
Capitals["Albania"]="Tirana"
Capitals["Belgium"]="Brussels"
Capitals["Czechia"]="Prague"
Capitals["Poland"]="Warsaw"
Capitals["Portugal"]="Lisbon"
Capitals["Finland"]="Helsinki"
Capitals["France"]="Paris"
Capitals["Lithuania"]="Vilnus"
Capitals["Germany"]="Berlin"
Capitals["Sweden"]="Stockholm"
Capitals["Spain"]="Madrid"
Capitals["Serbia"]="Belgrade"
Capitals["Norway"]="Oslo"
Capitals["Moldova"]="Chisinau"
Capitals["Greece"]="Athens"
Capitals["Bulgaria"]="Sofia"
Capitals["Austria"]="Vienna"
Capitals["Switzerland"]="Bern"
for country in Countries:
    country=input("Введите страну: ")
    if country in Capitals:
        print("Столица страны "+country+": " +Capitals[country])
    else:
        print("В базе данных нет страны с названием " +country)
        v=input("Хотите внести " +country+ " в базу данных? Да(+) или Нет?(-) ")
        if v=="+":
            ca=input("Введите столицу страны " +country+": ")
            Capitals.update({country: ca})
            g=input("Возможно в базе данных ошибка, хотите исправить её? Да(+) или Нет?(-) ")
            if g=="-":
                print("Хорошо")
            if g=="+":
                o=input("Введите правильно страну:")
                l=input("Введите правильно столицу:")
                Capitals.pop(country)
                Capitals.update({o: l})

        if v=="-":
            print("Хорошо")
    p=input("Хотите ли пройти тест на знания столиц Европы? Да(+) или Нет?(-) ")
    if p=="+":
        Countries.sort()
        Countries.reverse()
        a=0
        for i in range(10):
            country=str(choice(Countries))
            print(country)
            zp=input("Введите столицу:")
            if zp==Capitals[country]:
                print("Правильно!")
                a+=1
            else:
                print("Неправильно!")
        if a==0:
            print("0%")
        elif a==1:
            print("10%")
        elif a==2:
            print("20%")
        elif a==3:
            print("30%")
        elif a==4:
            print("40%")
        elif a==5:
            print("50%")
        elif a==6:
            print("60%")
        elif a==7:
            print("70%")
        elif a==8:
            print("80%")
        elif a==9:
            print("90%")
        elif a==10:
            print("100%")
    if p=="-":
        print("Всего доброго!")