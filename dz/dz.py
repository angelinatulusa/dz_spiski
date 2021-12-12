pervii=list(input("vvedite sto-to: "))
print(pervii)
while True:
    print("1-dobavit bukvu v spisok")
    print("2-soedenit dva spiska")
    print("3-dobavit bukvu na vibrannuu pozitiu")
    print("4-udalit element")
    print("5-Начинаются ли слова в строке с заглавной буквы(сломался, не работает :[ )")#этот вариант сломался и я не знаю как это починить и кажется я все только испортила
    print("6-Обращение по индексу ")
    print("7-slozenie strok")
    print("8-Извлечение среза")
    print("9-Повторение строки")
    print("10-(нету, не работает)")#не сделан
    print("11-oчистить список")
    try:
        v=int(input("vvedite cislo: "))
        if v==1:
            a=input("vvedite bukvu ")#которую хотят добавить
            pervii.append(a)
            print(pervii)
            print()
        elif v==2:
            a=input("vvedite sto hotite prisoedenit ")
            pervii.extend(a)#пользователь вводит что-то и потом это добавляется к списку
            print(pervii)
            print()
        elif v==3:
            a=input("vvedi bukvu ")
            i=int(input("vvedi pozitiu "))#человек вводит букву(которую хочет добавить) и место куда эту букву поставить в списке
            pervii.insert(i-1,a)#сперва позиция, потом буква. позиция по умолчанию начинает счет с 0
            print(pervii)
            print()
        elif v==4:
            a=input("vvedite bukvu ")#которую хотят удалитью удаляет только первое необходимое значение
            k=pervii.count(a)#чтобы удалить все значения, которые выбрал пользователь сперва узнаем их количество "k"
            print(k)
            print()
            if k>0:
                for i in range(k):
                    pervii.remove(a)#повторяет до тех пор пока k не будет равно 0
            else: 
                print("takogo elementa netu")
            print(pervii)
            print()
        elif v==5:
            if pervii.istitle()==False:
                print("nacinautsa s bolsoi")
            else:
                print("nacinautsa s malenkoi")
                print()
        elif v==6:
            try:
                a=int(input("kakoi element po indeksu vpisat? "))
                i=len(pervii)
                if a>i:
                   print("takogo indeksa v spiske netu")
                   print()
                else:
                    print(pervii[a])
                    print()
            except:
                ValueError
        elif v==7:
            pervii1=list(input("vvedite sto-to sto hotite slozit: "))
            print(pervii+pervii1)#по сути тоже самое что и было под цифрой 2, но сделано чуть по-другому
            print()
        elif v==8:
            while True:
                try:
                    i=int(input("vvedite nacalo sreza "))
                    j=int(input("vvedite konec sreza "))
                    a=len(pervii)
                    if i>a:
                        print("sto-to ne tak")
                    elif i<0:
                        print("sto-to ne tak")
                    elif j>a:
                        print("sto-to ne tak")
                    elif j<0:
                        print("sto-to ne tak")
                    print(pervii[i:j])
                    print()
                    break
                except:
                    ValueError
            print
        elif v==9:
            while True:
                try:
                    a=int(input("skolko raz povtorit stroku? "))
                    pervii*=a
                    print(pervii)
                    print()
                except:
                    ValueError
                break
        elif v==11:
            pervii.clear()
            print(pervii)
            while True:
                try:
                    a=int(input("hotite sozdat novii spisok?(1-da, 2-net) "))
                    if a==1:
                        pervii=list(input("vvedite sto-to: "))
                        print()
                    elif a==2:
                        print("horoso, togda zakoncim")
                        break
                except:
                    ValueError
                    print("sto-to ne tak")
                    print()
    except:
        ValueError
        print("takogo varianta netu")
        print()