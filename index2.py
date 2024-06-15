#print("hola" == "hola")

string1 = "dimas"
string2 = "suscribete"
string3 = "dimas"

if string1 == string3:
     print("Son iguales")
else:
    print("Son diferentes")
    
if string1 == string2:
     print("Son iguales")
else:
    print("Son diferentes")
    
    string1 = " hola"
    string2 = "Hola"
    
    #print("Son distintos") if string1 != string2 else print("Son iguales")
    
    if string1.strip().lower() == string2.strip().lower() == string2.strip().lower():
        print("Son iguales!")