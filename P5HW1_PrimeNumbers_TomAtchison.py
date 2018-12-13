# This program tells the user if they entered a prime number or not.
# 09 November 2018
# CTI-110 P5HW1 - Prime Numbers
# Tom Atchison


# boolean function for "isPrime" determines if number is prime or
# not prime.
def isPrime(number):
    thisZero = 0
    if number <=1:
        return False
    for i in range(1, number + 1):
        if number % i == 0:
            thisZero = thisZero + 1
            if thisZero > 2:
                return False
    return True
# Main function asks for input.
def main():
    number = int(input("Please enter a number: "))
    # Inserts space between lines.
    print()
    if isPrime(number):
        # States if number is prime.
        print(number, "is a prime number.")
        print() 
    else:
        # States if number is not prime.
        print("Sorry,", number, "is not a prime number.")
        print()
# Call main function          
main ()    


# I spent many hours last night attempting to put in a simple yes or no loop
# so I didn't have to re run the script every time I wanted to check a new
# number.  I could not figure it out, but I got very close using "while".
# I also tried the "def" function, "if else" and "for".  Just to satisfy my
# curiosity, what kind of loop is best?
    
    
        

    
    
