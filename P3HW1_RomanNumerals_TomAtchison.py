# CTI-110 
# P3HW1 - Roman Numerals 
# Tom Atchison 
# 07 Oct 2018
#
# Prompt user to enter a number within the range of 1 through 10.
# Display Roman Numeral of that number.
# If the prompted number is outside the range of 1 through 10, display error message.
#
def main():
    # Prompt user for number from 1 to 10.
    number = int (input ('Please enter a number between 1 and 10. '))
    # Print the Roman Numeral from 1 to 10.
    if number == 1:
        print ('The Roman Numeral for number 1 is I.')
    if number == 2:
        print ('The Roman Numeral for number 2 is II.')
    if number == 3:
        print ('The Roman Numeral for number 3 is III.')
    if number == 4:
        print ('The Roman Numeral for number 4 is IV.')
    if number == 5:
        print ('The Roman Numeral for number 5 is V.')
    if number == 6:
        print ('The Roman Numeral for number 6 is VI.')
    if number == 7:
       print ('The Roman Numeral for number 7 is VII.')
    if number == 8:
        print ('The Roman Numeral for number 8 is VIII.')
    if number == 9:
        print ('The Roman Numeral for number 9 is IX.')
    if number == 10:
        print ('The Roman Numeral for number 10 is X.')
    # Print error message if number out of range.
    if number > 10:
        print ('You have mistakenly entered an invalid number.')
        print ('Please try again.')
    if number <= 0:
        print ('You have mistakenly entered an invalid number.')
        print ('Please try again.') 
main()





           
