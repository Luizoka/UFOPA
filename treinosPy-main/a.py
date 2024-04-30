n = 5
h = 1
x = 0
cont = 0

while x < 1000:
    x = n * h
    h += 1
    cont +=500

print("O valor final de x é:", cont)