number = 6
prime = True 

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            prime = False
            break  

if prime:
    print("The Number", number, "is prime")
else:
    print("The Number", number, "is not prime")
