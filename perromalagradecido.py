x=1
cantCumplen = 0
sumaAptas =0 
cantPiezas = int(input("ingresa la xantidad de piezas:"))
while x <= cantPiezas:
    longPiezas = float(input("ingresa la longitud de la pieza:"))
    if longPiezas >= 1.20 and cantPiezas <=1.30:
        cantCumplen = cantCumplen+1
        sumaAptas = sumaAptas+longPiezas
    x+=1
print(f"cantidad de piezaa leidas: {x-1}")
print(f"cantidad de piezaa leidas: {cantCumplen}")
print(f"suman longitudes aptas: {sumaAptas}")

