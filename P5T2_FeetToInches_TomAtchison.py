# This program converts from f33t_to_inches.
# 09 November 2018
# CTI-110 P5T2_FeetToInches 
# Tom Atchison

# Constant of inches per foot.
inchesPerFoot = 12
# Use main function to get input in feet and output inches
def main():

    # Enter feet.
    feet = int(input("Enter your number in feet: "))

    # Display inches.
    print(feet, "feet equals", feet_to_inches(feet), "inches.")

# Convert feet to inches.    
def feet_to_inches(feet):
    return feet * inchesPerFoot

# Call the main function
main()
