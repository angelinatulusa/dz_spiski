pervii=list(input("vvedite sto-to: "))
print(pervii)
while True:
    print("1-dobavit bukvu v spisok")
    print("2-soedenit dva spiska")
    print("3-dobavit bukvu na vibrannuu pozitiu")
    print("4-udalit element")
    v=int(input("vvedite cislo: "))
    if v==1:
        a=input("vvedite bukvu")#которую хотят добавить
        pervii.append(a)
        print(pervii)
    elif v==2:
        a=input("vvedite sto hotite prisoedenit ")
        pervii.extend(a)#пользователь вводит что-то и потом это добавляется к списку
        print(pervii)
    elif v==3:
        a=input("vvedi bukvu ")
        i=int(input("vvedi pozitiu "))#человек вводит букву(которую хочет добавить) и место куда эту букву поставить в списке
        pervii.insert(i-1,a)#сперва позиция, потом буква. позиция по умолчанию начинает счет с 0
        print(pervii)
    elif v==4:
        a=input("vvedite bukvu ")#которую хотят удалитью удаляет только первое необходимое значение
        k=pervii.count(a)#чтобы удалить все значения, которые выбрал пользователь сперва узнаем их количество "k"
        print(k)
        if k>0:
            for i in range(k):
                pervii.remove(a)#повторяет до тех пор пока k не будет равно 0
        else: 
            print("takogo elementa netu")
        print(pervii)
    else:
        print("takogo varianta netu")
