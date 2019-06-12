def is_prime(number,counter = 1,devisibles = 0):
    while counter <= number:
        if number % counter == 0:
            devisibles += 1
        counter += 1
    if devisibles == 2:
        return(True)
    else:
        return(False)

print(is_prime(1))

print(is_prime(2))

print(is_prime(10))

print(is_prime(13))

print(is_prime(17))
