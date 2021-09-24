import math

def primogrado():
    f = b
    g = c

    if f == 0:
        if g == 0:
            print("indeterminata")
        else:
            print("impossibile")
    else:
        x = (-g)/f
        print(x)

a = int(input("Inserisci a: \n"))
b = int(input("inserisci b: \n"))
c = int(input("inserisci c: \n"))

if a == 0:
    primogrado()
elif a != 0:
    delta = (b*b)-4*a*c
    if delta < 0:
        print("impossibile")
    elif delta >= 0:
        x1 = (-b+math.sqrt(delta))/2*a
        x2 = (-b-math.sqrt(delta))/2*a
        print(x1, x2)