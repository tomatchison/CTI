# This program converts from kilometers to miles.
# 09 November 2018
# CTI-110 P5T1_KilometerConverter 
# Tom Atchison



# Constant for conversion.
conversionFactor = 0.6214
#
# Use main function to get the distance in kilometers and call showMiles
# function to convert to miles
def main():
    
    # Get distance in kilometers.
    kilometers = float(input("Enter a distance in kilometers: "))
    
    # Display distance in miles.
    showMiles (kilometers)

# The showMiles function converts the parameter km from kilometers to miles
# and displays the result.
def showMiles(km):

    # Calcutlate miles.
    miles = km * conversionFactor

    # Display miles
    print (km, "kilometers equals", miles, "miles.")

# Call main function
main ()
