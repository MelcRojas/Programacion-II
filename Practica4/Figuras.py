import math
# Círculo
def area(figura, **kwargs):
    if figura == "círculo":
        radio = kwargs.get('radio', 0)
        return math.pi * radio**2
    
    #Rectángulo
    elif figura == "rectángulo":
        largo = kwargs.get('largo', 0)
        ancho = kwargs.get('ancho', 0)
        return largo * ancho
    
    #Triángulo Rectángulo
    elif figura == "triángulo rectángulo":
        base = kwargs.get('base', 0)
        altura = kwargs.get('altura', 0)
        return (base * altura) / 2
    
    #Trapecio
    elif figura == "trapecio":
        base_mayor = kwargs.get('base_mayor', 0)
        base_menor = kwargs.get('base_menor', 0)
        altura = kwargs.get('altura', 0)
        return ((base_mayor + base_menor) * altura) / 2
    
    #Pentágono
    elif figura == "pentágono":
        apotema = kwargs.get('apotema', 0)
        lado = kwargs.get('lado', 0)
        return (5 * lado * apotema) / 2
    
    else:
        return "Figura desconocida"

print("Área del círculo:", area("círculo", radio=5))
print("Área del rectángulo:", area("rectángulo", largo=4, ancho=6))
print("Área del triángulo rectángulo:", area("triángulo rectángulo", base=3, altura=4))
print("Área del trapecio:", area("trapecio", base_mayor=8, base_menor=5, altura=3))
print("Área del pentágono:", area("pentágono", apotema=4, lado=6))
