# CTI-110 
# P3HW2 - Shipping Charges 
# Tom Atchison 
# 07 Oct 2018
#
# Display shipping charges for Fast Freight Shipping Company 
# after inputting the weight of the package.
# 2 lbs and less = $1.50
# More than 2 lbs to 6 lbs = $3.00
# More than 6 lbs to 10 lbs = $4.00
# More than 10 lbs = $4.75
#
def main():
    print ('Welcome to Fast Freight Shipping Company.')
    # input weight of package
    weight = int (input ('How many pounds does your package weigh? '))
    # output shipping charges
    if weight <= 2:
        print ('Your shipping charges are $1.50.')
    else:
        if weight <= 6:
            print ('Your shipping charges are $3.00.')
        else:
            if weight <= 10:
                print ('Your shipping charges are $4.00')
            else:
                if weight > 10:
                    print ('Your shipping charges are $4.75')
main()
                            
                
