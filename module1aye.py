def goroda(d:dict, v:int):
    keys_list=(list(d.keys()))
    values_list=(list(d.values()))
    if v=="uznatstolicy":
        mas=[]
        capital=(input("Введи столицу: "))
        capital.title()
        for i in values_list:
            if i==capital:
                for i in range(len(values_list)):
                    if values_list[i]==capital:
                        mas.append(int(i))
                        print("Страна -", keys_list[i],"<-->", "Cтолица -", values_list[i])
    else:
        country==(input("Введите страну: ")).capitalize()
        a=d.get(country)
        print("Страна -", country ,"<-->", "Cтолица -", a)
    return

def addstrana(d:dict, v:int):
    if v=="add":
        new={}
        country=(input("Введите страну: ")).capitalize()
        capital=(input("Введите страну: ")).capitalize()
        new={country:capital}

    return d,new

def changestrana(d:dict, v:int):
    keys_list=(list(d.keys()))
    values_list=(list(d.values()))
    if v=="changestrana":
        a=str(input("Введите название страны которую хотите изменить"))
        del dictionary[a]
        b=str(input(a))
        c=str(input("Также измените столицу"))
        strany={a: c}
    return a,c,b
