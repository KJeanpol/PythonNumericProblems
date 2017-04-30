#---------------------------------------------------FUNCIONES IMPORTANTES---------------------------------------------------


#Entrada: un numero entero 
#Salida: la catidad de digitos presentes en el parametro de entrada
def cantidadDigitos(num):
    cantidad=0
    while (num>0):
        num=num//10
        cantidad=cantidad+1
    return cantidad

#Entrada: primer parametro es un numero entero, el segundo parametro es un numero entero positivo el cual indica la posicion a buscar
#Salida: el digito segun la posicion consultada, siendo 1 el primer digito de derecha a izquierda
def obtenerNumPos(num,pos):
    resultado=0
    while(pos>0):
        resultado=num%10
        num=num//10
        pos=pos-1
    return resultado

#---------------------------------------------------PRIMER PROBLEMA---------------------------------------------------

#Entrada: un numero entero 
#Salida: la catidad de numeros primos que existen en un rango [2,numero entero dado]
def encontrarCantidadPrimos(num):
    contador=2
    cantidad=0
    while(contador<num):
        if (esPrimo(contador)):
            cantidad+=1
        contador+=1
    return cantidad

#Entrada: el primer parametro es un numero entero positivo, el segundo parametro es un numero entero positivo que indica cual numero primo quiere
#Salida: un numero primo menor o igual al primer parametro segun sea la posicion dada
def encontrarXPrimo(num,pos):
    contador=2
    cantidad=1
    while(contador<num):
        if (esPrimo(contador)):
            if (cantidad==pos):
                return contador
            cantidad+=1
        contador+=1
    return "No existen Primos"
    
#Entrada: un numero entero 
#Salida: retorna True si el numero es Primo, o False si no lo es    
def esPrimo(num):
    contador=2
    if num<2:
        return False
    while (contador<num):
        if (num%contador==0):
            return False
        contador+=1
    return  True

#Entrada: un numero entero 
#Salida: imprime en consola el numero dado, y los numero primos cuya multiplicacion da como resultado el numero de entrada
def buscarSemiPrimo(num):
    cantidad=encontrarCantidadPrimos(num)
    var1=0
    var2=0
    for z in range (1, cantidad+1):
        var1=encontrarXPrimo(num,z)
        for y in range (z+1,cantidad+1):
            var2=encontrarXPrimo(num,y)
            if (var1*var2==num):
                print(str(num) + "              |             "+ str(var1)  + " x "  +str(var2))
                return
    return False

#Entrada: un numero entero 
#Salida: retorna True si existen semiprimos de un numero dado, o False si no existen
def buscarSemiPrimoAux(num):
    cantidad=encontrarCantidadPrimos(num)
    var1=0
    var2=0
    for z in range (1, cantidad+1):
        var1=encontrarXPrimo(num,z)
        for y in range (z+1,cantidad+1):
            var2=encontrarXPrimo(num,y)
            if (var1*var2==num):
                return True
    return False

#Entrada: el primer y segundo parametros son numeros enteros positivos, cuyo segundo parametro debe ser mayor que el primero 
#Salida: retorna True si existen semiprimos en un intervalo dado, o False si no existen
def existeSemiPrimos(num1,num2):
    bandera=False
    while(num1<=num2):
        if (buscarSemiPrimoAux(num1)):
            return True
        num1=num1+1
    return bandera
        

#Entrada: el primer y segundo parametros son numeros enteros positivos, cuyo segundo parametro debe ser mayor que el primero 
#Salida: imprime en consola los numeros semiprimos en un intervalo dado, y los  primos cuya multiplicacion da como resultado el semiprimo   
def semiprimos(num1,num2):
    print("SemiPrimos-----------------Primos que lo conforman")
    bandera=existeSemiPrimos(num1,num2)
    if (bandera==False):
        print ("NO EXISTEN SEMIPRIMOS EN ESTE RANGO")
        return 
    else:         
        while(num1<=num2):
            buscarSemiPrimo(num1)
            num1=num1+1
    return
  
#---------------------------------------------------  SEGUNDO PROBLEMA---------------------------------------------------

#Entrada: el primer y segundo parametro son  numeros enteros positivos,el primero es el numero a buscar dentro del segundo parametro 
#Salida: retorna la cantidad de veces que el primer parametro aparece en el segundo parametro dado
def apariciones(num,num2):
    pos=0
    digNum=cantidadDigitos(num)
    digNum2=cantidadDigitos(num2)
    digNum3=digNum2
    resultado=0
    bandera=0
    while(digNum2>0):  
        var2=obtenerNumPos(num2,digNum2)   #Primer digito de derecha a izquierda del num2
        var1=obtenerNumPos(num,digNum)     #Primer digito de derecha a izquierda del num1
        if (var1==var2):                   #Si son iguales, obtiene un nuevo numero con la misma cantidad de digitos que el num1, y verifica si son iguales
            var3=obtenerNuevoNum(num2,digNum)
            if (var3==num):
                resultado=resultado+1
                num2=num2-(var3*pow(10,digNum2-digNum))  #Como son iguales, ya no se evaluan más entonces se eliminan del num2
                digNum2=digNum2-digNum
                continue                    #Sirve para continuar con la siguiente iteracion     
        num2=num2-(obtenerNumPos(num2,digNum2))*pow(10,digNum2-1)
        digNum2=digNum2-1
    return resultado
                

#Entrada: el primer y segundo parametro son  numeros enteros positivos, el primero es un numero dado, y el segundo es la posicion del numero los numero a eliminar 
#Salida: retorna un numero eliminando todos los numeros a la izquierda de la posicion dada, siendo 1 el primer digito de izquierda a derecha del primer parametro
def obtenerNuevoNum(num,cantidad):
    digNum=cantidadDigitos(num)-cantidad
    while (digNum>0):
        num=num//10
        digNum=digNum-1
    return num

#---------------------------------------------------  TERCER PROBLEMA---------------------------------------------------

#Entrada: el primer y segundo parametro son  numeros enteros positivos,el segundo es el numero a buscar dentro del primer parametro 
#Salida: retorna True si esta presente el num2 en el primer pamatero, False en el caso contrario
def verificaRepetido(num,num2):
    while(num>0):
        if (num%10 ==num2):
            return True
        num=num//10
    return False
#Entrada: un numero entero positivo
#Salida: devuelve la cantidad de veces que un 0 aparece en un numero dado
def contarCeros(num):
    resultado=0
    while(num>0):
        if (num%10 ==0):
            resultado=resultado+1
        num=num//10
    return resultado

#Entrada: un numero entero positivo
#Salida: devuelve un numero conl os mismo digitos pero agrupados segun el orden de izquierda a derecha
def agrupar(num):
    exponente= cantidadDigitos(num)
    exponente2=cantidadDigitos(num)
    cantDigitos=cantidadDigitos(num)
    numBandera=num
    var1=0
    var2=0
    resultado=0
    condicion=True
    while (cantDigitos>0):
        var1=obtenerNumPos(num,exponente)  #Primer digito de izquierda a derecha
        expoBandera=exponente-1           
        if (verificaRepetido(resultado,var1)):  #Verifica si se repite el numero en el resultado
            if (var1==0):                       #Si se repite y es un 0 , le resta al exponente2 la cantidad de ceros que hay en el numero
                if(condicion):                  #Si aparece otro cero más adelante no lo toma en cuenta puesto que ya se evaluaron todos
                    exponente2=exponente2-contarCeros(num)
                    condicion=False
            cantDigitos=cantDigitos-1
            exponente=exponente-1
            continue    
            
        else:
            resultado=resultado+var1*pow(10,exponente2-1)   #Si es la primera aparicion, lo suma al resultado dado         
            while (expoBandera>0):                          #Aqui verifica si se repite de nuevo el numero más adelante
                var2=obtenerNumPos(num,expoBandera)
                if (var1==var2):
                    resultado=resultado+var2*pow(10,exponente2-2) #Si se repite, se agrega el digito al inicio
                    exponente2=exponente2-1
                expoBandera=expoBandera-1 
            cantDigitos=cantDigitos-1
            exponente=exponente-1
            exponente2=exponente2-1
    return resultado
            
#---------------------------------------------------  CUARTO PROBLEMA---------------------------------------------------




#Entrada: un numero entero positivo
#Salida: devuelve los divisores maximos del parametro dado, separados por un 0
  
def secuencia_factores_primos(num):
    indice=2
    final=0
    exponente=0
    while (num>=indice):
        if ((num%indice)==0):
            final=  final +indice * pow(10,exponente)
            num=num//indice
            exponente=exponente+2
            indice=1
        indice=indice+1
    return final

    
#---------------------------------------------------  QUINTO PROBLEMA---------------------------------------------------

#Calcular la varianza de una muestra, Probabilidad y Estadistica

#Entrada: una lista con los valores de las muestras obtenidas
#Salida: la suma total de las muestras
def muestra_sum(muestras):
    total = 0
    for muestra in muestras: 
        total += muestra
    return total

#Entrada: una lista con los valores de las muestras obtenidas
#Salida: el valor promedio de las muestras  
def promedio(muestra):
    sumaTotal = muestra_sum(muestra)
    valorPromedio = float(sumaTotal) / len(muestra)
    return valorPromedio

# Para calcular la varianza restamos a cada muestra el promedio y se suman, luego se eleva al cuadrado y se dividi entre 2
#Entrada: una lista con los valores de las muestras obtenidas 
#Salida: la varianza obtenida de las muestras tomadas
def varianza(muestras):
    Promedio=promedio(muestras)
    sumatoria = 0
    for prueba in muestras:
        sumatoria += (Promedio - float(prueba))**2
    varianzaTotal = float(sumatoria)/len(muestras)
    return varianzaTotal


#///////////////////////////////////////////     EJEMPLOS DE FUNCIONAMIENTO    //////////////////////////////////////////

#Para el problema 1:
print("Ejemplo Problema 1")
semiprimos(14,22)
semiprimos(17,20)

#Para el problema 2:
print("Ejemplo Problema 2")
print (apariciones(25,8251052552))
print(apariciones(444,4444124446444444))
print(apariciones(12345,123))


#Para el problema 3:

print("Ejemplo Problema 3")
print(agrupar(20845224809))
print(agrupar(213323))

#Para el problema 4:
print("Ejemplo Problema 4")
print(secuencia_factores_primos(120))
print(secuencia_factores_primos(33))
print(secuencia_factores_primos(11))

#Para el problema 5:
print("Ejemplo Problema 5")
muestras = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5] 
print (varianza(muestras))

        
