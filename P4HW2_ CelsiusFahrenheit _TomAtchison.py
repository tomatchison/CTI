# Display a table that goes from 0 - 20 degrees Celsius and
# it's equivalant in Fahrenheit
# 26 October 2018
# CTI-110 P4HW2 - Celsius to Fahrenheit Table
# Tom Atchison
#


lowtemp = 0         # starting temperature
hightemp = 21       # Ending temperature
increment = 1       # Temperature increments

# Print the table headings
print("Celsius\t  Fahrenheit")
print("--------------------")

# Output for both temperatures
for C in range(lowtemp, hightemp, increment):
    F = ( ( 9 / 5 ) * C ) + 32
    print(C, "\t  ", format(F, ".2f"))
    
