import random
gFuel = ["Grape \n","Peach Mango \n","Kiwi Strawebrry \n","Frut Chug Rug \n","Watermelon \n","Battle Juice \n"]

ult = open("text.txt", "r+")

def CuantosRicosGFuels():
    return len(gFuel)



def leerFichero(ult):
    ricosGFuels = ult.readlines()
    
    if len(ricosGFuels) == 0:
        ult.write(gFuel[random.randint(0,CuantosRicosGFuels()-1)] )
        ult.write(gFuel[random.randint(0,CuantosRicosGFuels()-1)])
        ult.write("0\n")
        ult.truncate()
        ricosGFuels = ult.readlines()
    
    a = gFuel[random.randint(0,CuantosRicosGFuels()-1)]   
    
    while ricosGFuels[0] == a or ricosGFuels[1] == a:
        a = gFuel[random.randint(0,CuantosRicosGFuels()-1)]
    
        
    print(a)
    
    pos = int(ricosGFuels[2])
    posInsertion = abs(pos-1)
    print(posInsertion)
    ricosGFuels[posInsertion] = a
    ricosGFuels[2] = str(posInsertion)
    print(ricosGFuels)
    ult.close()
    ult = open("text.txt", "w")
    #for i in range(len(ricosGFuels)):
    ult.writelines(ricosGFuels) 
    ult.truncate()
    ult.close()
            
            
            
            

leerFichero(ult)

