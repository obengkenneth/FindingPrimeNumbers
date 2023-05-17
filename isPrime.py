number = int(input("Enter a number : ")
)
def isPrime(number):
    primeNumbers = [3, 5, 7, 9, 11, 13, 17]
    return True if number > 2 and number in primeNumbers else False 

print(isPrime(number) )  
