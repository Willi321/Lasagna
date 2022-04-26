def main():
    print("Personenerkennung: ")
def einGaben():
    userdata_vname = input("Vorname: ")
    userdata_nname = input("Nachname: ")
    userdata_bdate = input("Geburtstag: YYYY/MM/DD")
    if userdata_vname != "" and userdata_nname != "" and userdata_bdate != "": 
        object_vname = userdata_vname 
        object_nname = userdata_nname
        object_bdate = userdata_bdate
        personenliste.append(object_vname)
        personenliste.append(object_nname)
        personenliste.append(object_bdate)
        print(personenliste)
    
    else: 2
    print("fehler")
    einGaben()



if __name__ == "__main__":
    main() 

    personenliste= list()
    userinput = ''
    while userinput != "x":
        userinput = input("Wollen sie suchen 1, eingeben 2, ausgeben 3, beenden x: ")
        if userinput == "1": 
            print("1")

        elif userinput == "2":
            print("2")
            einGaben()
        elif userinput == "3":
            print("3")
        else: 
            print("falsche angaben !")