
# for i in range (start,stop) : i prendra successivement les valeurs 1 à 21-1 (20)
# % modulo renvoie le reste de la division entre les nombres

for i in range (1,21):
    if i%15==0:
        print("fizzBuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)