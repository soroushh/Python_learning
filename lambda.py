lambda_function = lambda name,family : "The full name is " + name +" "+ family

print(lambda_function("soroush","khosravi"))

def lambda_user(number):
    return lambda x : x*number

first = lambda_user(6)

print(first(5))
